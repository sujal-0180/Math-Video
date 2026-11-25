"""Build pipeline for the Gaussian Elimination M3 Animation Video.
Renders all Manim scenes, pads/normalizes the voice-over audio, concatenates
the video segments, and muxes the final 1080p 16:9 _Video.mp4.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE_DIR = ROOT / "_Code"
ASSETS_DIR = ROOT / "assets"
BUILD_DIR = ROOT / "build"
MEDIA_DIR = ROOT / "media"

SCENES = [
    ("scene0_intro.py", "OpeningFrame"),
    ("scene1_hook.py", "Scene1Hook"),
    ("scene2_concept.py", "Scene2Concept"),
    ("scene3_intuition.py", "Scene3Intuition"),
    ("scene4_example.py", "Scene4Example"),
    ("scene5_interpretation.py", "Scene5Interpretation"),
    ("scene6_summary.py", "Scene6Summary"),
]

QUALITY_MAP = {
    "l": ("-ql", "480p15"),
    "m": ("-qm", "720p30"),
    "h": ("-qh", "1080p60"),
}


def run(cmd: list[str], cwd: Path | None = None):
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quality", choices=["l", "m", "h"], default="h")
    args = parser.parse_args()

    q_flag, q_folder = QUALITY_MAP[args.quality]
    manim_bin = str(ROOT / ".venv" / "bin" / "manim")
    ffmpeg_bin = "/opt/homebrew/bin/ffmpeg"

    BUILD_DIR.mkdir(exist_ok=True)
    rendered_files: list[Path] = []

    for script, cls_name in SCENES:
        run([manim_bin, q_flag, "--media_dir", str(MEDIA_DIR), str(CODE_DIR / script), cls_name], cwd=CODE_DIR)
        stem = Path(script).stem
        out_mp4 = MEDIA_DIR / "videos" / stem / q_folder / f"{cls_name}.mp4"
        if not out_mp4.exists():
            raise FileNotFoundError(f"Expected rendered video not found: {out_mp4}")
        rendered_files.append(out_mp4)

    # Create ffmpeg concat list
    concat_txt = BUILD_DIR / "concat.txt"
    with open(concat_txt, "w") as f:
        for p in rendered_files:
            f.write(f"file '{p.as_posix()}'\n")

    video_silent = BUILD_DIR / "video_silent.mp4"
    run([
        ffmpeg_bin, "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_txt),
        "-c", "copy",
        str(video_silent),
    ])

    # Normalize voiceover, prepend exact 5.0s silence for Opening Frame, and pad tail
    audio_ready = BUILD_DIR / "voiceover_synced.m4a"
    run([
        ffmpeg_bin, "-y",
        "-f", "lavfi", "-t", "5.0", "-i", "anullsrc=r=48000:cl=stereo",
        "-i", str(ASSETS_DIR / "voiceover.m4a"),
        "-filter_complex", "[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[norm];[0:a][norm]concat=n=2:v=0:a=1,apad[out]",
        "-map", "[out]",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", "311.97",
        str(audio_ready),
    ])

    # Mux final _Video.mp4
    final_mp4 = ROOT / "_Video.mp4"
    run([
        ffmpeg_bin, "-y",
        "-i", str(video_silent),
        "-i", str(audio_ready),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        "-shortest",
        str(final_mp4),
    ])
    print(f"\nDONE! Final video written to: {final_mp4}")


if __name__ == "__main__":
    main()

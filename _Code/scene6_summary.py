"""Scene 6: Summary & Closing Credits (audio 266.40 - 301.20s + 7.0s outro = 41.80s).
Recaps 3 core takeaways and displays the required Closing Frame with references,
student info, and AI disclosure.
"""

from manim import *
from theme import *


class Scene6Summary(Scene):
    def construct(self):
        elapsed = 0.0

        def sync(target_t: float):
            nonlocal elapsed
            dt = target_t - elapsed
            if dt > 0.01:
                self.wait(dt)
                elapsed = target_t

        def play_sync(*anims, run_time: float = 1.0):
            nonlocal elapsed
            self.play(*anims, run_time=run_time)
            elapsed += run_time

        header = make_section_header("06", "SUMMARY & CREDITS")
        play_sync(FadeIn(header), run_time=0.4)

        # --- 0.40 - 23.48s: Three Core Takeaways ---
        title = txt("Three Core Takeaways", size=38, color=GOLD, weight=BOLD).shift(UP * 2.45)

        def takeaway_card(num: str, heading: str, body: str, color: str) -> VGroup:
            n = mono(num, size=30, color=color, weight=BOLD)
            h = txt(heading, size=23, color=TEXT_PRIMARY, weight=BOLD)
            b = txt(body, size=18, color=TEXT_MUTED)
            text_col = VGroup(h, b).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
            row = VGroup(n, text_col).arrange(RIGHT, buff=0.45)
            c = make_card(max(11.8, row.width + 1.0), 1.35, stroke_color=color, stroke_width=2.2)
            row.move_to(c.get_center()).align_to(c, LEFT).shift(RIGHT * 0.45)
            return VGroup(c, row)

        t1 = takeaway_card(
            "01",
            "Augmented Matrix [ A | b ]",
            "Packages a linear system into a grid where row operations preserve the solution.",
            TEAL,
        )
        t2 = takeaway_card(
            "02",
            "Gaussian Elimination",
            "Builds a staircase of pivots through swaps, scaling, and row replacement.",
            GOLD,
        )
        t3 = takeaway_card(
            "03",
            "Back-Substitution",
            "Peels equations from the bottom up to reveal the exact solution.",
            CYAN,
        )
        cards = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).shift(DOWN * 0.35)

        play_sync(Write(title), run_time=1.0)
        sync(2.1)
        play_sync(FadeIn(t1, shift=RIGHT * 0.25), run_time=1.4)
        sync(11.0)
        play_sync(FadeIn(t2, shift=RIGHT * 0.25), run_time=1.4)
        sync(19.1)
        play_sync(FadeIn(t3, shift=RIGHT * 0.25), run_time=1.4)
        sync(23.5)

        play_sync(FadeOut(VGroup(title, cards)), run_time=0.7)

        # --- 23.70 - 41.80s: Closing Frame & Credits ---
        end_title = txt("Thank You for Watching!", size=44, color=GOLD, weight=BOLD).shift(UP * 2.1)
        sub = txt("Gaussian Elimination  •  M3 Internal Assessment", size=24, color=TEXT_PRIMARY)
        sub.next_to(end_title, DOWN, buff=0.25)

        cred_card = make_card(10.6, 2.5, stroke_color=CARD_BORDER, stroke_width=2.0)
        cred_card.shift(DOWN * 0.75)

        c_lines = VGroup(
            txt("Created & Narrated by:  P. Sujal  (URN: E25B070607)", size=22, color=TEAL, weight=BOLD),
            txt("Animation Engine:  Manim Community Edition (Python)  &  FFmpeg", size=20, color=TEXT_PRIMARY),
            txt("References:  Gilbert Strang (Intro to Linear Algebra)  •  3Blue1Brown", size=20, color=TEXT_MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        c_lines.move_to(cred_card.get_center())

        play_sync(
            Write(end_title),
            FadeIn(sub),
            FadeIn(cred_card),
            FadeIn(c_lines),
            run_time=1.8,
        )
        sync(40.80)
        play_sync(FadeOut(VGroup(header, end_title, sub, cred_card, c_lines)), run_time=1.0)

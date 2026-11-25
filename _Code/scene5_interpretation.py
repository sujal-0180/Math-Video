"""Scene 5: Geometric Interpretation & Verification (audio 218.72 - 266.40s, duration = 47.68s).
Connects the Row-Echelon Form algebra back to 3D geometry (highlighting z = 3),
peels the planes via back-substitution, and verifies (2, -1, 3) in the original equations.
"""

from manim import *
from theme import *


class Scene5Interpretation(ThreeDScene):
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

        self.set_camera_orientation(phi=68 * DEGREES, theta=-45 * DEGREES, focal_distance=10)

        header = make_section_header("05", "GEOMETRIC INTERPRETATION")
        self.add_fixed_in_frame_mobjects(header)
        header.set_opacity(0)

        # 3D Axes shifted right, centered around (2, -1, 3) in local coordinates
        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2.0, 2.0, 1],
            x_length=4.6,
            y_length=4.6,
            z_length=3.8,
            axis_config={"color": TEXT_MUTED, "stroke_width": 1.6},
        ).shift(RIGHT * 2.2 + DOWN * 0.2)
        center_pt = axes.c2p(0, 0, 0)

        # Original tilted planes (around intersection)
        orig_p1 = Surface(
            lambda u, v: axes.c2p(u, v, -u - v),
            u_range=[-1.4, 1.4],
            v_range=[-1.4, 1.4],
            resolution=(5, 5),
            fill_color=TEAL,
            fill_opacity=0.28,
            stroke_color=TEAL,
            stroke_width=0.6,
        )
        orig_p2 = Surface(
            lambda u, v: axes.c2p(u, 2 * u + v, v),
            u_range=[-1.0, 1.0],
            v_range=[-1.2, 1.2],
            resolution=(5, 5),
            fill_color=PURPLE,
            fill_opacity=0.28,
            stroke_color=PURPLE,
            stroke_width=0.6,
        )
        orig_p3 = Surface(
            lambda u, v: axes.c2p(u, v, u + 2 * v),
            u_range=[-1.0, 1.0],
            v_range=[-1.0, 1.0],
            resolution=(5, 5),
            fill_color=CORAL,
            fill_opacity=0.30,
            stroke_color=CORAL,
            stroke_width=0.6,
        )

        # Simplified Row-Echelon planes:
        # R3: z = 3 (flat horizontal plane!)
        ref_p3 = Surface(
            lambda u, v: axes.c2p(u, v, 0.0),
            u_range=[-1.9, 1.9],
            v_range=[-1.9, 1.9],
            resolution=(6, 6),
            fill_color=GOLD,
            fill_opacity=0.38,
            stroke_color=GOLD,
            stroke_width=0.8,
        )
        # R2: y - 2z = -7 -> y = 2z (in local coords)
        ref_p2 = Surface(
            lambda u, v: axes.c2p(u, 0.8 * v, v),
            u_range=[-1.8, 1.8],
            v_range=[-1.4, 1.4],
            resolution=(6, 6),
            fill_color=CYAN,
            fill_opacity=0.28,
            stroke_color=CYAN,
            stroke_width=0.6,
        )

        sol_dot = Dot3D(point=center_pt, radius=0.14, color=GOLD)
        sol_halo = Sphere(center=center_pt, radius=0.24, resolution=(12, 12))
        sol_halo.set_color(GOLD).set_opacity(0.28)

        # Left HUD card: Original vs Row-Echelon
        hud1 = make_card(5.85, 1.85, stroke_color=TEAL)
        h1_t = txt("Original Planes → Tilted", size=20, color=TEXT_MUTED, weight=BOLD)
        h1_s = txt("Row-Echelon Form → Simplified!", size=21, color=GOLD, weight=BOLD)
        h1_z = mono("R₃: z = 3  (Flat Horizontal Plane)", size=17, color=GOLD)
        hud1_g = VGroup(hud1, VGroup(h1_t, h1_s, h1_z).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(hud1))
        hud1_g.to_corner(UL, buff=0.45).shift(DOWN * 0.75)
        self.add_fixed_in_frame_mobjects(hud1_g)
        hud1_g.set_opacity(0)

        # --- 0.00 - 14.20s: Original tilted -> Row-Echelon flat z = 3 ---
        play_sync(
            header.animate.set_opacity(1),
            hud1_g.animate.set_opacity(1),
            Create(axes),
            FadeIn(orig_p1),
            FadeIn(orig_p2),
            FadeIn(orig_p3),
            FadeIn(sol_dot),
            FadeIn(sol_halo),
            run_time=1.8,
        )
        self.begin_ambient_camera_rotation(rate=0.10)
        sync(7.0)
        play_sync(
            ReplacementTransform(orig_p3, ref_p3),
            ReplacementTransform(orig_p2, ref_p2),
            run_time=2.5,
        )
        sync(14.5)

        # --- 14.50 - 25.20s: Same intersection point (2, -1, 3) ---
        pt_badge = make_badge("Exact Same Point: (2, −1, 3)", accent=GOLD, font_size=21)
        pt_badge.next_to(hud1_g, DOWN, buff=0.35, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(pt_badge)
        pt_badge.set_opacity(0)

        play_sync(pt_badge.animate.set_opacity(1), Indicate(sol_dot, color=GOLD, scale_factor=1.5), run_time=1.4)
        sync(25.2)

        # --- 25.20 - 34.20s: Peeling planes one at a time ---
        peel_card = make_card(5.85, 1.5, stroke_color=CYAN)
        peel_t = txt("Peeling Planes Backwards:", size=20, color=CYAN, weight=BOLD)
        peel_s = mono("z = 3  →  y = −1  →  x = 2", size=21, color=TEXT_PRIMARY, weight=BOLD)
        peel_g = VGroup(peel_card, VGroup(peel_t, peel_s).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(peel_card))
        peel_g.next_to(pt_badge, DOWN, buff=0.35, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(peel_g)
        peel_g.set_opacity(0)

        play_sync(peel_g.animate.set_opacity(1), Indicate(ref_p3, color=GOLD), run_time=1.5)
        sync(30.2)
        play_sync(Indicate(ref_p2, color=CYAN), run_time=1.5)
        play_sync(Indicate(sol_dot, color=GOLD, scale_factor=1.5), run_time=1.2)
        sync(34.2)

        # --- 34.20 - 47.60s: Verification Card ---
        ver_card = make_card(5.85, 2.8, stroke_color=GREEN, stroke_width=2.4)
        ver_title = txt("Verify Solution  (2, −1, 3)", size=22, color=GREEN, weight=BOLD)
        v1 = mono(" 2 + (−1) + 3  =  4  ✓", size=20, color=TEXT_PRIMARY)
        v2 = mono("2(2) − (−1) + 3 =  8  ✓", size=20, color=TEXT_PRIMARY)
        v3 = mono(" 2 + 2(−1) − 3  = −3  ✓", size=20, color=TEXT_PRIMARY)
        ver_rows = VGroup(ver_title, v1, v2, v3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        ver_g = VGroup(ver_card, ver_rows.move_to(ver_card.get_center()))
        ver_g.to_corner(DL, buff=0.5)
        self.add_fixed_in_frame_mobjects(ver_g)
        ver_g.set_opacity(0)

        play_sync(
            FadeOut(VGroup(hud1_g, pt_badge, peel_g)),
            ver_g.animate.set_opacity(1),
            run_time=1.4,
        )
        sync(46.80)
        self.stop_ambient_camera_rotation()
        play_sync(
            FadeOut(VGroup(axes, orig_p1, ref_p2, ref_p3, sol_dot, sol_halo)),
            FadeOut(VGroup(header, ver_g)),
            run_time=0.8,
        )

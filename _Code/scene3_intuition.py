"""Scene 3: Visual Intuition (audio 71.56 - 113.76s, duration = 42.20s).
3D geometric interpretation: 3 planes intersecting at a point, and why the
three elementary row operations preserve the solution set.
"""

from manim import *
from theme import *


class Scene3Intuition(ThreeDScene):
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

        # Set 3D camera orientation with frame_center shifted left so 3D plot sits cleanly on the right
        self.set_camera_orientation(phi=68 * DEGREES, theta=-45 * DEGREES, focal_distance=10, frame_center=[-2.5, 0.0, 0.0])

        # Fixed HUD elements (2D overlay)
        header = make_section_header("03", "GEOMETRIC INTUITION")
        self.add_fixed_in_frame_mobjects(header)
        header.set_opacity(0)

        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2.0, 2.0, 1],
            x_length=4.0,
            y_length=4.0,
            z_length=3.4,
            axis_config={"color": TEXT_MUTED, "stroke_width": 1.6},
        )

        center_pt = axes.c2p(0, 0, 0)

        # Plane 1 (Teal): horizontal z = 0
        plane1 = Surface(
            lambda u, v: axes.c2p(u, v, 0.0),
            u_range=[-2.0, 2.0],
            v_range=[-2.0, 2.0],
            resolution=(6, 6),
            fill_color=TEAL,
            fill_opacity=0.35,
            stroke_color=TEAL,
            stroke_width=0.6,
        )

        # Plane 2 (Cyan): tilted y = 0.45x + 0.35z
        plane2 = Surface(
            lambda u, v: axes.c2p(u, 0.45 * u + 0.35 * v, v),
            u_range=[-1.8, 1.8],
            v_range=[-1.6, 1.6],
            resolution=(6, 6),
            fill_color=CYAN,
            fill_opacity=0.32,
            stroke_color=CYAN,
            stroke_width=0.6,
        )

        # Plane 3 (Coral): passes through Y-axis (intersection with Plane 1!)
        # Initially x = 0.55 * z
        plane3 = Surface(
            lambda u, v: axes.c2p(0.55 * v, u, v),
            u_range=[-1.8, 1.8],
            v_range=[-1.6, 1.6],
            resolution=(6, 6),
            fill_color=CORAL,
            fill_opacity=0.38,
            stroke_color=CORAL,
            stroke_width=0.6,
        )

        # Glowing intersection sphere at (0,0,0)
        sol_dot = Dot3D(point=center_pt, radius=0.14, color=GOLD)
        sol_halo = Sphere(center=center_pt, radius=0.24, resolution=(12, 12))
        sol_halo.set_color(GOLD).set_opacity(0.28)

        # Left HUD caption
        hud_title = txt("3 Equations = 3 Planes in 3D", size=24, color=TEXT_PRIMARY, weight=BOLD)
        hud_sub = txt("Solution = Single Intersection Point", size=20, color=GOLD, weight=BOLD)
        hud_grp = VGroup(hud_title, hud_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        hud_grp.to_corner(UL, buff=0.5).shift(DOWN * 0.65)
        self.add_fixed_in_frame_mobjects(hud_grp)
        hud_grp.set_opacity(0)

        # --- 0.00 - 10.04s: Reveal 3D planes & intersection ---
        play_sync(
            header.animate.set_opacity(1),
            hud_grp.animate.set_opacity(1),
            Create(axes),
            run_time=1.4,
        )
        play_sync(FadeIn(plane1), FadeIn(plane2), FadeIn(plane3), run_time=2.0)
        sync(4.8)
        play_sync(FadeIn(sol_dot, scale=1.5), FadeIn(sol_halo), run_time=1.0)
        sync(14.5)

        # --- 14.50 - 20.00s: Op 1: Swap Rows ---
        op1 = make_card(5.85, 1.45, stroke_color=TEAL, stroke_width=2.2)
        op1_t = txt("1. Swap Rows  (Rᵢ ↔ Rⱼ)", size=22, color=TEAL, weight=BOLD)
        op1_d = txt("Reorders equations — planes stay identical", size=18, color=TEXT_MUTED)
        op1_g = VGroup(op1, VGroup(op1_t, op1_d).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(op1))
        op1_g.to_edge(LEFT, buff=0.45).shift(UP * 0.85)
        self.add_fixed_in_frame_mobjects(op1_g)
        op1_g.set_opacity(0)

        play_sync(op1_g.animate.set_opacity(1), run_time=0.9)
        play_sync(Indicate(plane1, color=GOLD), Indicate(plane2, color=GOLD), run_time=1.2)
        sync(19.8)

        # --- 19.80 - 24.20s: Op 2: Scale Row ---
        op2 = make_card(5.85, 1.45, stroke_color=CYAN, stroke_width=2.2)
        op2_t = txt("2. Scale a Row  (Rᵢ → k·Rᵢ, k ≠ 0)", size=22, color=CYAN, weight=BOLD)
        op2_d = txt("Multiplies equation — keeps the same plane", size=18, color=TEXT_MUTED)
        op2_g = VGroup(op2, VGroup(op2_t, op2_d).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(op2))
        op2_g.next_to(op1_g, DOWN, buff=0.28)
        self.add_fixed_in_frame_mobjects(op2_g)
        op2_g.set_opacity(0)

        play_sync(op2_g.animate.set_opacity(1), run_time=0.9)
        play_sync(Indicate(plane2, color=CYAN), run_time=1.2)
        sync(24.2)

        # --- 24.20 - 35.40s: Op 3: Row Replacement (hinge Plane 3 on intersection line!) ---
        op3 = make_card(5.85, 1.55, stroke_color=CORAL, stroke_width=2.4)
        op3_t = txt("3. Row Replacement  (Rᵢ → Rᵢ + k·Rⱼ)", size=21, color=CORAL, weight=BOLD)
        op3_d = txt("Tilts plane around shared intersection line", size=18, color=TEXT_MUTED)
        op3_g = VGroup(op3, VGroup(op3_t, op3_d).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(op3))
        op3_g.next_to(op2_g, DOWN, buff=0.28)
        self.add_fixed_in_frame_mobjects(op3_g)
        op3_g.set_opacity(0)

        # Highlight the hinge line (Y-axis through center_pt)
        hinge_line = Line3D(
            start=axes.c2p(0, -1.8, 0),
            end=axes.c2p(0, 1.8, 0),
            color=GOLD,
            thickness=0.03,
        )

        play_sync(op3_g.animate.set_opacity(1), Create(hinge_line), run_time=1.2)
        sync(28.8)
        # Rotate Plane 3 around the Y-axis passing through center_pt!
        play_sync(
            Rotate(plane3, angle=-42 * DEGREES, axis=UP, about_point=center_pt),
            run_time=4.5,
        )
        sync(35.4)

        # --- 35.40 - 42.80s: Intersection never moves! ---
        banner = make_badge(
            "Intersection Point NEVER Moves → Same Solution!",
            accent=GOLD,
            font_size=22,
            padding_x=0.5,
            padding_y=0.24,
        )
        banner.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(banner)
        banner.set_opacity(0)

        play_sync(banner.animate.set_opacity(1), Indicate(sol_dot, color=GOLD, scale_factor=1.4), run_time=1.4)
        sync(42.00)
        play_sync(
            FadeOut(VGroup(axes, plane1, plane2, plane3, sol_dot, sol_halo, hinge_line)),
            FadeOut(VGroup(header, hud_grp, op1_g, op2_g, op3_g, banner)),
            run_time=0.8,
        )

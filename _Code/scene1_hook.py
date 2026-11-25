"""Scene 1: Hook / Context (audio 0.00 - 27.88s, duration = 27.88s).
Motivates why linear systems matter (bridges, neural nets, supply chains),
contrasts 2x2 line intersection with n x n complexity, and introduces Gaussian Elimination.
"""

from manim import *
from theme import *


class Scene1Hook(Scene):
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

        header = make_section_header("01", "HOOK & MOTIVATION")
        play_sync(FadeIn(header), run_time=0.5)

        # --- 0.50 - 6.88s: Three real-world application cards ---
        # Card 1: Bridge Forces
        c1 = make_card(3.6, 2.5, stroke_color=TEAL)
        c1_title = txt("Bridge Forces", size=24, color=TEAL, weight=BOLD)
        # Simple truss diagram
        p1, p2, p3, p4 = [-1.0, -0.4, 0], [0.0, 0.4, 0], [1.0, -0.4, 0], [0.0, -0.4, 0]
        truss = VGroup(
            Line(p1, p2, color=TEXT_PRIMARY, stroke_width=2.5),
            Line(p2, p3, color=TEXT_PRIMARY, stroke_width=2.5),
            Line(p1, p3, color=TEXT_PRIMARY, stroke_width=2.5),
            Line(p2, p4, color=GOLD, stroke_width=2.5),
            Dot(p1, color=TEAL, radius=0.06),
            Dot(p2, color=GOLD, radius=0.07),
            Dot(p3, color=TEAL, radius=0.06),
        ).shift(DOWN * 0.25)
        c1_title.move_to(c1.get_top() + DOWN * 0.42)
        g1 = VGroup(c1, c1_title, truss).move_to(LEFT * 4.3 + UP * 0.55)

        # Card 2: Neural Network
        c2 = make_card(3.6, 2.5, stroke_color=CYAN)
        c2_title = txt("Neural Networks", size=24, color=CYAN, weight=BOLD)
        c2_title.move_to(c2.get_top() + DOWN * 0.42)
        l_nodes = [Dot([-0.9, y, 0], color=CYAN, radius=0.08) for y in [-0.5, 0.0, 0.5]]
        r_nodes = [Dot([0.9, y, 0], color=GOLD, radius=0.08) for y in [-0.35, 0.35]]
        edges = [
            Line(a.get_center(), b.get_center(), color=TEXT_MUTED, stroke_width=1.4)
            for a in l_nodes for b in r_nodes
        ]
        nn_diag = VGroup(*edges, *l_nodes, *r_nodes).shift(DOWN * 0.28)
        g2 = VGroup(c2, c2_title, nn_diag).move_to(ORIGIN + UP * 0.55)

        # Card 3: Supply Chain
        c3 = make_card(3.6, 2.5, stroke_color=PURPLE)
        c3_title = txt("Supply Chains", size=24, color=PURPLE, weight=BOLD)
        c3_title.move_to(c3.get_top() + DOWN * 0.42)
        s_nodes = [
            Dot([-0.9, 0.3, 0], color=PURPLE, radius=0.09),
            Dot([-0.9, -0.45, 0], color=PURPLE, radius=0.09),
            Dot([0.0, 0.0, 0], color=GOLD, radius=0.10),
            Dot([0.95, 0.3, 0], color=GREEN, radius=0.09),
            Dot([0.95, -0.45, 0], color=GREEN, radius=0.09),
        ]
        s_arrows = [
            Arrow(s_nodes[0].get_center(), s_nodes[2].get_center(), buff=0.1, color=TEXT_MUTED, stroke_width=2, tip_length=0.14),
            Arrow(s_nodes[1].get_center(), s_nodes[2].get_center(), buff=0.1, color=TEXT_MUTED, stroke_width=2, tip_length=0.14),
            Arrow(s_nodes[2].get_center(), s_nodes[3].get_center(), buff=0.1, color=GOLD, stroke_width=2, tip_length=0.14),
            Arrow(s_nodes[2].get_center(), s_nodes[4].get_center(), buff=0.1, color=GOLD, stroke_width=2, tip_length=0.14),
        ]
        sc_diag = VGroup(*s_arrows, *s_nodes).shift(DOWN * 0.25)
        g3 = VGroup(c3, c3_title, sc_diag).move_to(RIGHT * 4.3 + UP * 0.55)

        play_sync(FadeIn(g1, shift=UP * 0.25), run_time=1.2)
        sync(2.7)
        play_sync(FadeIn(g2, shift=UP * 0.25), run_time=1.2)
        sync(4.5)
        play_sync(FadeIn(g3, shift=UP * 0.25), run_time=1.2)
        sync(6.86)

        # --- 6.86 - 12.22s: Converge to "Solving a System of Linear Equations" ---
        core_txt = txt("Solving a System of Linear Equations", size=28, color=GOLD, weight=BOLD)
        core_card = make_card(max(8.4, core_txt.width + 1.0), 1.35, stroke_color=GOLD, stroke_width=2.5)
        core_card.shift(DOWN * 2.05)
        core_txt.move_to(core_card.get_center())

        arr1 = Arrow(g1.get_bottom(), core_card.get_top() + LEFT * 2.0, color=TEAL, buff=0.15)
        arr2 = Arrow(g2.get_bottom(), core_card.get_top(), color=CYAN, buff=0.15)
        arr3 = Arrow(g3.get_bottom(), core_card.get_top() + RIGHT * 2.0, color=PURPLE, buff=0.15)

        play_sync(GrowArrow(arr1), GrowArrow(arr2), GrowArrow(arr3), run_time=1.0)
        sync(9.8)
        play_sync(FadeIn(core_card, scale=0.95), Write(core_txt), run_time=1.6)
        sync(12.8)

        # Clear cards
        play_sync(
            FadeOut(VGroup(g1, g2, g3, arr1, arr2, arr3, core_card, core_txt)),
            run_time=0.5,
        )

        # --- 13.40 - 17.50s: 2D two-line intersection ---
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4.2,
            y_length=4.2,
            axis_config={"color": TEXT_MUTED, "include_tip": True},
        ).shift(LEFT * 3.3 + DOWN * 0.2)
        ax_lbl = txt("2 Unknowns: Easy to Sketch", size=22, color=TEAL, weight=BOLD)
        ax_lbl.next_to(axes, UP, buff=0.25)

        line1 = axes.plot(lambda x: 0.5 * x + 2.0, x_range=[0.2, 4.6], color=CYAN, stroke_width=3.5)
        line2 = axes.plot(lambda x: -1.0 * x + 5.0, x_range=[0.4, 4.6], color=CORAL, stroke_width=3.5)
        cross_dot = Dot(axes.c2p(2, 3), color=GOLD, radius=0.11)
        cross_lbl = mono("(2, 3)", size=22, color=GOLD, weight=BOLD).next_to(cross_dot, UR, buff=0.12)

        play_sync(Create(axes), FadeIn(ax_lbl), run_time=0.9)
        play_sync(Create(line1), Create(line2), run_time=1.0)
        sync(15.7)
        play_sync(FadeIn(cross_dot, scale=1.5), FadeIn(cross_lbl), run_time=0.8)
        sync(17.7)

        # --- 17.70 - 23.50s: 3, 10, 10,000 unknowns ---
        scale_title = txt("3, 10, or 10,000 Unknowns?", size=23, color=CORAL, weight=BOLD)
        dims = VGroup(
            mono("3 × 3           →  3 planes in 3D", size=19, color=TEXT_PRIMARY),
            mono("10 × 10         →  10 hyperplanes", size=19, color=TEXT_MUTED),
            mono("10,000 × 10,000 →  Impossible by eye!", size=18, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        box_w = max(5.8, dims.width + 0.85, scale_title.width + 0.85)
        scale_box = make_card(box_w, 4.2, stroke_color=CORAL)
        scale_box.shift(RIGHT * 3.0 + DOWN * 0.2)
        scale_title.move_to(scale_box.get_top() + DOWN * 0.55)
        dims.move_to(scale_box.get_center() + DOWN * 0.25)

        play_sync(FadeIn(scale_box), Write(scale_title), run_time=0.8)
        play_sync(LaggedStart(*[FadeIn(d, shift=RIGHT * 0.2) for d in dims], lag_ratio=0.4), run_time=2.2)
        sync(23.2)

        # --- 23.20 - 26.60s: Reveal "Gaussian Elimination" ---
        play_sync(
            FadeOut(VGroup(axes, ax_lbl, line1, line2, cross_dot, cross_lbl, scale_box, scale_title, dims)),
            run_time=0.5,
        )
        hero_sub = txt("THE SYSTEMATIC ALGORITHM", size=20, color=CYAN, weight=BOLD)
        hero_title = txt("Gaussian Elimination", size=54, color=GOLD, weight=BOLD)
        hero_grp = VGroup(hero_sub, hero_title).arrange(DOWN, buff=0.22)
        hero_box = make_card(max(9.0, hero_grp.width + 1.2), 2.1, stroke_color=GOLD, stroke_width=3.0)
        hero_grp.move_to(hero_box.get_center())
        play_sync(FadeIn(hero_box, scale=0.92), Write(hero_title), FadeIn(hero_sub), run_time=1.2)
        sync(26.10)
        play_sync(FadeOut(VGroup(header, hero_box, hero_grp)), run_time=0.5)

"""Scene 2: Concept Introduction (audio 27.88 - 71.56s, duration = 43.68s).
Presents the learning goal, Ax = b matrix notation, Augmented Matrix [A | b],
and the target Row-Echelon Form staircase.
"""

from manim import *
from theme import *


class Scene2Concept(Scene):
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

        header = make_section_header("02", "CONCEPT & NOTATION")
        play_sync(FadeIn(header), run_time=0.4)

        # --- 0.40 - 9.30s: Learning Objective ---
        line1 = txt("1. Understand WHY Gaussian elimination works geometrically", size=24, color=TEXT_PRIMARY)
        line2 = txt("2. Apply it step-by-step using Row-Echelon Form", size=24, color=GOLD, weight=BOLD)
        goal_lines = VGroup(line1, line2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        goal_card = make_card(max(11.2, goal_lines.width + 1.1), 2.8, stroke_color=CYAN, stroke_width=2.5)
        goal_tag = make_badge("LEARNING OBJECTIVE", accent=CYAN, font_size=18)
        goal_tag.move_to(goal_card.get_top() + DOWN * 0.45)
        goal_lines.move_to(goal_card.get_center() + DOWN * 0.25)

        play_sync(FadeIn(goal_card), FadeIn(goal_tag), run_time=0.9)
        play_sync(Write(line1), run_time=2.2)
        sync(6.1)
        play_sync(Write(line2), run_time=2.0)
        sync(9.8)
        play_sync(FadeOut(VGroup(goal_card, goal_tag, goal_lines)), run_time=0.6)

        # --- 9.30 - 21.80s: Matrix equation A x = b ---
        # Show A, x, =, b cleanly
        A_mat = AugMatrix(
            [["a₁₁", "a₁₂", "a₁₃"], ["a₂₁", "a₂₂", "a₂₃"], ["a₃₁", "a₃₂", "a₃₃"]],
            col_spacing=1.0,
            row_spacing=0.75,
            font_size=28,
            show_divider=False,
        )
        for r in range(3):
            for c in range(3):
                A_mat.cell(r, c).set_color(TEAL)

        x_mat = AugMatrix(
            [["x"], ["y"], ["z"]],
            col_spacing=0.8,
            row_spacing=0.75,
            font_size=28,
            show_divider=False,
        )
        for r in range(3):
            x_mat.cell(r, 0).set_color(GOLD)

        eq_sign = mono("=", size=40, color=TEXT_PRIMARY, weight=BOLD)

        b_mat = AugMatrix(
            [["b₁"], ["b₂"], ["b₃"]],
            col_spacing=0.8,
            row_spacing=0.75,
            font_size=28,
            show_divider=False,
        )
        for r in range(3):
            b_mat.cell(r, 0).set_color(CORAL)

        axb_group = VGroup(A_mat, x_mat, eq_sign, b_mat).arrange(RIGHT, buff=0.45)
        axb_group.shift(UP * 0.55)

        lbl_A = txt("A : Coefficients", size=22, color=TEAL, weight=BOLD).next_to(A_mat, DOWN, buff=0.5)
        lbl_x = txt("x : Unknowns", size=22, color=GOLD, weight=BOLD).next_to(x_mat, DOWN, buff=0.5)
        lbl_b = txt("b : Constants", size=22, color=CORAL, weight=BOLD).next_to(b_mat, DOWN, buff=0.5)

        # Equation title above
        eq_title = mono("A x = b", size=38, color=TEXT_PRIMARY, weight=BOLD).shift(UP * 2.55)
        eq_title[0].set_color(TEAL)
        eq_title[1].set_color(GOLD)
        eq_title[3].set_color(CORAL)

        play_sync(FadeIn(eq_title), FadeIn(axb_group), run_time=1.8)
        sync(16.6)
        play_sync(FadeIn(lbl_A, shift=UP * 0.15), run_time=1.0)
        sync(18.6)
        play_sync(FadeIn(lbl_x, shift=UP * 0.15), run_time=1.0)
        sync(20.4)
        play_sync(FadeIn(lbl_b, shift=UP * 0.15), run_time=1.0)
        sync(21.6)
        play_sync(FadeOut(VGroup(eq_title, axb_group, lbl_A, lbl_x, lbl_b)), run_time=0.6)

        # --- 21.80 - 32.64s: Augmented Matrix [A | b] ---
        aug_title = txt("Augmented Matrix  [ A | b ]", size=32, color=TEXT_PRIMARY, weight=BOLD)
        aug_title.shift(UP * 2.45)

        aug = AugMatrix(
            [["a₁₁", "a₁₂", "a₁₃", "b₁"], ["a₂₁", "a₂₂", "a₂₃", "b₂"], ["a₃₁", "a₃₂", "a₃₃", "b₃"]],
            col_spacing=1.15,
            row_spacing=0.82,
            font_size=30,
            show_divider=True,
            col_headers=["x", "y", "z", "b"],
        ).shift(DOWN * 0.15)
        for r in range(3):
            aug.cell(r, 3).set_color(CORAL)

        row_box = aug.make_row_highlight(0, color=TEAL)
        row_note = txt("Each row = 1 equation", size=22, color=TEAL, weight=BOLD)
        row_note.next_to(aug, LEFT, buff=0.65).shift(UP * 0.6)

        col_note = txt("Each column = x, y, z, b", size=22, color=GOLD, weight=BOLD)
        col_note.next_to(aug, RIGHT, buff=0.65).shift(UP * 0.6)

        play_sync(Write(aug_title), FadeIn(aug), run_time=1.5)
        sync(26.2)
        play_sync(Create(row_box), FadeIn(row_note), run_time=1.2)
        sync(28.8)
        play_sync(FadeIn(col_note), Indicate(aug.headers, color=GOLD), run_time=1.3)
        sync(32.8)
        play_sync(FadeOut(VGroup(aug_title, aug, row_box, row_note, col_note)), run_time=0.6)

        # --- 32.64 - 43.68s: Row-Echelon Form Staircase ---
        ref_title = txt("Target: Row-Echelon Form", size=34, color=GOLD, weight=BOLD)
        ref_title.shift(UP * 2.55)

        ref_mat = AugMatrix(
            [["★", "*", "*", "*"], ["0", "★", "*", "*"], ["0", "0", "★", "*"]],
            col_spacing=1.15,
            row_spacing=0.85,
            font_size=34,
            show_divider=True,
        ).shift(DOWN * 0.1)

        # Color pivots gold, zeros cyan
        pivots = [(0, 0), (1, 1), (2, 2)]
        zeros = [(1, 0), (2, 0), (2, 1)]
        for r, c in pivots:
            ref_mat.cell(r, c).set_color(GOLD)
        for r, c in zeros:
            ref_mat.cell(r, c).set_color(CYAN)

        # Staircase path separating pivots from zeros below
        c00 = ref_mat.cell_pos(0, 0)
        c11 = ref_mat.cell_pos(1, 1)
        c22 = ref_mat.cell_pos(2, 2)
        dx, dy = 0.56, 0.42
        stair = VMobject(color=GOLD, stroke_width=3.5)
        stair.set_points_as_corners([
            [c00[0] - dx, c00[1] - dy, 0],
            [c11[0] - dx, c00[1] - dy, 0],
            [c11[0] - dx, c11[1] - dy, 0],
            [c22[0] - dx, c11[1] - dy, 0],
            [c22[0] - dx, c22[1] - dy, 0],
            [c22[0] + dx * 2.8, c22[1] - dy, 0],
        ])

        piv_lbl = txt("★  Non-zero Pivots", size=22, color=GOLD, weight=BOLD).next_to(ref_mat, RIGHT, buff=0.7).shift(UP * 0.6)
        zero_lbl = txt("0  Zeros below pivots", size=22, color=CYAN, weight=BOLD).next_to(ref_mat, RIGHT, buff=0.7).shift(DOWN * 0.5)

        play_sync(Write(ref_title), FadeIn(ref_mat), run_time=1.4)
        sync(36.2)
        play_sync(Create(stair), run_time=1.4)
        sync(38.8)
        play_sync(FadeIn(piv_lbl), run_time=1.0)
        sync(40.9)
        play_sync(FadeIn(zero_lbl), run_time=1.0)
        sync(43.40)
        play_sync(FadeOut(VGroup(header, ref_title, ref_mat, stair, piv_lbl, zero_lbl)), run_time=0.6)

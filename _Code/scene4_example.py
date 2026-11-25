"""Scene 4: Worked Example (audio 113.76 - 218.72s, duration = 104.96s).
Step-by-step Gaussian elimination on a 3x3 system with pivot highlights,
row replacement, row swap, row scaling, Row-Echelon Form staircase, and back-substitution.
"""

from manim import *
from theme import *


class Scene4Example(Scene):
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

        header = make_section_header("04", "WORKED EXAMPLE")
        play_sync(FadeIn(header), run_time=0.4)

        # --- 0.40 - 12.24s: Show the 3x3 System ---
        sys_card = make_card(5.4, 3.3, stroke_color=TEAL, stroke_width=2.2)
        sys_card.move_to(LEFT * 3.3 + UP * 0.2)
        sys_lbl = txt("Linear System", size=22, color=TEAL, weight=BOLD)
        sys_lbl.move_to(sys_card.get_top() + DOWN * 0.42)

        eq1 = mono(" x +  y + z =  4", size=26, color=TEXT_PRIMARY, weight=BOLD)
        eq2 = mono("2x -  y + z =  8", size=26, color=TEXT_PRIMARY, weight=BOLD)
        eq3 = mono(" x + 2y - z = -3", size=26, color=TEXT_PRIMARY, weight=BOLD)
        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        eqs.move_to(sys_card.get_center() + DOWN * 0.2)

        play_sync(FadeIn(sys_card), FadeIn(sys_lbl), run_time=0.9)
        sync(1.8)
        play_sync(Write(eq1), run_time=2.2)
        sync(5.1)
        play_sync(Write(eq2), run_time=2.2)
        sync(8.7)
        play_sync(Write(eq3), run_time=2.2)
        sync(12.4)

        # --- 12.40 - 16.50s: Convert to Augmented Matrix ---
        mat = AugMatrix(
            [["1", "1", "1", "4"], ["2", "-1", "1", "8"], ["1", "2", "-1", "-3"]],
            col_spacing=1.05,
            row_spacing=0.82,
            font_size=32,
            show_divider=True,
            col_headers=["x", "y", "z", "b"],
        ).move_to(LEFT * 3.1 + UP * 0.1)

        # Move system up-left as compact reference, reveal matrix
        sys_compact = VGroup(sys_card, sys_lbl, eqs)
        play_sync(
            sys_compact.animate.scale(0.58).to_corner(DL, buff=0.4),
            FadeIn(mat, shift=RIGHT * 0.3),
            run_time=1.6,
        )

        # Right-side scratchpad / operation panel
        panel = make_card(6.55, 4.75, stroke_color=CARD_BORDER, stroke_width=2.0)
        panel.move_to(RIGHT * 3.15 + UP * 0.1)
        panel_title = txt("Row Operations", size=22, color=TEXT_MUTED, weight=BOLD)
        panel_title.move_to(panel.get_top() + DOWN * 0.42)
        play_sync(FadeIn(panel), FadeIn(panel_title), run_time=0.7)
        sync(16.6)

        # --- 16.60 - 22.80s: Highlight Pivot 1 & targets below ---
        piv1_box = mat.make_cell_box(0, 0, color=GOLD)
        mat.cell(0, 0).set_color(GOLD)
        t2_box = mat.make_cell_box(1, 0, color=CORAL)
        t3_box = mat.make_cell_box(2, 0, color=CORAL)
        piv1_badge = make_badge("Pivot 1 = 1  (R1, C1)", accent=GOLD, font_size=20)
        piv1_badge.move_to(panel.get_top() + DOWN * 1.15)

        play_sync(Create(piv1_box), FadeIn(piv1_badge), run_time=1.2)
        sync(20.6)
        play_sync(Create(t2_box), Create(t3_box), run_time=1.0)
        sync(23.0)

        # Helper to update a matrix row's text smoothly
        def update_row(r: int, new_vals: list[str], colors: list[str] | None = None):
            anims = []
            for c, val in enumerate(new_vals):
                old = mat.cell(r, c)
                col = colors[c] if colors else TEXT_PRIMARY
                new_t = mono(val, size=32, color=col, weight=BOLD).move_to(old.get_center())
                anims.append(Transform(old, new_t))
            return anims

        # --- 23.00 - 32.10s: R2 -> R2 - 2*R1 ("gives" at 28.2s) ---
        op_r2 = make_badge("R₂ → R₂ − 2·R₁", accent=CYAN, font_size=22)
        op_r2.move_to(panel.get_center() + UP * 0.35)
        calc_r2 = VGroup(
            mono("  [ 2, -1,  1 |  8 ]", size=20, color=TEXT_MUTED),
            mono("− [ 2,  2,  2 |  8 ]", size=20, color=TEXT_MUTED),
            Line(LEFT * 1.8, RIGHT * 1.8, color=TEXT_MUTED, stroke_width=1.5),
            mono("= [ 0, -3, -1 |  0 ]", size=21, color=CYAN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(panel.get_center() + DOWN * 0.95)

        play_sync(FadeOut(t2_box), FadeIn(op_r2), run_time=0.9)
        play_sync(FadeIn(calc_r2, shift=UP * 0.1), run_time=1.2)
        sync(28.0)
        play_sync(*update_row(1, ["0", "-3", "-1", "0"], [CYAN, TEXT_PRIMARY, TEXT_PRIMARY, TEXT_PRIMARY]), run_time=1.6)
        sync(32.1)

        # --- 32.10 - 39.60s: R3 -> R3 - R1 ("gives" at 35.5s) ---
        op_r3 = make_badge("R₃ → R₃ − R₁", accent=CYAN, font_size=22)
        op_r3.move_to(op_r2.get_center())
        calc_r3 = VGroup(
            mono("  [ 1,  2, -1 | -3 ]", size=20, color=TEXT_MUTED),
            mono("− [ 1,  1,  1 |  4 ]", size=20, color=TEXT_MUTED),
            Line(LEFT * 1.8, RIGHT * 1.8, color=TEXT_MUTED, stroke_width=1.5),
            mono("= [ 0,  1, -2 | -7 ]", size=21, color=CYAN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(calc_r2.get_center())

        play_sync(FadeOut(t3_box), ReplacementTransform(op_r2, op_r3), ReplacementTransform(calc_r2, calc_r3), run_time=1.2)
        sync(35.3)
        play_sync(*update_row(2, ["0", "1", "-2", "-7"], [CYAN, TEXT_PRIMARY, TEXT_PRIMARY, TEXT_PRIMARY]), run_time=1.6)
        sync(39.7)

        # --- 39.70 - 45.40s: Column 1 clean, move to Column 2 ---
        col1_done = make_badge("Column 1 Clean ✓", accent=GREEN, font_size=20)
        col1_done.move_to(piv1_badge.get_center())
        play_sync(
            FadeOut(piv1_box),
            ReplacementTransform(piv1_badge, col1_done),
            FadeOut(op_r3),
            FadeOut(calc_r3),
            run_time=1.0,
        )
        sync(42.3)
        c2_r2_box = mat.make_cell_box(1, 1, color=CORAL)
        c2_r3_box = mat.make_cell_box(2, 1, color=GOLD)
        play_sync(Create(c2_r2_box), Create(c2_r3_box), run_time=1.0)
        sync(48.8)

        # --- 48.80 - 52.40s: Row Swap R2 <-> R3 ---
        swap_badge = make_badge("Swap:  R₂ ↔ R₃  (avoid fractions!)", accent=PURPLE, font_size=20)
        swap_badge.move_to(panel.get_center() + UP * 0.2)
        play_sync(ReplacementTransform(col1_done, swap_badge), run_time=0.7)

        # Animate physical row swap + update internal row references
        y1 = mat.row(1).get_center()[1]
        y2 = mat.row(2).get_center()[1]
        dy = y1 - y2
        play_sync(
            FadeOut(c2_r2_box),
            FadeOut(c2_r3_box),
            mat.row(1).animate.shift(DOWN * dy),
            mat.row(2).animate.shift(UP * dy),
            run_time=1.5,
        )
        mat.cells[1], mat.cells[2] = mat.cells[2], mat.cells[1]
        mat.row_groups[1], mat.row_groups[2] = mat.row_groups[2], mat.row_groups[1]
        sync(52.4)

        # --- 52.40 - 64.80s: Highlight Pivot 2 & R3 <- R3 + 3*R2 ("gives" at 60.8s) ---
        piv2_box = mat.make_cell_box(1, 1, color=GOLD)
        mat.cell(1, 1).set_color(GOLD)
        piv2_badge = make_badge("Pivot 2 = 1  (R2, C2)", accent=GOLD, font_size=20)
        piv2_badge.move_to(panel.get_top() + DOWN * 1.15)

        op_r3_2 = make_badge("R₃ → R₃ + 3·R₂", accent=CYAN, font_size=22)
        op_r3_2.move_to(panel.get_center() + UP * 0.35)
        calc_r3_2 = VGroup(
            mono("  [ 0, -3, -1 |   0 ]", size=20, color=TEXT_MUTED),
            mono("+ [ 0,  3, -6 | -21 ]", size=20, color=TEXT_MUTED),
            Line(LEFT * 1.8, RIGHT * 1.8, color=TEXT_MUTED, stroke_width=1.5),
            mono("= [ 0,  0, -7 | -21 ]", size=21, color=CYAN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(panel.get_center() + DOWN * 0.95)

        play_sync(Create(piv2_box), ReplacementTransform(swap_badge, piv2_badge), run_time=1.2)
        sync(56.2)
        play_sync(FadeIn(op_r3_2), FadeIn(calc_r3_2, shift=UP * 0.1), run_time=1.4)
        sync(60.6)
        play_sync(*update_row(2, ["0", "0", "-7", "-21"], [CYAN, CYAN, TEXT_PRIMARY, TEXT_PRIMARY]), run_time=1.8)
        sync(64.8)

        # --- 64.80 - 72.70s: Scale R3 -> (-1/7) * R3 ("gives" at 69.0s) ---
        scale_badge = make_badge("Scale:  R₃ → (−1/7)·R₃", accent=PURPLE, font_size=22)
        scale_badge.move_to(op_r3_2.get_center())
        play_sync(
            FadeOut(piv2_box),
            FadeOut(calc_r3_2),
            ReplacementTransform(op_r3_2, scale_badge),
            run_time=1.0,
        )
        sync(68.8)
        play_sync(*update_row(2, ["0", "0", "1", "3"], [CYAN, CYAN, GOLD, TEXT_PRIMARY]), run_time=1.6)
        piv3_box = mat.make_cell_box(2, 2, color=GOLD)
        play_sync(Create(piv3_box), run_time=0.8)
        sync(72.8)

        # --- 72.80 - 77.20s: Row-Echelon Form Staircase ---
        c00 = mat.cell_pos(0, 0)
        c11 = mat.cell_pos(1, 1)
        c22 = mat.cell_pos(2, 2)
        dx, sx = 0.52, 0.40
        stair = VMobject(color=GOLD, stroke_width=3.5)
        stair.set_points_as_corners([
            [c00[0] - dx, c00[1] - sx, 0],
            [c11[0] - dx, c00[1] - sx, 0],
            [c11[0] - dx, c11[1] - sx, 0],
            [c22[0] - dx, c11[1] - sx, 0],
            [c22[0] - dx, c22[1] - sx, 0],
            [c22[0] + dx * 2.6, c22[1] - sx, 0],
        ])
        ref_badge = make_badge("Row-Echelon Form ✓", accent=GOLD, font_size=22)
        ref_badge.move_to(piv2_badge.get_center())

        play_sync(
            FadeOut(piv3_box),
            FadeOut(scale_badge),
            ReplacementTransform(piv2_badge, ref_badge),
            Create(stair),
            run_time=1.8,
        )
        sync(77.2)

        # --- 77.20 - 104.50s: Back-Substitution ---
        bs_title = txt("Back-Substitution", size=22, color=TEAL, weight=BOLD)
        bs_title.move_to(panel_title.get_center())
        play_sync(ReplacementTransform(panel_title, bs_title), FadeOut(ref_badge), run_time=0.8)

        step_z = mono("R₃:  z = 3", size=21, color=GOLD, weight=BOLD)
        step_y = mono("R₂:  y − 2(3) = −7  ⇒  y = −1", size=19, color=CYAN, weight=BOLD)
        step_x = mono("R₁:  x + (−1) + 3 = 4  ⇒  x = 2", size=18, color=TEAL, weight=BOLD)
        steps = VGroup(step_z, step_y, step_x).arrange(DOWN, aligned_edge=LEFT, buff=0.40)
        steps.move_to(panel.get_center() + UP * 0.45)

        sol_box = make_badge("Solution:  (x, y, z) = (2, −1, 3)", accent=GOLD, font_size=19, padding_x=0.40, padding_y=0.22)
        sol_box.move_to(panel.get_bottom() + UP * 0.72)

        sync(78.8)
        play_sync(Write(step_z), run_time=1.8)
        sync(81.6)
        play_sync(Write(step_y), run_time=4.2)
        sync(89.8)
        play_sync(Write(step_x), run_time=4.2)
        sync(99.3)
        play_sync(FadeIn(sol_box, scale=0.92), run_time=1.4)
        sync(103.80)
        play_sync(FadeOut(VGroup(header, sys_compact, mat, stair, panel, bs_title, steps, sol_box)), run_time=0.7)

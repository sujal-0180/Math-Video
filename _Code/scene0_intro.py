"""Scene 0: Opening Frame (0:00 - 0:05, duration = 5.0s).
Displays Title, Concept, Student Name (P. Sujal), and URN (E25B070607)
as required by the M3 Internal Assessment rubric.
"""

from manim import *
from theme import *


class OpeningFrame(Scene):
    def construct(self):
        # Subtle decorative background grid
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": CARD_BORDER,
                "stroke_width": 1.0,
                "stroke_opacity": 0.35,
            },
            axis_config={"stroke_opacity": 0.0},
        )
        self.add(grid)

        # Top assessment badge
        badge = make_badge(
            "LINEAR ALGEBRA & CALCULUS (M3)  •  INTERNAL ASSESSMENT",
            accent=CYAN,
            font_size=18,
            padding_x=0.55,
            padding_y=0.24,
        )
        badge.shift(UP * 2.15)

        # Main Title
        title = txt("Gaussian Elimination", size=64, color=TEXT_PRIMARY, weight=BOLD)
        title.shift(UP * 0.75)

        underline = Line(LEFT * 3.6, RIGHT * 3.6, color=GOLD, stroke_width=4.5)
        underline.next_to(title, DOWN, buff=0.22)

        subtitle = txt(
            "Visualizing Row Operations, Pivots & Row-Echelon Form",
            size=26,
            color=TEXT_MUTED,
        )
        subtitle.next_to(underline, DOWN, buff=0.35)

        # Student Details Card
        card = make_card(7.2, 1.15, stroke_color=GOLD, stroke_width=2.0)
        card.shift(DOWN * 1.95)
        name_lbl = txt("P. Sujal", size=30, color=TEXT_PRIMARY, weight=BOLD)
        sep = txt("|", size=28, color=GOLD)
        urn_lbl = mono("URN: E25B070607", size=26, color=GOLD, weight=BOLD)
        details = VGroup(name_lbl, sep, urn_lbl).arrange(RIGHT, buff=0.4)
        details.move_to(card.get_center())

        # Animate (total = 5.0s)
        self.play(
            FadeIn(badge, shift=DOWN * 0.2),
            Write(title),
            run_time=1.1,
        )
        self.play(
            Create(underline),
            FadeIn(subtitle, shift=UP * 0.15),
            FadeIn(card, shift=UP * 0.2),
            FadeIn(details, shift=UP * 0.2),
            run_time=1.2,
        )
        self.wait(1.9)
        self.play(
            FadeOut(VGroup(badge, title, underline, subtitle, card, details)),
            run_time=0.8,
        )

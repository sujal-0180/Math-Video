"""Shared visual theme, typography, and matrix/UI helpers for the
Gaussian Elimination M3 animation video.
"""

from manim import *

# --- Color Palette (3Blue1Brown-inspired dark theme) ---
BG_COLOR = "#0B0F19"
CARD_BG = "#141B2D"
CARD_BORDER = "#263354"

TEXT_PRIMARY = "#F1F5F9"
TEXT_MUTED = "#94A3B8"

GOLD = "#F5C542"       # Pivots, key highlights, final solution
CYAN = "#4CC9F0"       # Zeros below pivots, secondary highlights
TEAL = "#2EC4B6"       # Matrix A / Plane 1 / Success checks
CORAL = "#FF6B6B"      # Vector b / Plane 2 / Targets to eliminate
PURPLE = "#A78BFA"     # Plane 3 / Row operations
GREEN = "#34D399"      # Verification checkmarks

FONT_MAIN = "Helvetica Neue"
FONT_MONO = "Menlo"

# Set Manim global background
config.background_color = BG_COLOR


def txt(
    content: str,
    size: int = 28,
    color: str = TEXT_PRIMARY,
    weight: str = NORMAL,
    font: str = FONT_MAIN,
) -> Text:
    """Create a cleanly styled Text object."""
    return Text(content, font=font, font_size=size, color=color, weight=weight)


def mono(
    content: str,
    size: int = 26,
    color: str = TEXT_PRIMARY,
    weight: str = NORMAL,
) -> Text:
    """Create a monospace Text object for matrices and equations."""
    return Text(content, font=FONT_MONO, font_size=size, color=color, weight=weight)


def make_card(
    width: float,
    height: float,
    fill_color: str = CARD_BG,
    stroke_color: str = CARD_BORDER,
    corner_radius: float = 0.18,
    stroke_width: float = 2.0,
) -> RoundedRectangle:
    """Create a rounded UI card."""
    return RoundedRectangle(
        width=width,
        height=height,
        corner_radius=corner_radius,
        fill_color=fill_color,
        fill_opacity=0.92,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
    )


def make_badge(
    label: str,
    accent: str = GOLD,
    font_size: int = 24,
    padding_x: float = 0.45,
    padding_y: float = 0.22,
) -> VGroup:
    """Create a pill badge for row operation labels or section tags."""
    t = mono(label, size=font_size, color=accent, weight=BOLD)
    box = RoundedRectangle(
        width=t.width + padding_x,
        height=t.height + padding_y,
        corner_radius=0.14,
        fill_color=CARD_BG,
        fill_opacity=0.95,
        stroke_color=accent,
        stroke_width=2.0,
    )
    t.move_to(box.get_center())
    return VGroup(box, t)


def make_section_header(scene_num: str, title: str) -> VGroup:
    """Top-left subtle header bar for continuity across scenes."""
    tag = txt(scene_num, size=18, color=GOLD, weight=BOLD)
    sep = txt("•", size=18, color=TEXT_MUTED)
    ttl = txt(title, size=20, color=TEXT_MUTED, weight=MEDIUM)
    row = VGroup(tag, sep, ttl).arrange(RIGHT, buff=0.18)
    row.to_corner(UL, buff=0.45)
    return row


class AugMatrix(VGroup):
    """Custom 3x4 Augmented Matrix [A | b] with individually addressable cells,
    brackets, vertical divider, and optional column/row labels.
    """

    def __init__(
        self,
        rows: list[list[str]],
        col_spacing: float = 1.05,
        row_spacing: float = 0.78,
        font_size: int = 34,
        show_divider: bool = True,
        col_headers: list[str] | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.col_spacing = col_spacing
        self.row_spacing = row_spacing
        self.font_size = font_size

        self.cells: list[list[Text]] = []
        self.row_groups: list[VGroup] = []

        # Create cell grid centered at origin
        total_w = (self.num_cols - 1) * col_spacing + (0.35 if show_divider else 0.0)
        total_h = (self.num_rows - 1) * row_spacing

        for r in range(self.num_rows):
            row_cells = []
            for c in range(self.num_cols):
                extra_x = 0.35 if (show_divider and c == self.num_cols - 1) else 0.0
                x = -total_w / 2 + c * col_spacing + extra_x
                y = total_h / 2 - r * row_spacing
                cell = mono(rows[r][c], size=font_size, color=TEXT_PRIMARY, weight=BOLD)
                cell.move_to([x, y, 0])
                row_cells.append(cell)
            self.cells.append(row_cells)
            rg = VGroup(*row_cells)
            self.row_groups.append(rg)

        self.entries_group = VGroup(*self.row_groups)
        self.add(self.entries_group)

        # Brackets
        pad_x = 0.48
        pad_y = 0.36
        left_x = -total_w / 2 - pad_x
        right_x = total_w / 2 + pad_x
        top_y = total_h / 2 + pad_y
        bot_y = -total_h / 2 - pad_y
        tick = 0.18

        left_bracket = VMobject(color=TEXT_PRIMARY, stroke_width=3.2)
        left_bracket.set_points_as_corners([
            [left_x + tick, top_y, 0],
            [left_x, top_y, 0],
            [left_x, bot_y, 0],
            [left_x + tick, bot_y, 0],
        ])

        right_bracket = VMobject(color=TEXT_PRIMARY, stroke_width=3.2)
        right_bracket.set_points_as_corners([
            [right_x - tick, top_y, 0],
            [right_x, top_y, 0],
            [right_x, bot_y, 0],
            [right_x - tick, bot_y, 0],
        ])
        self.brackets = VGroup(left_bracket, right_bracket)
        self.add(self.brackets)

        # Vertical augmented divider line
        self.divider = None
        if show_divider:
            div_x = -total_w / 2 + (self.num_cols - 1.5) * col_spacing + 0.175
            self.divider = DashedLine(
                [div_x, top_y - 0.06, 0],
                [div_x, bot_y + 0.06, 0],
                color=TEXT_MUTED,
                stroke_width=2.2,
                dash_length=0.1,
            )
            self.add(self.divider)

        # Optional column headers (e.g. ["x", "y", "z", "b"])
        self.headers = None
        if col_headers:
            hdrs = []
            for c, h in enumerate(col_headers):
                extra_x = 0.35 if (show_divider and c == self.num_cols - 1) else 0.0
                x = -total_w / 2 + c * col_spacing + extra_x
                hdr_color = CORAL if (show_divider and c == self.num_cols - 1) else TEAL
                ht = mono(h, size=22, color=hdr_color, weight=BOLD)
                ht.move_to([x, top_y + 0.32, 0])
                hdrs.append(ht)
            self.headers = VGroup(*hdrs)
            self.add(self.headers)

    def cell(self, r: int, c: int) -> Text:
        return self.cells[r][c]

    def row(self, r: int) -> VGroup:
        return self.row_groups[r]

    def cell_pos(self, r: int, c: int) -> np.ndarray:
        return self.cells[r][c].get_center()

    def make_cell_box(self, r: int, c: int, color: str = GOLD) -> RoundedRectangle:
        return RoundedRectangle(
            width=0.68,
            height=0.58,
            corner_radius=0.1,
            stroke_color=color,
            stroke_width=2.8,
            fill_color=color,
            fill_opacity=0.14,
        ).move_to(self.cells[r][c].get_center())

    def make_row_highlight(self, r: int, color: str = TEAL) -> RoundedRectangle:
        rg = self.row_groups[r]
        return RoundedRectangle(
            width=rg.width + 0.4,
            height=0.62,
            corner_radius=0.12,
            stroke_color=color,
            stroke_width=2.2,
            fill_color=color,
            fill_opacity=0.10,
        ).move_to(rg.get_center())

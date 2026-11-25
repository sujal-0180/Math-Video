"""Generates the required 6-Scene Storyboard PDF (Storyboard_GaussianElimination.pdf)
matching the M3 Internal Assessment rubric.
"""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent.parent
OUT_PDF = ROOT / "Storyboard_GaussianElimination.pdf"


def build_pdf():
    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=landscape(A4),
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCustom", parent=styles["Heading1"], fontSize=18, textColor=colors.HexColor("#0F172A"), spaceAfter=4
    )
    sub_style = ParagraphStyle(
        "SubCustom", parent=styles["Normal"], fontSize=10, textColor=colors.HexColor("#475569"), spaceAfter=8
    )
    obj_style = ParagraphStyle(
        "ObjCustom",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#1E293B"),
        backColor=colors.HexColor("#EFF6FF"),
        borderPadding=8,
        spaceAfter=12,
    )
    cell_style = ParagraphStyle("Cell", parent=styles["Normal"], fontSize=8.8, leading=11.5)
    hdr_style = ParagraphStyle(
        "Hdr", parent=styles["Normal"], fontSize=9.5, leading=12, textColor=colors.white, fontName="Helvetica-Bold"
    )

    story = [
        Paragraph("M3 Internal Assessment • 6-Scene Animation Storyboard", title_style),
        Paragraph(
            "<b>Topic:</b> Gaussian Elimination (3×3 Linear System) &nbsp;&nbsp;|&nbsp;&nbsp; "
            "<b>Student:</b> P. Sujal &nbsp;&nbsp;|&nbsp;&nbsp; <b>URN:</b> E25B070607 &nbsp;&nbsp;|&nbsp;&nbsp; "
            "<b>Duration:</b> 5:13 (1080p 16:9)",
            sub_style,
        ),
        Paragraph(
            "<b>Learning Objective:</b> By the end of this video, the viewer will be able to understand "
            "<i>why</i> Gaussian elimination preserves solutions geometrically and <i>how</i> to solve a 3×3 "
            "system step-by-step using elementary row operations, Row-Echelon Form, and back-substitution.",
            obj_style,
        ),
    ]

    rows = [
        [
            Paragraph("Scene & Time", hdr_style),
            Paragraph("Purpose", hdr_style),
            Paragraph("Visual Plan (Manim)", hdr_style),
            Paragraph("Narration & Math Plan", hdr_style),
        ],
        [
            Paragraph("<b>0. Opening Frame</b><br/>0:00 – 0:05", cell_style),
            Paragraph("Identify project, topic, and student details.", cell_style),
            Paragraph("Dark slate grid, M3 badge, gold-underlined title, P. Sujal | URN E25B070607 card.", cell_style),
            Paragraph("Silent 5s intro card before narration begins.", cell_style),
        ],
        [
            Paragraph("<b>1. Hook / Context</b><br/>0:05 – 0:33", cell_style),
            Paragraph("Spark curiosity and motivate why linear systems matter.", cell_style),
            Paragraph("Cards for Bridge Forces, Neural Nets, Supply Chains converging to Ax=b; 2D line crossing vs. 10,000×10,000 scale.", cell_style),
            Paragraph("Contrast 2-variable visual crossing with large systems; introduce Gaussian Elimination.", cell_style),
        ],
        [
            Paragraph("<b>2. Concept Intro</b><br/>0:33 – 1:17", cell_style),
            Paragraph("Define notation and target Row-Echelon Form.", cell_style),
            Paragraph("Color-coded A x = b; transition to [A | b] augmented matrix; gold staircase over pivots & cyan zeros.", cell_style),
            Paragraph("State learning objective, define A, x, b, augmented matrix rows/columns, and pivots.", cell_style),
        ],
        [
            Paragraph("<b>3. Visual Intuition</b><br/>1:17 – 1:59", cell_style),
            Paragraph("Build 3D geometric understanding before algebra.", cell_style),
            Paragraph("3D ThreeDAxes with 3 intersecting planes & glowing gold point; animate plane hinging around shared line.", cell_style),
            Paragraph("Explain 3 equations as 3 planes; show why Swap, Scale, and Row Replacement never move the intersection.", cell_style),
        ],
        [
            Paragraph("<b>4. Worked Example</b><br/>1:59 – 3:44", cell_style),
            Paragraph("Demonstrate every intermediate step clearly.", cell_style),
            Paragraph("3×3 system → [A|b], gold pivot boxes, scratchpad arithmetic, physical R2↔R3 swap, staircase, back-sub.", cell_style),
            Paragraph("Solve x+y+z=4, 2x−y+z=8, x+2y−z=−3 step-by-step to unique solution (2, −1, 3).", cell_style),
        ],
        [
            Paragraph("<b>5. Interpretation</b><br/>3:44 – 4:31", cell_style),
            Paragraph("Connect Row-Echelon Form back to 3D geometry & verify.", cell_style),
            Paragraph("Morph tilted planes into simplified REF planes highlighting flat z=3; verification card with green checkmarks.", cell_style),
            Paragraph("Show intersection (2, −1, 3) is unchanged; peel planes backwards; verify 4, 8, −3.", cell_style),
        ],
        [
            Paragraph("<b>6. Summary & Credits</b><br/>4:31 – 5:13", cell_style),
            Paragraph("Reinforce 3 takeaways and cite tools/AI disclosure.", cell_style),
            Paragraph("3 animated takeaway cards → Closing Frame with P. Sujal, URN, references, Manim/FFmpeg & AI disclosure.", cell_style),
            Paragraph("Recap augmented matrix, pivot staircase, and back-substitution; direct viewers to GitHub repo.", cell_style),
        ],
    ]

    table = Table(rows, colWidths=[1.35 * inch, 1.75 * inch, 3.45 * inch, 3.35 * inch], repeatRows=1)
    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
            ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ])
    )
    story.append(table)
    doc.build(story)
    print(f"Generated storyboard PDF: {OUT_PDF}")


if __name__ == "__main__":
    build_pdf()

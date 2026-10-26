import os
import zipfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_box_dieline_image():
    """Generates a high-precision, professional flat dieline for a 3D lipstick box."""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    fig.patch.set_facecolor('#F5F3EF')
    ax.set_facecolor('#F5F3EF')
    
    c_bg = '#1E3A2B'       # Deep Botanical Emerald Green
    c_gold = '#D4A373'     # Warm Rose Gold / Sand
    c_cream = '#FAF6F0'    # Off-white / Cream
    c_rose = '#C86D7D'     # Shade color (Velvet Terracotta/Rose)
    c_dieline = '#888888'  # Dieline border color
    
    w = 1.8
    h = 5.5
    glue_w = 0.5
    flap_h = 1.8
    
    x_glue = 0.5
    x_panel1 = x_glue + glue_w          # Left Side (Story)
    x_panel2 = x_panel1 + w             # Front Panel (Main Brand)
    x_panel3 = x_panel2 + w             # Right Side (Ingredients & Icons)
    x_panel4 = x_panel3 + w             # Back Panel (Directions & Barcode)
    
    y_body = 2.2
    
    # Glue Tab
    rect_glue = patches.Rectangle((x_glue, y_body), glue_w, h, linewidth=1, edgecolor=c_dieline, facecolor='#E2DFD8', linestyle='--')
    ax.add_patch(rect_glue)
    ax.text(x_glue + glue_w/2, y_body + h/2, 'GLUE TAB', rotation=90, ha='center', va='center', fontsize=8, color='#777777', fontweight='bold')
    
    # Panels
    rect1 = patches.Rectangle((x_panel1, y_body), w, h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    rect2 = patches.Rectangle((x_panel2, y_body), w, h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    rect3 = patches.Rectangle((x_panel3, y_body), w, h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    rect4 = patches.Rectangle((x_panel4, y_body), w, h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    ax.add_patch(rect1); ax.add_patch(rect2); ax.add_patch(rect3); ax.add_patch(rect4)
    
    # Caps & Flaps
    rect_top_cap = patches.Rectangle((x_panel2, y_body + h), w, flap_h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    rect_bot_cap = patches.Rectangle((x_panel2, y_body - flap_h), w, flap_h, linewidth=1.5, edgecolor=c_dieline, facecolor=c_bg)
    ax.add_patch(rect_top_cap); ax.add_patch(rect_bot_cap)
    
    rect_dust1 = patches.Rectangle((x_panel1, y_body + h), w, 0.8, linewidth=1, edgecolor=c_dieline, facecolor='#E2DFD8', linestyle='--')
    rect_dust2 = patches.Rectangle((x_panel3, y_body + h), w, 0.8, linewidth=1, edgecolor=c_dieline, facecolor='#E2DFD8', linestyle='--')
    rect_dust3 = patches.Rectangle((x_panel1, y_body - 0.8), w, 0.8, linewidth=1, edgecolor=c_dieline, facecolor='#E2DFD8', linestyle='--')
    rect_dust4 = patches.Rectangle((x_panel3, y_body - 0.8), w, 0.8, linewidth=1, edgecolor=c_dieline, facecolor='#E2DFD8', linestyle='--')
    ax.add_patch(rect_dust1); ax.add_patch(rect_dust2); ax.add_patch(rect_dust3); ax.add_patch(rect_dust4)
    
    # FRONT PANEL GRAPHICS (Panel 2)
    cx2 = x_panel2 + w/2
    border_front = patches.Rectangle((x_panel2 + 0.12, y_body + 0.15), w - 0.24, h - 0.3, linewidth=1, edgecolor=c_gold, facecolor='none')
    ax.add_patch(border_front)
    
    ax.text(cx2, y_body + 4.7, 'VERDANT', ha='center', va='center', fontsize=16, fontweight='bold', color=c_gold, family='serif')
    ax.text(cx2, y_body + 4.4, 'FLORA', ha='center', va='center', fontsize=14, fontweight='bold', color=c_cream, family='serif')
    ax.text(cx2, y_body + 4.15, '──── * ────', ha='center', va='center', fontsize=8, color=c_gold)
    
    ax.text(cx2, y_body + 3.6, 'HERBAL VELVET', ha='center', va='center', fontsize=11, fontweight='bold', color=c_cream)
    ax.text(cx2, y_body + 3.3, 'LIPSTICK', ha='center', va='center', fontsize=13, fontweight='bold', color=c_gold)
    
    swatch = patches.Circle((cx2, y_body + 2.3), radius=0.45, facecolor=c_rose, edgecolor=c_gold, linewidth=1.5)
    ax.add_patch(swatch)
    ax.text(cx2, y_body + 2.3, '04', ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')
    
    ax.text(cx2, y_body + 1.5, 'TERRACOTTA ROSE', ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_cream)
    ax.text(cx2, y_body + 1.2, 'Infused with Organic Neem,\nRosehip & Vitamin E', ha='center', va='center', fontsize=7, color='#CBD5E1', style='italic')
    ax.text(cx2, y_body + 0.6, '100% NATURAL • VEGAN', ha='center', va='center', fontsize=7.5, fontweight='bold', color=c_gold)
    ax.text(cx2, y_body + 0.35, 'Net Wt. 4.2g / 0.15 oz.', ha='center', va='center', fontsize=6.5, color=c_cream)

    # LEFT PANEL (Panel 1: Brand Story)
    cx1 = x_panel1 + w/2
    ax.text(cx1, y_body + 4.8, 'OUR PROMISE', ha='center', va='center', fontsize=10, fontweight='bold', color=c_gold)
    story_text = (
        "Verdant Flora blends\n"
        "ancient botanical\n"
        "wisdom with modern\n"
        "clean beauty.\n\n"
        "Handcrafted with\n"
        "cold-pressed oils\n"
        "and pure mineral\n"
        "pigments for intense\n"
        "moisture and long-\n"
        "lasting velvet color.\n\n"
        "• 0% Parabens\n"
        "• 0% Synthetic Dyes\n"
        "• 0% Lead & Toxins\n\n"
        "Pure Nature on\n"
        "Your Lips."
    )
    ax.text(cx1, y_body + 2.6, story_text, ha='center', va='center', fontsize=6.5, color=c_cream, multialignment='center')

    # RIGHT PANEL (Panel 3: Ingredients & Icons)
    cx3 = x_panel3 + w/2
    ax.text(cx3, y_body + 4.8, 'KEY INGREDIENTS', ha='center', va='center', fontsize=10, fontweight='bold', color=c_gold)
    ing_text = (
        "• Organic Neem Oil\n"
        "Anti-bacterial & Healing\n\n"
        "• Cold-Pressed Rosehip\n"
        "Deep Hydration\n\n"
        "• Vitamin E & Shea\n"
        "Velvet Smooth Finish\n\n"
        "• Mineral Pigments\n"
        "Rich Botanical Tint\n\n"
        "─────────────────\n"
        "Dermatologically Tested\n"
        "Suitable for Sensitive Lips"
    )
    ax.text(cx3, y_body + 2.7, ing_text, ha='center', va='center', fontsize=6.5, color=c_cream, multialignment='center')

    # BACK PANEL (Panel 4: Directions & Barcode)
    cx4 = x_panel4 + w/2
    ax.text(cx4, y_body + 4.8, 'HOW TO USE', ha='center', va='center', fontsize=10, fontweight='bold', color=c_gold)
    ax.text(cx4, y_body + 4.2, "Glide smoothly over clean lips.\nReapply as needed for richer\ncolor and deep nourishing moisture.", ha='center', va='center', fontsize=6.5, color=c_cream, multialignment='center')
    
    ax.text(cx4, y_body + 3.3, 'FULL INGREDIENTS', ha='center', va='center', fontsize=8, fontweight='bold', color=c_gold)
    ax.text(cx4, y_body + 2.6, "Ricinus Communis Seed Oil*,\nSimmondsia Chinensis Seed Oil*,\nMelia Azadirachta (Neem) Oil*,\nRosa Canina (Rosehip) Oil*,\nButyrospermum Parkii Butter*,\nCandelilla Wax, Tocopherol (Vit E),\n[+/- Mineral Iron Oxides CI 77491].\n*Certified Organic Ingredients.", ha='center', va='center', fontsize=5.5, color='#CBD5E1', multialignment='center')

    # Barcode
    rect_bc = patches.Rectangle((cx4 - 0.6, y_body + 0.6), 1.2, 0.7, facecolor='#FFFFFF', edgecolor=c_gold)
    ax.add_patch(rect_bc)
    for bx in [cx4 - 0.5, cx4 - 0.45, cx4 - 0.38, cx4 - 0.3, cx4 - 0.22, cx4 - 0.15, cx4 - 0.05, cx4 + 0.05, cx4 + 0.15, cx4 + 0.25, cx4 + 0.35, cx4 + 0.45]:
        ax.plot([bx, bx], [y_body + 0.75, y_body + 1.15], color='#000000', linewidth=1.2)
    ax.text(cx4, y_body + 0.65, '8 901234 567890', ha='center', va='center', fontsize=5, color='#000000', fontweight='bold')
    
    ax.text(cx4, y_body + 0.3, 'Mfd. by: Verdant Organics Pvt Ltd\nMade in India | Batch: VO2026-04', ha='center', va='center', fontsize=5.5, color=c_cream)

    # TOP FLAP DESIGN
    ax.text(cx2, y_body + h + 1.1, 'VERDANT FLORA', ha='center', va='center', fontsize=9, fontweight='bold', color=c_gold)
    top_swatch = patches.Circle((cx2, y_body + h + 0.55), radius=0.3, facecolor=c_rose, edgecolor=c_gold, linewidth=1)
    ax.add_patch(top_swatch)
    ax.text(cx2, y_body + h + 0.55, '04', ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')
    ax.text(cx2, y_body + h + 0.15, 'TERRACOTTA ROSE', ha='center', va='center', fontsize=6, fontweight='bold', color=c_cream)

    # BOTTOM FLAP DESIGN
    ax.text(cx2, y_body - 0.6, '100% RECYCLABLE BOX', ha='center', va='center', fontsize=7, fontweight='bold', color=c_gold)
    ax.text(cx2, y_body - 1.1, 'CRUELTY FREE • VEGAN', ha='center', va='center', fontsize=6.5, color=c_cream)

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    plt.title('HERBAL LIPSTICK PACKAGING FLAT DIELINE & BOX LAYOUT', fontsize=13, fontweight='bold', color='#1E3A2B', pad=15)
    
    output_path = '/workspace/scratch/packaging_preview_box.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#F5F3EF')
    plt.close()
    return output_path


def create_lipstick_tube_image():
    """Generates a high-res mockup render of the inner lipstick tube packaging."""
    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    fig.patch.set_facecolor('#FAF6F0')
    ax.set_facecolor('#FAF6F0')
    
    c_bg = '#1E3A2B'       # Deep Botanical Emerald Green
    c_gold = '#D4A373'     # Warm Rose Gold / Sand
    c_cream = '#FAF6F0'    # Off-white / Cream
    c_rose = '#C86D7D'     # Shade color
    
    # Base Cylinder
    base_rect = patches.Rectangle((2.5, 1), 2.2, 2.8, facecolor=c_bg, edgecolor=c_gold, linewidth=1.5)
    ax.add_patch(base_rect)
    
    # Middle Metallic Gold Ring
    ring_rect = patches.Rectangle((2.5, 3.8), 2.2, 0.6, facecolor=c_gold, edgecolor='#B45309', linewidth=1)
    ax.add_patch(ring_rect)
    ax.text(3.6, 4.1, 'VERDANT FLORA', ha='center', va='center', fontsize=8, fontweight='bold', color='#1E3A2B')
    
    # Upper Inner Metallic Sheath
    sheath_rect = patches.Rectangle((2.7, 4.4), 1.8, 1.2, facecolor='#E5E7EB', edgecolor='#9CA3AF', linewidth=1)
    ax.add_patch(sheath_rect)
    
    # Curved Bullet Lipstick Tip (Terracotta Rose)
    bullet_path = Path(
        [(2.8, 5.6), (2.8, 6.8), (3.6, 7.6), (4.4, 6.8), (4.4, 5.6), (2.8, 5.6)],
        [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    )
    bullet_patch = patches.PathPatch(bullet_path, facecolor=c_rose, edgecolor='#9F1239', linewidth=1.5)
    ax.add_patch(bullet_patch)
    
    # Cap (Placed beside the tube)
    cap_rect = patches.Rectangle((6.0, 1.0), 2.0, 4.5, facecolor=c_bg, edgecolor=c_gold, linewidth=1.5)
    ax.add_patch(cap_rect)
    
    # Cap Gold Emblem & Typography
    ax.text(7.0, 4.8, 'VERDANT', ha='center', va='center', fontsize=11, fontweight='bold', color=c_gold, family='serif')
    ax.text(7.0, 4.45, 'FLORA', ha='center', va='center', fontsize=10, fontweight='bold', color=c_cream, family='serif')
    ax.text(7.0, 4.2, '─── * ───', ha='center', va='center', fontsize=7, color=c_gold)
    ax.text(7.0, 3.2, 'HERBAL VELVET\nLIPSTICK', ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_cream, multialignment='center')
    
    # Cap Bottom Swatch Dot
    cap_dot = patches.Circle((7.0, 1.8), radius=0.3, facecolor=c_rose, edgecolor=c_gold, linewidth=1.2)
    ax.add_patch(cap_dot)
    ax.text(7.0, 1.8, '04', ha='center', va='center', fontsize=7, fontweight='bold', color='#FFFFFF')
    
    # Label Annotations
    ax.annotate('Satin Gold Foil Band', xy=(2.5, 4.1), xytext=(0.5, 4.5),
                arrowprops=dict(facecolor='#1E3A2B', shrink=0.08, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color='#1E3A2B')
                
    ax.annotate('Organic Velvet Bullet Tip', xy=(3.8, 7.2), xytext=(4.8, 7.7),
                arrowprops=dict(facecolor='#1E3A2B', shrink=0.08, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color='#1E3A2B')
                
    ax.annotate('Matte Emerald Cap & Swatch', xy=(6.0, 2.5), xytext=(0.5, 1.8),
                arrowprops=dict(facecolor='#1E3A2B', shrink=0.08, width=1, headwidth=5),
                fontsize=8.5, fontweight='bold', color='#1E3A2B')

    ax.set_xlim(0, 9.5)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    
    plt.title('INNER LIPSTICK TUBE & CAP PACKAGING MOCKUP', fontsize=12, fontweight='bold', color='#1E3A2B', pad=15)
    
    output_path = '/workspace/scratch/packaging_preview_tube.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#FAF6F0')
    plt.close()
    return output_path

box_img_path = create_box_dieline_image()
tube_img_path = create_lipstick_tube_image()

# ----------------------------------------------------------------------
# 2. GENERATE COMPLETE PRESENTATION PDF DOCUMENT (REPORTLAB)
# ----------------------------------------------------------------------

pdf_path = '/workspace/scratch/herbal_lipstick_packaging_design.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(LETTER),
    leftMargin=0.5*inch, rightMargin=0.5*inch,
    topMargin=0.5*inch, bottomMargin=0.5*inch
)

styles = getSampleStyleSheet()

COLORS = {
    'primary': HexColor('#1E3A2B'),
    'accent': HexColor('#D4A373'),
    'bg_light': HexColor('#FAF6F0'),
    'text': HexColor('#262626'),
    'white': HexColor('#FFFFFF')
}

title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    textColor=COLORS['primary'],
    leading=26,
    alignment=1,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    fontName='Helvetica',
    fontSize=11,
    textColor=COLORS['accent'],
    leading=14,
    alignment=1,
    spaceAfter=15
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    fontName='Helvetica',
    fontSize=9.5,
    textColor=COLORS['text'],
    leading=13.5,
    spaceAfter=6
)

story = []

story.append(Paragraph("VERDANT FLORA — HERBAL VELVET LIPSTICK", title_style))
story.append(Paragraph("Product Packaging Design & Production Dieline | Brand Identity & Layout Specification", subtitle_style))

story.append(RLImage(box_img_path, width=9.5*inch, height=5.2*inch))

story.append(PageBreak())

story.append(Paragraph("PACKAGING SPECIFICATIONS & BRAND IDENTITY", title_style))
story.append(Paragraph("Visual Consistency, Materials, Typography & Target Audience Analysis", subtitle_style))

col1_content = [
    RLImage(tube_img_path, width=4.5*inch, height=4.2*inch)
]

col2_text = """
<b>1. Brand Identity & Target Audience</b><br/>
• <b>Target Market:</b> Eco-conscious beauty enthusiasts, lovers of clean/herbal cosmetics, ages 18–45.<br/>
• <b>Positioning:</b> Luxury organic botanical beauty. Combines natural neem & rosehip efficacy with rich velvet pigmentation.<br/><br/>

<b>2. Packaging Architecture & Materials</b><br/>
• <b>Outer Carton:</b> 350 GSM FSC-Certified 100% Recycled Kraft Board with Soft-Touch Matte Laminate and Gold Foil Stamping.<br/>
• <b>Inner Lipstick Tube:</b> Slim-line Aluminium casing in Deep Emerald Green with Satin Gold Collar.<br/>
• <b>Dieline Format:</b> Reverse Tuck End (RTE) Folding Carton (Dimensions: 25mm x 25mm x 85mm).<br/><br/>

<b>3. Color Palette & Typography</b><br/>
• <b>Deep Emerald (#1E3A2B):</b> Symbolizes botanical purity, organic strength, and eco-luxury.<br/>
• <b>Warm Sand Gold (#D4A373):</b> Premium touch for foil accents and logo lettering.<br/>
• <b>Terracotta Rose (#C86D7D):</b> High-contrast shade indicator swatch.<br/>
• <b>Typography:</b> Playfair/Serif header for heritage luxury + Clean Helvetica for legibility of INCI ingredients.
"""

col2_content = [Paragraph(col2_text, body_style)]

spec_table = Table([[col1_content, col2_content]], colWidths=[4.7*inch, 5.1*inch])
spec_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))

story.append(spec_table)

doc.build(story)

# Publish to /workspace/out/
out_zip = '/workspace/out/herbal_lipstick_packaging_package.zip'
out_pdf = '/workspace/out/herbal_lipstick_packaging_design.pdf'
out_img_box = '/workspace/out/packaging_preview_box.png'
out_img_tube = '/workspace/out/packaging_preview_tube.png'

import shutil
shutil.copy(pdf_path, out_pdf)
shutil.copy(box_img_path, out_img_box)
shutil.copy(tube_img_path, out_img_tube)

readme_path = '/workspace/scratch/README.md'
with open(readme_path, 'w') as f:
    f.write("# Product Packaging Design — Herbal Velvet Lipstick\n\nBrand: Verdant Flora")

with zipfile.ZipFile(out_zip, 'w') as zipf:
    zipf.write(pdf_path, arcname='herbal_lipstick_packaging_design.pdf')
    zipf.write(box_img_path, arcname='packaging_preview_box.png')
    zipf.write(tube_img_path, arcname='packaging_preview_tube.png')
    zipf.write('/workspace/scratch/generate_packaging.py', arcname='generate_packaging.py')
    zipf.write(readme_path, arcname='README.md')

print("All packaging artifacts published successfully.")

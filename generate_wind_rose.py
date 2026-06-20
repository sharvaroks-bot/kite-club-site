#!/usr/bin/env python3
"""
Wind rose v2 — neon glow, modern style
Output: assets/wind-rose-koh-phangan.png
"""
import requests, math, io
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

OUTPUT = '/Users/mac/Downloads/KITE-CLUB-v3/assets/wind-rose-koh-phangan.png'
PINK   = '#ff007a'
PURPLE = '#9b3fff'
CYAN   = '#00d4ff'
PINK_R = (255, 0, 122)
PURP_R = (155, 63, 255)
CYAN_R = (0, 212, 255)

# ── 1. Satellite tiles ────────────────────────────────────────────────────
def tile_xy(lat, lon, z):
    n = 2 ** z
    x = int((lon + 180) / 360 * n)
    r = math.radians(lat)
    y = int((1 - math.log(math.tan(r) + 1/math.cos(r)) / math.pi) / 2 * n)
    return x, y

def fetch_tile(z, x, y):
    url = (f'https://server.arcgisonline.com/ArcGIS/rest/services/'
           f'World_Imagery/MapServer/tile/{z}/{y}/{x}')
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
    r.raise_for_status()
    return Image.open(io.BytesIO(r.content)).convert('RGB')

LAT, LON, ZOOM = 9.77, 100.03, 10  # geographic centre of Koh Phangan island
cx, cy = tile_xy(LAT, LON, ZOOM)

# Compute sub-pixel position of island within tile grid
n = 2 ** ZOOM
cx_f = (LON + 180) / 360 * n
r = math.radians(LAT)
cy_f = (1 - math.log(math.tan(r) + 1/math.cos(r)) / math.pi) / 2 * n

TS = 256
N = 4  # 4×4 tile grid → 1024×1024
start_x, start_y = cx - N//2, cy - N//2
big = Image.new('RGB', (TS * N, TS * N))
for di in range(N):
    for dj in range(N):
        t = fetch_tile(ZOOM, start_x + di, start_y + dj)
        big.paste(t, (di * TS, dj * TS))
        print(f'  tile ({di},{dj}) ✓')

# Crop 768×768 centered on island coords
OUT = 768
px = int((cx_f - start_x) * TS)
py = int((cy_f - start_y) * TS)
x1 = max(0, px - OUT//2)
y1 = max(0, py - OUT//2)
mosaic = big.crop((x1, y1, x1 + OUT, y1 + OUT))
W, H = mosaic.size
print(f'  island pixel in grid: ({px},{py}), crop: ({x1},{y1})')

# Bright base
arr = np.array(mosaic, dtype=np.float32)
arr = arr * 1.05  # slightly boost overall
arr = np.clip(arr, 0, 255)
base = Image.fromarray(arr.astype(np.uint8))

# Gradient overlay: dark at edges, slight at center
grad = np.zeros((H, W, 4), dtype=np.uint8)
ys, xs = np.ogrid[:H, :W]
dist = np.sqrt((xs - W/2)**2 + (ys - H/2)**2)
max_d = np.sqrt((W/2)**2 + (H/2)**2)
alpha = np.clip((dist / max_d) * 180, 0, 180).astype(np.uint8)
grad[:,:,3] = alpha
vignette = Image.fromarray(grad, 'RGBA')
base_rgba = base.convert('RGBA')
base_rgba = Image.alpha_composite(base_rgba, vignette)

# ── 2. matplotlib wind rose ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(W/100, H/100), dpi=100)
fig.patch.set_alpha(0)
ax.set_facecolor('none')
ax.set_xlim(0, W); ax.set_ylim(H, 0)
ax.axis('off')

CX, CY = W / 2, H / 2
R = 215

# Outer dashed ring (dotted compass)
theta = np.linspace(0, 2*np.pi, 360)
for i in range(0, 360, 6):
    a = math.radians(i)
    size = 3 if i % 90 == 0 else (1.5 if i % 45 == 0 else 1)
    ax.plot(CX + R * math.cos(a), CY + R * math.sin(a), 'o',
            color='white', markersize=size, alpha=0.4)

# Inner ring
for r, a in [(R*0.55, 0.12), (R*0.25, 0.07)]:
    c = plt.Circle((CX, CY), r, fill=False, color='white', alpha=a, lw=1,
                   linestyle='--')
    ax.add_patch(c)

# Cardinal labels with glow
for lbl, deg in [('N', 270), ('E', 0), ('S', 90), ('W', 180)]:
    rad = math.radians(deg)
    tx = CX + (R + 30) * math.cos(rad)
    ty = CY + (R + 30) * math.sin(rad)
    ax.text(tx, ty, lbl, ha='center', va='center', color='white',
            fontsize=14, fontweight='bold', alpha=0.7,
            fontfamily='DejaVu Sans Mono',
            path_effects=[pe.withStroke(linewidth=4, foreground='black')])

# Long tick lines for cardinals
for deg in [0, 90, 180, 270]:
    rad = math.radians(deg)
    ax.plot([CX + (R-18)*math.cos(rad), CX + (R+2)*math.cos(rad)],
            [CY + (R-18)*math.sin(rad), CY + (R+2)*math.sin(rad)],
            color='white', alpha=0.3, lw=1.5)

# ── Wind arrows with neon glow ────────────────────────────────────────────
def neon_arrow(screen_deg, hex_color, rgb, name, season):
    rad = math.radians(screen_deg)
    # Arrow from edge → center
    x1, y1 = CX + R * math.cos(rad),    CY + R * math.sin(rad)
    x2, y2 = CX + 38 * math.cos(rad),   CY + 38 * math.sin(rad)

    # Glow layers (wide → narrow)
    for lw, alpha in [(22, 0.06), (14, 0.10), (8, 0.18), (4, 0.6), (2.5, 1.0)]:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=hex_color,
                                   lw=lw, mutation_scale=28, alpha=alpha))

    # Label pill background
    lx = CX + (R + 78) * math.cos(rad)
    ly = CY + (R + 78) * math.sin(rad)

    # Glow on text
    ax.text(lx, ly - 1, name, ha='center', va='center',
            color=hex_color, fontsize=12, fontweight='bold',
            path_effects=[pe.withStroke(linewidth=6, foreground=(*[c/255 for c in rgb], 0.3))])
    ax.text(lx, ly + 17, season, ha='center', va='center',
            color='white', fontsize=9, alpha=0.85,
            path_effects=[pe.withStroke(linewidth=3, foreground='black')])

neon_arrow(135, PINK,   PINK_R,  'SE  WIND', 'FEB – APR')
neon_arrow(225, PURPLE, PURP_R,  'SW  WIND', 'JUN – SEP')
neon_arrow(315, CYAN,   CYAN_R,  'NE  WIND', 'DEC – JAN')

# Center — glowing dot
for size, alpha in [(18, 0.08), (12, 0.15), (7, 0.35), (4, 1.0)]:
    ax.plot(CX, CY, 'o', color=PINK, markersize=size, alpha=alpha, zorder=10)
ax.plot(CX, CY, 'o', color='white', markersize=2.5, zorder=11)

# Bottom label
ax.text(CX, H - 32, 'K O H   P H A N G A N   ·   W I N D   S E A S O N S',
        ha='center', va='center', color='white', alpha=0.4,
        fontsize=8, fontfamily='DejaVu Sans Mono')

# ── 3. Composite ──────────────────────────────────────────────────────────
buf = io.BytesIO()
fig.savefig(buf, format='png', dpi=100,
            bbox_inches='tight', pad_inches=0, transparent=True)
buf.seek(0); plt.close(fig)

overlay = Image.open(buf).convert('RGBA').resize((W, H), Image.LANCZOS)
result  = Image.alpha_composite(base_rgba, overlay)

# Subtle color grade: slight pink/purple tint in corners
grade = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grade)
for i in range(80):
    a = int(30 * ((80 - i) / 80) ** 2)
    gd.rectangle([i, i, W-1-i, H-1-i], outline=(155, 63, 255, a))
result = Image.alpha_composite(result, grade)

result.convert('RGB').save(OUTPUT, quality=94)
print(f'\n✓ Saved → {OUTPUT}')

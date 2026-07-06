import os
import sys
import math
import pygame

pygame.init()

# ---------- Window setup ----------
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我がシステム - WAGA SYSTEM")
clock = pygame.time.Clock()

# ---------- Colors (old phosphor-terminal palette) ----------
BG_COLOR = (10, 10, 14)
FG_COLOR = (0, 255, 140)      # green phosphor
DIM_COLOR = (0, 120, 70)
SELECT_COLOR = (255, 210, 0)  # amber highlight
SCANLINE_COLOR = (0, 0, 0, 40)


def find_japanese_font(size):
    """
    Try a list of common system fonts that support Japanese glyphs.
    Falls back to pygame's default font (romaji-only) if none are found.
    """
    candidates = [
        "msgothic", "msmincho",          # Windows
        "hiraginosans", "hiraginokakugothicpro",  # macOS
        "notosanscjkjp", "notosansjp",   # Linux (Noto)
        "ipagothic", "ipamincho",        # Linux (IPA fonts)
        "takaogothic",
    ]
    available = pygame.font.get_fonts()
    for name in candidates:
        if name in available:
            return pygame.font.SysFont(name, size)

    # Try loading by common file paths as a last resort
    file_candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJKjp-Regular.otf",
        "C:/Windows/Fonts/msgothic.ttc",
        "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    ]
    for path in file_candidates:
        if os.path.exists(path):
            return pygame.font.Font(path, size)

    return None  # signal: no CJK-capable font found


title_font = find_japanese_font(40)
menu_font = find_japanese_font(26)
small_font = find_japanese_font(18)

JAPANESE_SUPPORTED = title_font is not None

# Fallback fonts (always romaji, guaranteed to work)
fallback_title = pygame.font.SysFont("couriernew", 40, bold=True)
fallback_menu = pygame.font.SysFont("couriernew", 26)
fallback_small = pygame.font.SysFont("couriernew", 18)

if not JAPANESE_SUPPORTED:
    title_font, menu_font, small_font = fallback_title, fallback_menu, fallback_small


# ---------- Menu data ----------
MENU_ITEMS = [
    ("開始", "START"),
    ("設定", "SETTINGS"),
    ("情報", "ABOUT"),
    ("終了", "EXIT"),
]

selected = 0
running = True
frame = 0


def draw_text(surface, font, text_jp, text_en, pos, color, center=False):
    """Draw Japanese text if supported, otherwise fall back to English only."""
    label = f"{text_jp}  {text_en}" if JAPANESE_SUPPORTED else text_en
    rendered = font.render(label, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surface.blit(rendered, rect)


def draw_scanlines(surface):
    """Old CRT scanline overlay."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for y in range(0, HEIGHT, 3):
        pygame.draw.line(overlay, SCANLINE_COLOR, (0, y), (WIDTH, y))
    surface.blit(overlay, (0, 0))


def draw_border(surface):
    pygame.draw.rect(surface, DIM_COLOR, (10, 10, WIDTH - 20, HEIGHT - 20), 2)


def run_action(index):
    """Placeholder actions for each menu item."""
    global running
    if index == 0:
        print("開始 -> Starting...")
    elif index == 1:
        print("設定 -> Opening settings...")
    elif index == 2:
        print("情報 -> This is a retro pygame menu demo.")
    elif index == 3:
        print("終了 -> Goodbye.")
        running = False


while running:
    dt = clock.tick(60)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                selected = (selected - 1) % len(MENU_ITEMS)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                selected = (selected + 1) % len(MENU_ITEMS)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                run_action(selected)
            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BG_COLOR)
    draw_border(screen)

    # Flicker effect on title (subtle brightness pulse)
    pulse = 200 + int(55 * math.sin(frame * 0.05))
    title_color = (0, pulse, min(255, pulse - 40))
    draw_text(screen, title_font, "我がシステム", "WAGA SYSTEM",
              (WIDTH // 2, 90), title_color, center=True)

    draw_text(screen, small_font, "", "- MAIN MENU -", (WIDTH // 2, 150), DIM_COLOR, center=True)

    # Menu items
    start_y = 220
    gap = 50
    for i, (jp, en) in enumerate(MENU_ITEMS):
        color = SELECT_COLOR if i == selected else FG_COLOR
        prefix = "> " if i == selected else "  "
        label_jp = prefix + jp
        rendered_label = f"{label_jp}  {en}" if JAPANESE_SUPPORTED else prefix + en
        rendered = menu_font.render(rendered_label, True, color)
        rect = rendered.get_rect(center=(WIDTH // 2, start_y + i * gap))
        screen.blit(rendered, rect)

    footer = "矢印キー: 移動 | Enter: 選択 | Esc: 終了" if JAPANESE_SUPPORTED \
        else "Arrows: Move | Enter: Select | Esc: Quit"
    footer_render = small_font.render(footer, True, DIM_COLOR)
    footer_rect = footer_render.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    screen.blit(footer_render, footer_rect)

    draw_scanlines(screen)
    pygame.display.flip()

pygame.quit()
sys.exit(0)
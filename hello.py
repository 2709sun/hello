import os
import sys
import pygame
import pygame_menu

# ─── 초기화 ─────────────────────────────────────────────────────────────
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DJ FIGHT!")
clock = pygame.time.Clock()

# ─── 폰트 경로 설정 ─────────────────────────────────────────────────────
# test.py 위치를 기준으로 assets/fonts 폴더를 찾도록 경로 생성
BASE_PATH    = os.path.dirname(os.path.abspath(__file__))
FONTS_FOLDER = os.path.join(BASE_PATH, 'assets', 'fonts')
FONT_REGULAR = os.path.join(FONTS_FOLDER, 'NanumBarunGothic.ttf')
FONT_BOLD    = os.path.join(FONTS_FOLDER, 'NanumBarunGothicBold.ttf')

# ─── 테마에 폰트 지정 ────────────────────────────────────────────────────
my_theme = pygame_menu.themes.THEME_DEFAULT.copy()
# 메뉴 상단 타이틀에 볼드체
my_theme.title_font  = FONT_BOLD
# 버튼 등 위젯에는 레귤러체
my_theme.widget_font = FONT_REGULAR

# ─── 메뉴 생성 ───────────────────────────────────────────────────────────
menu = pygame_menu.Menu(
    height=SCREEN_HEIGHT,
    width=SCREEN_WIDTH,
    title='DJ FIGHT!',
    theme=my_theme
)

# ─── 버튼 추가 ───────────────────────────────────────────────────────────
menu.add.button(
    '전투 시작',
    lambda: print('전투 시작!'),
    # 개별 위젯에서 크기를 바꾸고 싶으면 아래 옵션 추가 가능
    font_size=48
)
menu.add.button(
    '덱 편성',
    lambda: print('덱 편성!'),
    font_size=48
)

# ─── 메인 루프 ───────────────────────────────────────────────────────────
while True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    menu.update(events)
    menu.draw(screen)
    pygame.display.flip()
    clock.tick(60)
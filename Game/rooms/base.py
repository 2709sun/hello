import pygame
import os

TILE_W, TILE_H = 50, 50
ASSET_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "blocks")
)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, block_type):
        super().__init__()

        img_path = os.path.join(ASSET_DIR, f"{block_type}.png")
        full_img = pygame.image.load(img_path).convert_alpha()

        # 1) 잘라낼 영역 정의 (좌상단 TILE_W×TILE_H)
        crop_rect = pygame.Rect(0, 0, TILE_W, TILE_H)

        # 2) crop된 크기의 빈 Surface 준비 (투명도 포함)
        cropped = pygame.Surface((TILE_W, TILE_H), pygame.SRCALPHA)

        # 3) full_img 의 crop_rect 영역만 cropped 위에 그리기
        cropped.blit(full_img, (0, 0), area=crop_rect)

        # 4) 이 cropped 을 실제로 사용할 image 로 지정
        self.image = cropped #image가 Surface임.

        # 5) 위치·크기용 rect
        self.rect = self.image.get_rect(topleft=(x, y))

class Room:
    def __init__(self):
        self.xsize = 10
        self.ysize = 10
        self.blocks = pygame.sprite.Group()
        pass
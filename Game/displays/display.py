import pygame
import os

ASSET_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "backgrounds")
)

class Display:
    def __init__(self, x, y, player:pygame.sprite):
        self.screen = pygame.display.set_mode((x, y))
        self.width = x
        self.height = y
        self.player = player
        self.bg = 'bg1'

    def setsize(self, x, y):
        self.width = x*50
        self.height = y*50
        self.screen = pygame.display.set_mode((self.width, self.height))

    def setbg(self, type):
        self.bg = type
    
    def display(self, all_sprites: pygame.sprite.Group):
        # 임시
        self.zoom = 2

        # 카메라 기준점 계산
        camera_offset_x = self.player.rect.centerx - self.width // 2
        camera_offset_y = self.player.rect.centery - self.height // 2

        # 카메라 뷰(Rect형태)
        camera_view = pygame.Rect(camera_offset_x, camera_offset_y, self.width, self.height)

        #배경 이미지 불러오기
        img_path = os.path.join(ASSET_DIR, f"{self.bg}.png")
        full_img = pygame.image.load(img_path).convert_alpha()
        full_img = pygame.transform.scale(full_img, (int(full_img.get_width() * self.zoom), int(full_img.get_height() * self.zoom)))

        # 2) crop된 크기의 빈 Surface 준비 (투명도 포함)
        cropped = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # 3) full_img 의 crop_rect 영역만 cropped 위에 그리기
        cropped.blit(full_img, (0, 0), area=camera_view)

        # 4) cropped를 그려서 화면 지우기.
        self.screen.blit(cropped, (0, 0))

        # 가시 영역 내의 스프라이트만 그림
        for sprite in all_sprites:
            if camera_view.colliderect(sprite.rect):  # 카메라 시야 안에 있으면
                offset_rect = sprite.rect.move(-camera_offset_x, -camera_offset_y)
                self.screen.blit(sprite.image, offset_rect)

        pygame.display.flip()
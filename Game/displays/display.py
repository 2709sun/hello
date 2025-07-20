import pygame

class Display:
    def __init__(self, x, y, player:pygame.sprite):
        self.screen = pygame.display.set_mode((x, y))
        self.width = x
        self.height = y
        self.player = player

    def setsize(self, x, y):
        self.width = x*50
        self.height = y*50
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def display(self, all_sprites: pygame.sprite.Group):
        #화면 지우기
        self.screen.fill((30, 30, 30))

        # 카메라 기준점 계산
        camera_offset_x = self.player.rect.centerx - self.width // 2
        camera_offset_y = self.player.rect.centery - self.height // 2

        # 카메라 뷰(Rect형태)
        camera_view = pygame.Rect(camera_offset_x, camera_offset_y, self.width, self.height)

        # 가시 영역 내의 스프라이트만 그림
        for sprite in all_sprites:
            if camera_view.colliderect(sprite.rect):  # 카메라 시야 안에 있으면
                offset_rect = sprite.rect.move(-camera_offset_x, -camera_offset_y)
                self.screen.blit(sprite.image, offset_rect)

        pygame.display.flip()
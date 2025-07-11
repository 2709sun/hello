import pygame

# 설정값
GRAVITY      = 0.5
MAX_FALL     = 15
MOVE_SPEED   = 5
JUMP_SPEED   = -12

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((100, 200, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, r, g, b, platforms_group):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y)) #rect : x, y, w, h 들고있음.
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

        # 충돌 대상이 될 플랫폼 그룹
        self.platforms = platforms_group

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVE_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_SPEED
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL)

    def update(self):
        self.handle_input() #keydown 받았을 때만 호출하기(key_respond)
        self.apply_gravity()

        # 가로 이동 & 충돌
        self.rect.x += self.vel_x
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        for plat in hits:
            if self.vel_x > 0:
                self.rect.right = plat.rect.left
            elif self.vel_x < 0:
                self.rect.left  = plat.rect.right

        # 세로 이동 & 충돌
        self.rect.y += self.vel_y
        # 바닥에 붙어있는 상태 초기화
        self.on_ground = False
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        for plat in hits:
            if self.vel_y > 0:  # 떨어지는 중
                self.rect.bottom = plat.rect.top
                self.vel_y = 0
                self.on_ground = True
            elif self.vel_y < 0:  # 점프해서 부딪힐 때
                self.rect.top = plat.rect.bottom
                self.vel_y *= -1

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock  = pygame.time.Clock()

    # 플랫폼 그룹 생성
    platforms = pygame.sprite.Group()
    platforms.add(
        Platform(0, 550, 800, 50),
        Platform(200, 400, 200, 20),
    )

    # 플레이어와 전체 스프라이트 그룹
    player = Player(100, 100, platforms)
    all_sprites = pygame.sprite.Group(player, *platforms.sprites())

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        # 모든 스프라이트 업데이트
        all_sprites.update()

        # 그리기
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

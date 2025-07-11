import pygame

GRAVITY      = 0.5 #방에서 가져와서 구현할수도있음.
MAX_FALL     = 15

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, r, g, b, ms, js):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect(topleft=(x, y)) #rect : x, y, w, h 들고있음.
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.ms = ms
        self.js = js

    def update(self, xy):
        if xy=='x':
            self.rect.x += self.vel_x
        else:
            self.rect.y += self.vel_y

class Gravity_Object(Object):
    def update(self, xy):
        if xy=='y':
            self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL)
        super().update(xy)
import pygame

GRAVITY      = 0.5 #방에서 가져와서 구현할수도있음.
MAX_FALL     = 15

class Object:
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

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.ms
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.js
            self.on_ground = False
   
class GravityMixin:
    def apply_gravity(self):
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL)

class Gravity_Object(Object, GravityMixin):
    pass
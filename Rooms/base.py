import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((100, 200, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

class Room:
    def __init__(self):
        pass
import base
import pygame

class Test_Room(base.Room):
    def __init__(self):
        platforms = pygame.sprite.Group()
        platforms.add(
            base.Platform(0, 550, 800, 50),
            base.Platform(200, 400, 200, 20),
        )
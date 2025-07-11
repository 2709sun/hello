from Game.rooms.base import Room, Platform
import pygame

class Test_Room(Room):
    def __init__(self):
        platforms = pygame.sprite.Group()
        platforms.add(
            Platform(0, 550, 800, 50),
            Platform(200, 400, 200, 20),
        )
from Game.rooms.base import Room, Platform, Block
import pygame

class Test_Room(Room):
    def __init__(self):
        super().__init__()
        self.platforms.add(
            Platform(0, 550, 800, 50),
            Platform(200, 400, 200, 20),
        )
        self.blocks.add(
            Block(110, 110, 'grass')
        )
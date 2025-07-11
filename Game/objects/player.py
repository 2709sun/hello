from Game.objects.base import Gravity_Object
import pygame

class Player(Gravity_Object):
    def __init__(self, *args):
        super().__init__(*args)

    def handle_input(self):
            keys = pygame.key.get_pressed()
            self.vel_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.ms
            if keys[pygame.K_SPACE] and self.on_ground:
                self.vel_y = self.js
                self.on_ground = False
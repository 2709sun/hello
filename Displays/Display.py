import rooms
import objects
import pygame

class Display:
    def __init__(self, x, y):
        self.screen = pygame.display.set_mode((x, y))

    def display(self, all_sprites:pygame.sprite.Group):
        self.screen.fill((30, 30, 30))
        all_sprites.draw(self.screen)
        pygame.display.flip()
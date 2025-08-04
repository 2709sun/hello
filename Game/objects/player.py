from Game.objects.base import Gravity_Object, Animate
import pygame

class Player(Gravity_Object, Animate):
    def __init__(self, *args):
        Gravity_Object.__init__(self, *args)
        Animate.__init__(self, self.image, self.rect, "D:\\Personal\\Works\\MyProject\\hello\\Game\\assets\\animate\\player\\", 3, 1, 10)

    def handle_input(self):
            keys = pygame.key.get_pressed()
            self.vel_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.ms
            if keys[pygame.K_SPACE] and self.on_ground:
                self.vel_y = self.js
                self.on_ground = False

    def update(self, xy):
        Gravity_Object.update(self, xy)
        if xy == 'y':
            Animate.update(self) #인자로 조건문 전달 가능 : 조건이 만족되어야만 애니메니션 틱이 흐르게 조정 가능.
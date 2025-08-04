import pygame
import os

GRAVITY      = 1 #방에서 가져와서 구현할수도있음.
MAX_FALL     = 15

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, r, g, b, ms, js):
        super().__init__()
        self.image = pygame.Surface((w, h)) #image가 Surface임.
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

#일단 rect는 없앰
class Animate:
    def __init__(self, image:pygame.Surface, rect:pygame.Surface, path, image_amount:int, rect_amount:int, ticks:int):
        self.image = image
        self.current_img = image
        #self.rect = rect
        self.path = path #해당 폴더의 경로.
        self.image_c = image_amount
        #self.rect_c = rect_amount
        self.current_img = 0
        self.current_rect = 0
        self.ticks = ticks
        self.current_tick = 0
        #이미지 일단 미리 불러오기
        self.image_list = [ #이미지 : 숫자_img(0번부터)
            pygame.image.load(os.path.join(self.path, f"{i}_img.png")).convert_alpha() for i in range(self.image_c)
        ]
        #self.rect_list = [
            #pygame.image.load(os.path.join(self.path, f"{i}_rect.png")).convert_alpha() for i in range(self.image_c)
        #]
    def update(self, isbool:bool=True):
        if isbool:
            self.current_tick += 1
            if self.current_tick == self.ticks:
                self.current_img = (self.current_img+1)%self.image_c
                #self.current_rect = (self.current_rect+1)%self.rect_c
                #불러온 이미지 가져오기
                self.image = self.image_list[self.current_img]
                #self.rect = self.rect_list[self.current_rect]
                self.current_tick = 0
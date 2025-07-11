import Game.displays.display as d
import Game.objects.player as p
import Game.rooms.base as r
import pygame

class Engine():
    def __init__(self, start_room:r.Room, display:d.Display, player:p.Player):
        self.room = start_room
        self.display = display
        self.player = player
        self.running = True
        self.clock  = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group(*self.room.platforms, self.player)

    def move_room(self, room:r.Room):
        self.room = room

    def play(self):
        while self.running == True:
            self.update('x')
            self.collide('x')

            self.update('y')
            self.collide('y')

            self.cooldown()
            self.display.display(self.all_sprites)
            self.clock.tick(60)

    def update(self, xy):
        if xy=='x':
            self.player.rect.x += self.vel_x
        else:
            self.player.rect.y += self.vel_y

    def collide(self, xy):
        if xy=='x':
            hits = pygame.sprite.spritecollide(self, self.platforms, False)
            for plat in hits:
                if self.vel_x > 0:
                    self.rect.right = plat.rect.left
                elif self.vel_x < 0:
                    self.rect.left  = plat.rect.right
        else:
            self.on_ground = False
            hits = pygame.sprite.spritecollide(self, self.platforms, False)
            for plat in hits:
                if self.vel_y > 0:  # 떨어지는 중
                    self.rect.bottom = plat.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # 점프해서 부딪힐 때
                    self.rect.top = plat.rect.bottom
                    self.vel_y *= -1

    def cooldown(self):
        pass
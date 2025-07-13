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

        self.display.screen = pygame.display.set_mode((50*self.room.xsize, 50*self.room.ysize))
        self.all_sprites = pygame.sprite.Group(*self.room.blocks, self.player) #여기 나중에 투사체랑 적군(몬스터)도 추가될예정임.

    def move_room(self, room:r.Room):
        self.room = room
        self.display.screen = pygame.display.set_mode((50*self.room.xsize, 50*self.room.ysize))

    def play(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.player.handle_input()
            
            self.update('x')
            self.collide('x')

            self.update('y')
            self.collide('y')

            self.cooldown()
            self.display.display(self.all_sprites)
            self.clock.tick(60)
        pygame.quit()

    def update(self, xy): #object의 update를 호출하는 것으로 구현. 우선 움직이는 물체가 플레이어밖에 없으니까 플레이어만 업데이트.
        self.player.update(xy)

    def collide(self, xy):
        if xy=='x':
            hits = pygame.sprite.spritecollide(self.player, self.room.blocks, False)
            for block in hits:
                if self.player.vel_x > 0:
                    self.player.rect.right = block.rect.left
                    self.player.vel_x = 0
                elif self.player.vel_x < 0:
                    self.player.rect.left  = block.rect.right
                    self.player.vel_x = 0
        else:
            self.player.on_ground = False
            hits = pygame.sprite.spritecollide(self.player, self.room.blocks, False)
            for plat in hits:
                if self.player.vel_y > 0: 
                    self.player.rect.bottom = plat.rect.top
                    self.player.vel_y = 0
                    self.player.on_ground = True
                elif self.player.vel_y < 0:
                    self.player.rect.top = plat.rect.bottom
                    self.player.vel_y = 0

    def cooldown(self):
        pass
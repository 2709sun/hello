import Game.engines.engine as e
import Game.rooms.test_room as r
import Game.objects.player as p
import Game.displays.display as d
import pygame

pygame.init()
display = d.Display(800, 600)
player = p.Player(100, 100, 50, 50, 255, 100, 100, 5, -12)
room = r.Test_Room()

engine = e.Engine(room, display, player)

engine.play()
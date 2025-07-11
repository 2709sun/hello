import engines.engine as e
import rooms.test_room as r
import objects.player as p
import displays.display as d
import pygame

pygame.init()
player = p.Player(50, 50, 255, 100, 100, 100, 100)
room = r.Test_Room()
display = d.Display()
engine = e.Engine(room, display, player)

engine.play()
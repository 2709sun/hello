import Engines
import Objects
import Rooms

class Engine():
    def __init__(self, start_room:Rooms.Room):
        self.room = start_room

from rentomatic.domain.room import Room

class MemRepo:
    def __init__(self, rooms_dicts):
        self.rooms_dicts = rooms_dicts

    def list(self):
        rooms = [Room.from_dict(i) for i in self.rooms_dicts]
        return rooms


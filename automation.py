import json
import time

class Event:
    def __init__(self, name, date, _time, actions, repeat):
        self.name = name
        self.date = date
        self._time = _time
        self.actions = actions
        self.repeat = repeat


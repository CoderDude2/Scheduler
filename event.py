from datetime import date, time
import calendar

NEVER = 0
WEEKLY = 1
BIWEEKLY = 2
MONTHLY = 3
YEARLY = 4

class Event:
    def __init__(self, name="", _date=date(1970, 1, 1), _time=time(0,0), actions=[], repeat=[]):
        self.name = name
        self._date = _date
        self._time = _time
        self.actions = actions
        self.repeat = repeat
        self.ran = False

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def set_date(self, year, month, day):
        self._date = date(year, month, day)

    def set_time(self, hour, minute):
        self._time = time(hour, minute)

    def serialize(self):
        return [self.name, (self._date.year, self._date.month, self._date.day), (self._time.hour, self._time.minute), self.actions, self.repeat]

    def __str__(self):
        return f"{self.name} {self._date} {self._time} {self.actions} {self.repeat}"

def deserialize(event):
    return Event(event[0], date(event[1][0], event[1][1], event[1][2]), time(event[2][0], event[2][1]), event[3], event[4])
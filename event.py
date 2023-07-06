from datetime import date, time
import calendar
import action

NEVER = 0
WEEKLY = 1
BIWEEKLY = 2
MONTHLY = 3
YEARLY = 4

def get_repeat_text(repeat_option:int) -> str:
    if(repeat_option == 0):
        return "never"
    elif(repeat_option == 1):
        return "weekly"
    elif(repeat_option == 2):
        return "bi-weekly"
    elif(repeat_option == 3):
        return "monthly"
    elif(repeat_option == 4):
        return "yearly"

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
        return {'name':self.name, 
                'date':(self._date.year, self._date.month, self._date.day), 
                'time':(self._time.hour, self._time.minute), 
                'actions':[a.serialize() for a in self.actions], 
                'repeat':self.repeat}

    def __str__(self):
        return f"{self.name} {self._date} {self._time} {self.actions} {self.repeat}"

def deserialize(event):
    return Event(
        name=event["name"],
        _date=date(event["date"][0], event["date"][1], event["date"][2]),
        _time=time(event["time"][0], event["time"][1]),
        actions=[action.deserialize(a) for a in event["actions"]],
        repeat=event["repeat"]
    )
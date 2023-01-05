import event
import time
from enum import Enum

class RepeatOptions(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    NEVER = 7

def main():
    events = event.loadEvents()

    if(events != None):
        for e in events:
            if(event.checkDate(e) and event.checkTime(e) and e.repeat[0] == RepeatOptions.NEVER and e.ran == False):
                for action in e.actions:
                    action.Do()
                del(events[events.index(e)])
                event.saveEvents(events)
            elif(event.checkTime(e) and event.checkDay(e) and event.checkDateGTE(e) and e.ran == False):
                for action in e.actions:
                    action.Do()
                e.ran = True
                event.saveEvents(events)
            elif(event.checkTime(e) == False and event.checkDay(e) == True and e.ran == True):
                e.ran = False
                event.saveEvents(events)
        time.sleep(1)


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            exit()

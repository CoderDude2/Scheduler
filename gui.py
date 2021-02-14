import json
import time
import event

eventList = {
    "events":[]
}

def newEvent(name, date, _time, actions, repeat):
    _event = event.Event(name, date, _time, actions, repeat)
    eventList['events'].append(_event)

def main():
    eventList['events'] = event.loadEvents()
    print(event.checkDate(eventList['events'][0]))

try:
    main()
except KeyboardInterrupt:
    exit()
import event
import time

def main():
    events = event.loadEvents()

    if(events != None):
        for e in events:
            if(event.checkDate(e) and event.checkTime(e) and e.repeat[0] == 7 and e.ran == False):
                for a in e.actions:
                    a.Do()
                del(events[events.index(e)])
                event.saveEvents(events)
            elif(event.checkTime(e) and event.checkDay(e) and event.checkDateGTE(e) and e.ran == False):
                for a in e.actions:
                    a.Do()
                e.ran = True
                event.saveEvents(events)
            elif(event.checkTime(e) == False and event.checkDay(e) == True and e.ran == True):
                e.ran = False
                event.saveEvents(events)
        time.sleep(1)


while True:
    try:
        main()
    except KeyboardInterrupt:
        exit()

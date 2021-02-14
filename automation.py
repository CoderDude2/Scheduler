import json
import time
import event

def main():
    events = event.loadEvents()

    for e in events:
        if(event.checkTime(e) and event.checkDate(e) and e.isDone == False):
            print("Time reached")
            e.isDone = True
            event.saveEvents(events)
    
    time.sleep(1)

while True:
    try:
        main()
    except KeyboardInterrupt:
        exit()
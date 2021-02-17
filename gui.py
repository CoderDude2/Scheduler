import json
import time
import event
import os

eventList = {
    "events":[]
}

def clear():
    os.system("clear")

def displayEvents():
    for e in eventList['events']:
        print(e.name,e.date,e._time)

def addActions():
    actions = []
    while True:
        clear()
        print("1) Open Link")
        print("2) Open File")
        print("3) Open Folder")
        print()
        print("4) Notify")
        print()
        print("5) Done")
        inp = str(input("Enter Number: "))

        if(inp == "1"):
            link = str(input("Enter Link: "))
            actions.append(f'Open+Link+{link}')
        elif(inp == "2"):
            path = str(input("Enter Path to file: "))
            actions.append(f'Open+File+{path}')
        elif(inp == "3"):
            path = str(input("Enter Path to folder"))
            actions.append(f'Open+Folder+{path}')
        elif(inp == "4"):
            title = str(input("Enter Title: "))
            message = str(input("Enter Message: "))
            actions.append(f'Notify+{title}+{message}')
        elif(inp == "5"):
            return actions

def repeatOptions():
    print("1 Monday")
    print("2 Tuesday")
    print("3 Wednesday")
    print("4 Thursday")
    print("5 Friday")
    print("6 Saturday")
    print("7 Sunday")
    print("8 Never")
    inp = str(input("Enter numbers seperated by commas: "))
    inp = inp.split(',')
    inp = [(int(i) - 1) for i in inp]
    return inp

def createEvent():
    name = str(input("Enter Name: "))
    date = str(input("Enter Date (mm/dd/yy): "))
    _time = str(input("Enter time (hh:mm am/pm): "))
    actions = addActions()
    repeat = repeatOptions()
    newEvent = event.Event(name, date, _time, actions, repeat)
    return newEvent

def main():
    eventList['events'] = event.loadEvents()
    clear()
    print("Events:")
    print("-"*20)
    displayEvents()
    print("-"*20)
    print("1) New Event")
    print("2) Delete Event")
    print("3) Exit")
    inp = str(input("Enter Number: "))

    if(inp == "1"):
        eventList['events'].append(createEvent())
        event.saveEvents(eventList['events'])
    elif(inp == "3"):
        exit()

while True:
    try:
        main()
    except KeyboardInterrupt:
        exit()
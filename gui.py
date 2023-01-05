import time
import os
import time
import threading

import automation
from action import Action
from event import Event, saveEvents, loadEvents

_events = []

def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system("clear")

def displayEvents(num=False):
    print("Events:")
    print("-"*20)
    if(_events != None):
        if(num == False):
            for e in _events:
                print(e.name, e.date, e._time)
        elif(num == True):
            for i,e in enumerate(_events):
                print(i+1, e.name)
    print("-"*20)

def displayActions(actions, num=False):
    print("Actions:")
    print("-"*20)
    if(num == False):
        for a in actions:
            print(a)
    elif(num == True):
        for i,a in enumerate(actions):
            print(i+1,a)
    print("-"*20)

def actionEditor(event=None):
    if(event != None):
        actions = event.actions
    else:
        actions = []
    
    while True:
        clear()
        displayActions(actions)

        print("1) Add Action")
        print("2) Remove Action")
        print("3) Save")
        inp = str(input("Enter Number: "))

        if(inp == "1"):
            clear()
            print("1) Open Link")
            print("2) Open Path")
            print("3) Notify")
            print("4) Run Command")
            actionInp = str(input("Enter Number: "))

            if(actionInp == "1"):
                link = str(input("Enter Link: "))
                action = Action("Open", "Link", link)
                actions.append(action)
            elif(actionInp == "2"):
                path = str(input("Enter Path to file or folder: "))
                action = Action("Open", "Path", path)
                actions.append(action)
            elif(actionInp == "3"):
                title = str(input("Enter Title: "))
                message = str(input("Enter Message: "))
                action = Action("Notify", title, message)
                actions.append(action)
            elif(actionInp == "4"):
                command = str(input("Enter Command Line Command: "))
                action = Action("Run", command)
                actions.append(action)
        elif(inp == "2" and len(actions) > 0):
            clear()
            displayActions(actions, num=True)
            actionInp = str(input("Enter Number: "))
            if(actionInp.isdigit()):
                del(actions[int(actionInp) - 1])
        elif(inp == "3"):
            if(event == None):
                return actions
            else:
                event.actions = actions
                return

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
    if(inp == "$c"):
        return
    inp = inp.split(',')
    inp = [(int(i) - 1) for i in inp]
    return inp

def createEvent():
    clear()
    name = str(input("Enter Name: "))
    if(name == "$c"):
        return

    date = str(input("Enter Date (mm/dd/yy): "))
    if(date == "today"):
        date = time.strftime("%m/%d/%Y", time.localtime())
    if(date == "$c"):
        return

    _time = str(input("Enter time (hh:mm am/pm): "))
    if(_time == "$c"):
        return

    actions = actionEditor()
    if(actions == None):
        return

    repeat = repeatOptions()
    if(repeat == None):
        return

    newEvent = Event(name, date, _time, actions, repeat)
    _events.append(newEvent)
    saveEvents(_events)

def editEvent():
    clear()
    displayEvents(num=True)
    eventNum = str(input("Enter Number: "))
    if(eventNum.isdigit()):
        selectedEvent = _events[int(eventNum) - 1]
    elif(eventNum == "$c"):
        return

    while True:
        clear()
        print("1) Edit Name")
        print("2) Edit Date")
        print("3) Edit Time")
        print("4) Edit Action")
        print("5) Edit Repeat")
        print("6) Save Changes")
        inp = str(input("Enter Number: "))

        if(inp == "1"):
            name = str(input("Enter Name: "))
            selectedEvent.name = name
        elif(inp == "2"):
            date = str(input("Enter Date: "))
            selectedEvent.date = date
        elif(inp == "3"):
            _time = str(input("Enter Time: "))
            selectedEvent._time = _time
        elif(inp == "4"):
            actionEditor(selectedEvent)
        elif(inp == "5"):
            clear()
            selectedEvent.repeat = repeatOptions()
        elif(inp == "6"):
            saveEvents(_events)
            return
        elif(inp == "$c"):
            return


def deleteEvent():
    if(len(_events) > 0):
        displayEvents(num=True)
        inp = str(input("Enter Number: "))
        if(inp == "$c"):
            return
        try:
            del(_events[int(inp)-1])
            saveEvents(_events)
        except ValueError:
            print()
            print("Invalid Input!")
            input("Press Enter to continue...")

def main():
    _events = loadEvents()
    clear()
    displayEvents()

    print("1) New Event")
    print("2) Delete Event")
    print("3) Edit Event")
    print("4) Exit")
    inp = str(input("Enter Number: "))

    if(inp == "1"):
       createEvent()
    elif(inp == "2"):
        deleteEvent()
    elif(inp == "3"):
        editEvent()
    elif(inp == "4"):
        exit()

run = True
def run_automation():
    while run:
        automation.main()
        return run

a = threading.Thread(target=run_automation)
a.start()

while True:
    try:
        _events = loadEvents()
        main()
    except KeyboardInterrupt:
        run = False
        exit()

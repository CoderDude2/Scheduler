import time
import event
import os

eventList = {
    "events":[]
}

def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system("clear")

def displayEvents(num=False):
    if(eventList['events'] != None):
        if(num == False):
            for e in eventList['events']:
                print(e.name,e.date,e._time)
        elif(num == True):
            for i,e in enumerate(eventList['events']):
                print(i+1, e.name)

def addActions():
    actions = []
    while True:
        clear()
        print("1) Open Link")
        print("2) Open File/Folder")
        print("3) Notify")
        print("4) Done")
        inp = str(input("Enter Number: "))

        if(inp == "1"):
            link = str(input("Enter Link: "))
            actions.append(f'Open+Link+{link}')
        elif(inp == "2"):
            path = str(input("Enter Path to file or folder: "))
            actions.append(f'Open+Path+{path}')
        elif(inp == "3"):
            title = str(input("Enter Title: "))
            message = str(input("Enter Message: "))
            actions.append(f'Notify+{title}+{message}')
        elif(inp == "$c"):
            return
        elif(inp == "4"):
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
    if(inp == "$c"):
        return
    inp = inp.split(',')
    inp = [(int(i) - 1) for i in inp]
    return inp

def createEvent():
    name = str(input("Enter Name: "))
    if(name == "$c"):
        return

    date = str(input("Enter Date (mm/dd/yy): "))
    if(date == "$c"):
        return

    _time = str(input("Enter time (hh:mm am/pm): "))
    if(_time == "$c"):
        return

    actions = addActions()
    if(actions == None):
        return

    repeat = repeatOptions()
    if(repeat == None):
        return

    newEvent = event.Event(name, date, _time, actions, repeat)
    return newEvent

def deleteEvent():
    if(len(eventList['events']) > 0):
        displayEvents(num=True)
        inp = str(input("Enter Number: "))
        if(inp == "$c"):
            return
        try:
            del(eventList['events'][int(inp)-1])
            event.saveEvents(eventList['events'])
        except ValueError:
            print()
            print("Invalid Input!")
            input("Press Enter to continue...")

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
        e = createEvent()
        if(e != None):
            eventList['events'].append(e)
            event.saveEvents(eventList['events'])
    elif(inp == "2"):
        deleteEvent()
    elif(inp == "3"):
        exit()

while True:
    try:
        main()
    except KeyboardInterrupt:
        exit()
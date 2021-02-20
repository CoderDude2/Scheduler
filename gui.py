from event import Event, saveEvents, loadEvents
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

def displayActions(actions, num=False):
    if(num == False):
        for a in actions:
            a = a.split('+')
            print(' '.join(a))
    elif(num == True):
        for i,a in enumerate(actions):
            a = a.split('+')
            print(i+1,' '.join(a))

def actionEditor(event=None):
    if(event != None):
        actions = event.actions
    else:
        actions = []
    while True:
        clear()
        print("Actions:")
        print("-"*20)
        displayActions(actions)
        print("-"*20)
        print("1) Add Action")
        print("2) Remove Action")
        print("3) Save")
        inp = str(input("Enter Number: "))

        if(inp == "1"):
            clear()
            print("1) Open Link")
            print("2) Open Path")
            print("3) Notify")
            actionInp = str(input("Enter Number: "))

            if(actionInp == "1"):
                link = str(input("Enter Link: "))
                actions.append(f'Open+Link+{link}')
            elif(actionInp == "2"):
                path = str(input("Enter Path to file or folder: "))
                actions.append(f'Open+Path+{path}')
            elif(actionInp == "3"):
                title = str(input("Enter Title: "))
                message = str(input("Enter Message: "))
                actions.append(f'Notify+{title}+{message}')
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
    name = str(input("Enter Name: "))
    if(name == "$c"):
        return

    date = str(input("Enter Date (mm/dd/yy): "))
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
    return newEvent

def editEvent():
    clear()
    displayEvents(num=True)
    eventNum = str(input("Enter Number: "))
    if(eventNum.isdigit()):
        selectedEvent = eventList['events'][int(eventNum) - 1]
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
            saveEvents(eventList['events'])
            return
        elif(inp == "$c"):
            return


def deleteEvent():
    if(len(eventList['events']) > 0):
        displayEvents(num=True)
        inp = str(input("Enter Number: "))
        if(inp == "$c"):
            return
        try:
            del(eventList['events'][int(inp)-1])
            saveEvents(eventList['events'])
        except ValueError:
            print()
            print("Invalid Input!")
            input("Press Enter to continue...")

def main():
    eventList['events'] = loadEvents()
    clear()
    print("Events:")
    print("-"*20)
    displayEvents()
    print("-"*20)

    print("1) New Event")
    print("2) Delete Event")
    print("3) Edit Event")
    print("4) Exit")
    inp = str(input("Enter Number: "))

    if(inp == "1"):
        e = createEvent()
        if(e != None):
            eventList['events'].append(e)
            saveEvents(eventList['events'])
    elif(inp == "2"):
        deleteEvent()
    elif(inp == "3"):
        editEvent()
    elif(inp == "4"):
        exit()

while True:
    try:
        main()
    except KeyboardInterrupt:
        exit()

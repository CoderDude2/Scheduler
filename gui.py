import calendar
import os
import time
from datetime import date, datetime
from datetime import time as dtime
import threading
import json

import action
import event
import igui




def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def save_events(events):
    serialized_events = [e.serialize() for e in events]
    json_events = json.dumps(serialized_events, indent=2)
    with open('events.json', 'w') as file:
        file.write(json_events)

def load_events():
    with open('events.json', 'r') as file:
        contents = file.read()
    
    json_events = [event.deserialize(e) for e in json.loads(contents)]
    return json_events

events = load_events()

def action_editor():

    actions = []

    while True:
        clear()
        
        [print(i) for i in actions]
        print('-'*25)
        igui.menu(options=[
            "Add Action",
            "Remove Action",
            "Done"
        ])

        inp = input()
        if(inp == '$c'):
            return

        inp = igui.parse_input(inp)

        if(inp[0] == 1):
            clear()
            igui.menu(options=[
                "Open Path",
                "Open Link",
                "Notify",
                "Run"
            ])

            inp2 = input()
            if(inp2 == '$c'):
                return

            inp2 = igui.parse_input(inp2)

            if(inp2[0] == 1):
                path = str(input("Enter Path: "))

                actions.append(action.Action('open', path))
            elif(inp2[0] == 2):
                link = str(input("Enter Link: "))

                actions.append(action.Action('open-link', link))
            elif(inp2[0] == 3):
                title = str(input("Enter Title: "))
                message = str(input("Enter Message: "))

                actions.append(action.Action('notify', title, message))
            elif(inp2[0] == 4):
                command = str(input("Enter Command: "))

                actions.append(action.Action('run', command))
        if(inp[0] == 3):
            return actions

def repeat_menu():
    output = {'days':[], 'repeat':0}
    
    while True:
        clear()

        igui.menu(options=[
            "Weekly",
            "Bi-Weekly",
            "Monthly",
            "Yearly",
            "Never"
        ])

        inp = input()

        try:
            inp = int(inp)
            if(inp == 1):
                output['repeat'] = event.WEEKLY
                break
            elif(inp == 2):
                output['repeat'] = event.BIWEEKLY
                break
            elif(inp == 3):
                output['repeat'] = event.MONTHLY
                break
            elif(inp == 4):
                output['repeat'] = event.YEARLY
                break
            elif(inp == 5):
                output['repeat'] = event.NEVER
                break
        except ValueError:
            if(inp == '$c'):
                return
    return output

def get_date():
    while True:
        while True:
            clear()
            _date = input("Enter Event Date (MM/DD/YYYY): ").lower()

            if(_date == '$c'):
                return
            if(_date == 'today'):
                return datetime.now().date()

            slash_count = 0
            for char in _date:
                slash_count += 1 if char == '/' or char == '-' else 0

            if(len(_date) >= 8 and len(_date) < 11 and slash_count == 2):
                if(not ('/' in _date and '-' in _date)):
                    break

            print("Incorrect format")
            time.sleep(0.5)

        try:
            _date = _date.split('/') if '/' in _date else _date.split('-')
            return date(year=int(_date[2]), month=int(_date[0]), day=int(_date[1]))
        except ValueError:
            print("Incorrect format")
            time.sleep(0.5)

def get_time():
    while True:
        while True:
            clear()
            _time = input("Enter Event Time (HH:MM AM/PM): ").lower()

            if(_time == '$c'):
                return
            if(len(_time) >= 7 and len(_time) < 9):
                if('am' in _time or 'pm' in _time):
                    break
            
            print("Incorrect format")
            time.sleep(0.5)
        
        _time = _time.split(' ')
        hour = 0

        try:
            if(_time[1] == 'am'):
                if(int(_time[0].split(':')[0]) == 12):
                    hour = 0
                else:
                    hour = int(_time[0].split(':')[0])
            elif(_time[1] == 'pm'):
                if(int(_time[0].split(':')[0]) == 12):
                    hour = int(_time[0].split(':')[0])
                else:
                    hour = int(_time[0].split(':')[0]) + 12

            minute = int(_time[0].split(':')[1])
            return dtime(hour=hour, minute=minute)
        except ValueError:
            print("Incorrect format")
            time.sleep(0.5)

def create_event() -> event.Event:
    clear()
    name = input("Enter Event Name: ")
    if(name == "$c"):
        return

    _date = get_date()
    if(not _date):
        return
    
    _time = get_time()
    if(not _time):
        return
    
    repeat = repeat_menu()
    if(not repeat):
        return
    
    actions = action_editor()
    print(actions)
    if(actions is None):
        return

    _event = event.Event(name, _date, _time, actions, repeat)
    return _event

def delete_event():
    global events
    while True:
        clear()
        igui.menu([e.name for e in events])
        inp = input()

        if(inp == '$c'):
            return

        inp = igui.parse_input(inp)

        if(inp != None):
            try:
                events.pop(inp[0] - 1)
                break
            except IndexError:
                continue

def select_event():
    clear()
    global events

    igui.menu([e.name for e in events])
    inp = input()

    if(inp == "$c"):
        return
    
    inp = igui.parse_input(inp)

    return events[(inp[0] - 1)]

def edit_event(event_to_edit:event.Event):
    clear()
    print(f"Name: {event_to_edit.name}")
    print(f"Date: {event_to_edit._date}")
    print(f"Time: {event_to_edit._time}")
    print(f"Repeat: { event.get_repeat_text(event_to_edit.repeat['repeat']).capitalize() }")

    print("\nActions:")
    print("-"*25)
    [print(a) for a in event_to_edit.actions]
    print("-"*25)
    input()

def gui():
    global events
    while True:
        clear()
        [print(e.name, e._date, e._time) for e in events]
        print("-"*25)
        igui.menu(options=[
            "New Event",
            "Edit Event",
            "Delete Event",
            "Exit"
        ])

        inp = igui.parse_input(input())
        if(inp):
            if(len(inp) > 1):
                print("Incorrect input")
                time.sleep(1)
            else:
                if(inp[0] == 1):
                    event = create_event()
                    if(event):
                        events.append(event)
                elif(inp[0] == 2):
                    print(edit_event(select_event()))
                elif(inp[0] == 3):
                    delete_event()
                if(inp[0] == 4):
                    exit_event.set()
                    save_events(events)
                    exit()

def check_event(event_to_check:event.Event):
    current_time = dtime(datetime.now().time().hour, datetime.now().time().minute, datetime.now().time().second)
    current_date = date(datetime.now().date().year, datetime.now().date().month, datetime.now().date().day)

    if(event_to_check.repeat['repeat'] == event.NEVER):
        if(current_date == event_to_check._date 
        and current_time == event_to_check._time):
            return True
    elif(event_to_check.repeat['repeat'] == event.WEEKLY):
        if((current_date - event_to_check._date).days % 7 == 0 
        and current_date >= event_to_check._date
        and current_time == event_to_check._time):
            return True
    elif(event_to_check.repeat['repeat'] == event.BIWEEKLY):
        if((current_date - event_to_check._date).days % 14 == 0 
        and current_date >= event_to_check._date
        and current_time == event_to_check._time):
            return True
    elif(event_to_check.repeat['repeat'] == event.MONTHLY):
        if(current_date.day == calendar.monthrange(current_date.year, current_date.month)[1] 
        and event_to_check._date.day > current_date.day 
        and current_date >= event_to_check._date
        and event_to_check._time == current_time):
            return True
        elif(current_date.day == event_to_check._date.day
        and current_date >= event_to_check._date
        and current_time == event_to_check._time):
            return True
    elif(event_to_check.repeat['repeat'] == event.YEARLY):
        if((current_date - event_to_check._date).days % 365 == 0 
        and current_date >= event_to_check._date
        and current_time == event_to_check._time):
            return True
    
    return False

def event_checker(exit_event):
    global events
    while True:
        for e in events:
            if(check_event(e)):
                [a.Do() for a in e.actions]    
            
        if(exit_event.is_set()):
            return False
        
        time.sleep(1)

exit_event = threading.Event()
t = threading.Thread(target=event_checker, args=(exit_event, ))

def main():
    t.start()
    gui()
    t.join()

if __name__ == '__main__':
    main()
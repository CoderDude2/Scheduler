import igui
import event
import os
import time
from datetime import datetime, date
from datetime import time as dtime
import calendar

def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def action_editor():
    raise NotImplementedError

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

    if(output['repeat'] == event.WEEKLY or output['repeat'] == event.BIWEEKLY):  
        while True:
            clear()

            igui.menu(options=[
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ])

            days = input().lower()

            if(days == "$c"):
                return
            else:
                output["days"] = igui.parse_input(days)
            break
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
    # TODO
    # Add action editor system
    _event = event.Event(name, _date, _time, None, repeat)
    return _event

def gui():
    events = []
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
                        print(event.serialize())
                        input()
                        events.append(event)
                if(inp[0] == 4):
                    exit()

gui()
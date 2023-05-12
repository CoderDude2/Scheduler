import igui
import event
import os
import time
from datetime import datetime, date, time
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
                return None

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
                return None
            else:
                output["days"] = igui.parse_input(days)
            break
    return output

def get_date():
    _date = input("Enter Event Date (MM/DD/YYYY): ").lower()
    
    if(_date == 'today'):
        return datetime.now().date()
    
    _date = _date.split('/')
    return date(year=int(_date[2]), month=int(_date[0]), day=int(_date[1]))

def create_event() -> event.Event:
    clear()
    name = input("Enter Event Name: ")
    _date = get_date()
    _time = input("Enter Event Time (HH:MM AM/PM): ")    
    repeat = repeat_menu()
    # TODO
    # Add action editor system
    _event = event.Event(name, _date, _time, None, repeat)
    return _event

def main():
    while True:
        clear()
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
                    create_event()
                if(inp[0] == 4):
                    exit()

main()
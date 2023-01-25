import time

def menu(options=[]) -> list[int]:
    for i, option in enumerate(options):
        print(f'{i+1}) {option}')

def table(headers=[], entries=[]):
    pass


def parse_input(msg, decrement_by_one=False):
    if(len(msg) == 1):
        try:
            output = [int(msg)]
            return output
        except ValueError:
            print("Invalid Input")
            time.sleep(1)
            return

    if('-' in msg):
        try:
            output = [int(i) for i in list(range( int(msg.split('-')[0]), int(msg.split('-')[1])+1))]
        except ValueError:
            print("Invalid Input!")
            time.sleep(1)
            return
        
        for i in output:
            if(i < 0):
                return
        return output
    
    if("," in msg):
        try:
            output = [int(i) for i in msg.split(",")]
            for i in output:
                if(i < 0):
                    return
            return output
        except ValueError:
            print("Invalid Input!")
            time.sleep(1)
            return
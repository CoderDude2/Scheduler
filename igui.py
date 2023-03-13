import time

def menu(options=[]) -> list[int]:
    for i, option in enumerate(options):
        print(f'{i+1}) {option}')

def table(headers=[], entries=[]):
    pass


def parse_input(msg):
    msg = ''.join(msg.split(" ")).split(',')
    output = []

    for i, inp in enumerate(msg):
        if('-' in inp):
            try:
                minimum_value = int(inp.split('-')[0])
                maximum_value = int(inp.split('-')[1])
                [output.append(i) for i in list(range(minimum_value, maximum_value+1)) if i not in output]
            except ValueError:
                return
        else:
            try:
                if(int(inp) not in output):
                    output.append(int(inp))
            except ValueError:
                return
    return output
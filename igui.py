def menu(options=[]):
    for i, option in enumerate(options):
        print(f'{i+1}) {option}')

def table(headers=[]):
    pass

def parse_input(msg) -> list[int]:
    msg = ''.join(msg.split(" ")).split(',')
    output = []

    for index, inp in enumerate(msg):
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
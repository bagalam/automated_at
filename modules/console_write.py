def prGreen(skk): return"\033[92m {}\033[00m" .format(skk)
def prRed(skk): return"\033[91m {}\033[00m" .format(skk)
LINE_CLEAR = '\x1b[2K'

def print_tests(tests):
    print(prGreen(f"Tests passed: {tests[0]}"))
    print(prRed(f"Tests not passed: {tests[1]}"))
    print(f"Total commands: {tests[0]+tests[1]}")

def print_current(command, result, tests):
    print(f"{command:<10} {result:<6} {prGreen(f'Tests passed: {tests[0]}'):<20} {prRed(f'Tests not passed: {tests[1]}'):<20}", end='\r')
    print(end=LINE_CLEAR)
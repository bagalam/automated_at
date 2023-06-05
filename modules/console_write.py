import sys
sys.dont_write_bytecode = True

def prGreen(skk): return"\033[92m {}\033[00m" .format(skk)
def prRed(skk): return"\033[91m {}\033[00m" .format(skk)
LINE_CLEAR = '\x1b[2K'
CURSOR_UP = "\033[1A"

def print_tests(tests):
    print(prGreen(f"Tests passed: {tests[0]}"))
    print(prRed(f"Tests not passed: {tests[1]}"))
    print(f"Total commands: {tests[0]+tests[1]}")

def print_current(command, result, tests):
    print(f"{command:<10} {result:<6}")
    print(prGreen(f'Tests passed: {tests[0]}'))
    print(prRed(f'Tests not passed: {tests[1]}'))
    #print(end=LINE_CLEAR)
    print(2*(CURSOR_UP + LINE_CLEAR)+ CURSOR_UP, end="")
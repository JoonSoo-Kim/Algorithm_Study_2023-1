import sys

buffer, result, char = '', '', ''
is_reversed = True


def flush():
    global result, buffer, char
    result += buffer + char
    buffer = ''


for char in sys.stdin.readline().rstrip():
    match char:
        case '<' | '>':
            flush()
            is_reversed = not is_reversed
        case ' ':
            flush()
        case _:
            buffer = char + buffer if is_reversed else buffer + char

print(result + buffer)

import sys
input = sys.stdin.readline

def explode_str(string: str, bomb: str) -> str:
    explode = []

    for char in string:
        explode.append(char)

        if len(explode) < len(bomb):
            continue
        else:
            if "".join(explode[-len(bomb):]) == bomb:
                for _ in range(len(bomb)):
                    explode.pop()

    if len(explode) == 0:
        return "FRULA"
    else:
        return "".join(explode)

# 입력에 \n이 섞여들어와서 이를 제거해줌
string = input()
string = string[:-1]
bomb = input()
bomb = bomb[:-1]
print(explode_str(string, bomb))
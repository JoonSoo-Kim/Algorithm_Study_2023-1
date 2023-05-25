def convert_str(char: str) -> str:
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine"]
    try:
        result = str(num_list.index(char))
        return result
    except:
        return "Error"


def solution(s) -> int:
    result = ""
    temp = ""

    for char in s:
        if 48 <= ord(char) and ord(char) < 58:
            result += char
            continue

        temp += char
        if convert_str(temp) != "Error":
            result += convert_str(temp)
            temp = ""

    answer = int(result)
    return answer

for i in range(9, -1, -1):
    print(i)
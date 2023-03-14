import re

def isPalindrome(sentence):
    sentence = re.sub(r"[^a-zA-Z0-9]", "", sentence).lower()
    for i in range(len(sentence) - 1):
        if(sentence[i] != sentence[len(sentence) - i - 1]):
            print(sentence[i], sentence[len(sentence) - i - 1])
            return False
    return True


sentence = input()
result = isPalindrome(sentence)
if(result == True):
    print("true")
elif(result == False):
    print("false")
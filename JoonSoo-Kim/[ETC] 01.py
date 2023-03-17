import re
import collections

def isPalindrome(sentence):
    sentence = re.sub(r"[^a-zA-Z0-9]", "", sentence).lower()
    for i in range(len(sentence) - 1):
        if(sentence[i] != sentence[len(sentence) - i - 1]):
            print(sentence[i], sentence[len(sentence) - i - 1])
            return False
    return True

# 리스트로 변환
def isPalindromeExample01(self, sentence: str) -> bool:
    processedSentence = []
    for char in sentence:
        if char.isalnum():
            processedSentence.append(char.lower())

    while len(processedSentence) > 1:
        if processedSentence.pop(0) != processedSentence.pop():
            return False
    return True

# 데크를 이용한 최적화
def isPalindromeExample02(self, sentence: str) -> bool:
    sentenceDeque = collections.deque()

    for char in sentence:
        if char.isalnum():
            sentenceDeque.append(char.lower())

    while len(sentenceDeque) > 1:
        if sentenceDeque.popleft() != sentenceDeque.pop():
            return False
    return True

# 슬라이싱 사용
def isPalindromeExample03(self, sentence: str) -> bool:
    sentence = sentence.lower()
    sentence = re.sub("[^a-z0-9]", '', sentence)

    return sentence == sentence[::-1]


sentence = input()
result = isPalindrome(sentence)
if(result == True):
    print("true")
elif(result == False):
    print("false")
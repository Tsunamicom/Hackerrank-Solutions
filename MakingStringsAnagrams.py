# https://www.hackerrank.com/challenges/ctci-making-anagrams

def number_needed(a, b):
    anagramDict = dict()
    for letter in a:
        if not(letter in anagramDict.keys()):
            anagramDict[letter] = 1
        else:
            anagramDict[letter] += 1
    for letter in b:
        if not(letter in anagramDict.keys()):
            anagramDict[letter] = -1
        else:
            anagramDict[letter] -= 1
    for count in anagramDict:
        if anagramDict[count] < 0:
            anagramDict[count] = abs(anagramDict[count])
    
    return sum(anagramDict.values())

a = input().strip()
b = input().strip()
if a == b:
    print(0)
else:
    print(number_needed(a, b))

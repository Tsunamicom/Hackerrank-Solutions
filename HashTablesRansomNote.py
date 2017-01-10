# https://www.hackerrank.com/challenges/ctci-ransom-note

def ransom_note(magazine, ransom):
    noteDict = dict()
    for word in magazine:
        if word in noteDict.keys():
            noteDict[word] += 1
        else:
            noteDict[word] = 1
    for word in ransom:
        if not(word in noteDict.keys()):
            return False
        else:
            noteDict[word] -= 1
            if noteDict[word] < 0:
                return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
if m < n:
    print("No")
else:
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
    

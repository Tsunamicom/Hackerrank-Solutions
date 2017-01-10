# https://www.hackerrank.com/challenges/ctci-balanced-brackets

def is_matched(expression):
    stack = list()  #Implement stack as array/list
    expressionDict = {"}":"{", ")":"(", "]":"["}
    for character in expression:
        if character in expressionDict.values():
            stack.append(character)
        elif character in expressionDict.keys():
            try:
                if expressionDict[character] != stack[-1]:
                    return False
                else:
                    stack.pop()
            except:
                return False
        else:
            return False
    return len(stack)== 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

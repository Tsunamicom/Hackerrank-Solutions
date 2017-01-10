# https://www.hackerrank.com/challenges/ctci-big-o

from math import sqrt, floor
def primeCheck(num):
    if num == 1:
        return "Not prime"
    elif num == 2:
        return "Prime"
    elif num % 2 == 0:
        return "Not prime"
    else:
        for i in range(2, floor(sqrt(num))+1):
            if num % i == 0:
                #print("{} % {} == 0".format(num, i))
                return "Not prime"
        return "Prime"
                

for test in range(int(input())):
    print(primeCheck(int(input())))

# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

def gatherData():
    number_array = list()
    for _ in range(int(input())):
        number_array.append(input()[-10:])
    return number_array

def displayData(data):
    for num in sorted(data):
        print("+91 "+num[:5]+" "+num[5:])
        
displayData(gatherData())

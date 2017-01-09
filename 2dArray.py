# https://www.hackerrank.com/challenges/2d-array

import sys
   

# Given Code
arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
# End Given Code

class Hourglass:
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
    
    def getValue(self):
        return sum(self.top) + self.middle + sum(self.bottom)

def findHourglasses(array):
    """Given an array, return an array of Hourglass"""
    hourglasses = list()
    rownum = 0
    while rownum <= len(array)-3:
        for num in range(0, len(array[rownum])-2):
            top = array[rownum][num:num+3]
            middle = array[rownum+1][num+1]
            bottom = array[rownum+2][num:num+3]
            hourglasses.append(Hourglass(top, middle, bottom))
        rownum += 1
    return hourglasses

def maxHourglass(array):
    """Given an array of Hourglass, return the value of the Hourglass with
    the maximum .getValue() integer.
    """
    maximum = -99999999999999999
    for hourglass in range(len(array)):
        maximum = max(array[hourglass].getValue(), maximum)
    return maximum

hourglasses = findHourglasses(arr)
print(maxHourglass(hourglasses))

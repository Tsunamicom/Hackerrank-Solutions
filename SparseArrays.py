# https://www.hackerrank.com/challenges/sparse-arrays

strnum = int(input())
strings = [input() for string in range(strnum)]
querynum = int(input())
for queries in range(querynum):
    query = input()
    print(strings.count(query))

# https://www.hackerrank.com/challenges/dynamic-array

N, Q = [int(num) for num in input().split(' ')]
allqueries = {num: list() for num in range(N)}
lastAns = 0
for queries in range(Q):
    query = [int(num)for num in input().split()]
    sequencenum = (query[1]^lastAns) % N
    if query[0] == 1:
        allqueries[sequencenum].append(query[2])
    else:
        lastAns = allqueries[sequencenum][(query[2])%(len(allqueries[sequencenum]))]
        print(lastAns)

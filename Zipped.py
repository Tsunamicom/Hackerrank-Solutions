# https://www.hackerrank.com/challenges/zipped

studentIdNum, subjects = [int(x) for x in input().split()]
subjectMaster = list()
for subject in range(subjects):
    subjectMaster.append([float(x) for x in input().split()])
for student in zip(*subjectMaster):
    print(sum(student)/subjects)

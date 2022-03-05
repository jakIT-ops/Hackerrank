import math

def mean(lst):
    return sum(lst) / len(lst)

def sdev(lst, size):
    sum = 0
    for i in range(size):
        sum = sum + (lst[i] - mean(lst)) ** 2
    return math.sqrt(sum / size)

size = int(input())
lst = list(map(int, input().split()))

print(round(sdev(lst, size), 1))
# Enter your code here. Read input from STDIN. Print output to STDOUT
def Mean(lst):
    sum = 0
    for i in lst:
        sum += i
    mean = float(sum) / len(lst)
    return mean
    
def Median(lst):
    median = 0.0
    size = len(lst)
    copy = lst
    copy.sort()
    if(size % 2 == 0):
        median = float(copy[size//2 - 1] + copy[size//2]) / 2
    else:
        median = copy[(size - 1)/2]
    return median
    
def Mode(lst):
    mode = 0
    size = len(lst)
    count, max =0,0
    copy = lst
    copy.sort()
    current = 0
    for i in copy:
        if(i == current):
            count += 1
        else:
            count = 1
            current = i
        if(count > max):
            max = count
            mode = i
    return mode

size = int(input())
lst = list(map(int, input().split()))
print(Mean(lst))
print(Median(lst))
print(Mode(lst))
# Hylbar bichiglel
'''
import numpy as np
from scipy impor stats

size = int(input())
lst = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
'''
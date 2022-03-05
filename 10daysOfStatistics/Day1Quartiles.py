def median(lst):
    size = len(lst)
    if(size % 2 == 0):
        return (lst[size // 2] + lst[size // 2 - 1]) // 2
    else:
        return lst[size // 2]

def quart(size, lst):
    print(median(lst[:size//2])) # Q1
    print(median(lst)) # Q2
    if(size % 2 == 0):  # Q3
        print(median(lst[size//2:]))  
    else:
        print(median(lst[size//2+1:]))

size = int(input())
lst = list(map(int, input().split()))
lst.sort()
quart(size, lst)
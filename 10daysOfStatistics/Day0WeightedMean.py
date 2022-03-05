size = int(input())
lst = list(map(int, input().split()))
weights = list(map(int, input().split()))
total = 0
for i in range(size):
    total += lst[i] * weights[i]
    
print(round(total / sum(weights), 1))
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Боломжуудыг шалгах
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if(dice1[i] != dice1[j] and (dice1[i] + dice1[j]) == 9):
            total_possibilities += 1
            print("{0} + {1} = {2}".format(dice1[i], dice2[j], (dice1[j] + dice1[i])))

# Магадлалыг авах
probability = total_possibilities / total
print("Probability: {0}/{1} = {2}".format(total_possibilities, total, probability))
# hariult : <p>1/9</p>
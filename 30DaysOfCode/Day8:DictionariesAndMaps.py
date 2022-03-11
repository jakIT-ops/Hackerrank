n = int(input())
phoneBook = dict()
for i in range(n):
    line = input()
    line = line.split()
    phoneBook[line[0]] = phoneBook.get(line[0],line[1])

while 1:
    try:
        q = input()
        if q in phoneBook:
            print(str(q) + "=" + str(phoneBook[q]))
        else:
            print("Not found")
    except:
        break
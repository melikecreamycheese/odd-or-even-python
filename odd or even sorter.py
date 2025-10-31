import random

evlist = []

for k in "gggggggggggggggggggg":
    evlist.append(random.randint(1,50))


find = "0"
calculated = 0

for i in evlist:
    calculated = i / 2
    if find in str(calculated):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

input("")
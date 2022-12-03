

backpackList = []


priorityList = ["empty",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("input3.txt", "r") as file:

    for line in file:

        wrongLength = len(line)

        line = line[0:wrongLength - 1]

        backpackList.append(line)

compartment1 = []

compartment2 = []

for item in backpackList:

    length = len(item)
    endLength = int(length + 1)
    halfLength = int(length/2 + 1)

    compartment1.append(item[0:halfLength])

    compartment2.append(item[halfLength:endLength])


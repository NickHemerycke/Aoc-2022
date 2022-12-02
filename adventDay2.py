

matchList = []

with open ("input2.txt","r") as file:

    for line in file:

        line = line[:3]

        matchList.append(line)

print(matchList)
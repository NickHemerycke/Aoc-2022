

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


counterCompartment = 0

letterCheckBasedOnForLoop = "empty"

letterList = []

letterCheck = []

listCheck = len(letterCheck)

for item in compartment1:

    for letter in item:

        if listCheck == 0:

            for letter2 in compartment2[counterCompartment]:

                if letter == letter2:

                    letterList.append(letter)
                    letterCheck.append(letter)
                    listCheck = len(letterCheck)
            
                else:   

                    letterList = letterList

        else:

            for letterC in letterCheck:

                if letterC == letter:

                    letterCheckBasedOnForLoop = True

                    if letterCheckBasedOnForLoop == True:

                        alfred = False

                    else:
                        for letter2 in compartment2[counterCompartment]:

                            if letter == letter2:

                                letterList.append(letter)
                                letterCheck.append(letter)
            
                            else:   

                                letterList = letterList
            
                else:

                    letterCheckBasedOnForLoop = False

                    if letterCheckBasedOnForLoop == True:

                        alfred = False

                    else:
                        for letter2 in compartment2[counterCompartment]:

                            if letter == letter2:

                                letterList.append(letter)
                                letterCheck.append(letter)
            
                            else:   

                                letterList = letterList
            
    letterCheck = []
        
    counterCompartment = counterCompartment + 1

pointList = []

for letters in letterList:

    point = priorityList.index(letters)

    pointList.append(point)

totalScore = 0

for points in pointList:

    points = int(points)

    totalScore = totalScore + points

print(totalScore)
calorieList = []

with open("adventDay1.txt", "r") as file:

    for line in file:

        line = int(line)
        calorieList.append(line)


elf = "elf"

def elfCalorieCounter(calorie):

    ElfList = []

    calorieAmount = 0


    for i in calorieList:

        if i > 0 :
            
            calorieAmount = calorieAmount + i
        
        else:

            ElfList.append(calorieAmount)

            calorieAmount = 0


    return(ElfList)

def findBigElfs(calorie ):

    bigElfList = []

    counter = 1

    output = elfCalorieCounter(calorieList)

    bigNumber = max(output)

    for i in elfCalorieCounter(calorieList):

        if i == bigNumber:

            bigElfList.append(counter)

            counter = counter + 1

        else:

            counter = counter + 1

    return bigElfList

numbers = elfCalorieCounter(calorieList)

biggestNumber = max(numbers)

biggestNumber= str(biggestNumber)

index = findBigElfs(calorieList)

index = str(index)

print(biggestNumber)

print(index)

print("elf or elves number " + index + " with a total of " + biggestNumber + " calories.")

        

#remove een nul want ja kheb me text file verkeerd append oops







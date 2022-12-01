calorieList = [1000,2000,3000,0,4000,0,5000,6000,0,7000,8000,9000,0,10000]


def elfCalorieCounter(calorie):

    ElfList = []

    calorieAmount = 0


    for i in calorieList:

        if i > 0 :
            
            calorieAmount = calorieAmount + i
        
        else:

            ElfList.append(calorieAmount)

            calorieAmount = 0

            print(ElfList)

elfCalorieCounter(calorieList)






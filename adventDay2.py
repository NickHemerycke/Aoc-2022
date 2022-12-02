

matchList = []

with open ("input2.txt","r") as file:

    for line in file:

        line = line[:3]

        matchList.append(line)


def didIWin(matches):

    winList = []
    playList = []

    for i in matches:

        opponent = i[0]

        me = i [2]

        if((opponent == "A" and me == "Y") or (opponent == "B" and me == "Z") or (opponent == "C" and me == "X")):

            winList.append("win")
            playList.append(me)
        
        elif((opponent == "A" and me == "X") or (opponent == "B" and me == "Y") or (opponent == "C" and me == "Z")):

            winList.append("draw")
            playList.append(me)

        elif((opponent == "A" and me == "Z") or (opponent == "B" and me == "X") or (opponent == "C" and me == "Y")):

            winList.append("loss")
            playList.append(me)

    return(winList, playList)



def scoreCalc(matches):

    score = 0

    counter = 0

    alfa = didIWin(matches)

    beta = alfa[0]

    gamma = alfa[1]

    for i in beta:

        if(i == "win"):

            score = score + 6

            if(gamma[counter] == "X"):

                score = score + 1

            elif(gamma[counter] == "Y"):

                score = score + 2

            elif(gamma[counter] == "Z"):

                score = score + 3
            







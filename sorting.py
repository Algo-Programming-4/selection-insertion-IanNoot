
import random
import time

#Swaps two elements in a list
def swap(location1, location2, inputList):
    x = inputList[location2]
    inputList[location2] = inputList[location1]
    inputList[location1] = x
    

#Goes through the list, grabs the largest number and moves it until it finds a larger number, when the end of the list is found, deposit the largest number in a seperate list
def bubble(input):
    
    summedInput = 0
    for i in input:
        summedInput += i

    print(summedInput)


    outputList = []
    arrow = 0
    
    
    while (len(input) > 0):
        print(outputList)
        highest = -1
        arrow = 0
        for i in input:
            #If I find a higher value than the stored highest
            if i > highest:
                highest = i
            else:
                swap(arrow - 1, arrow, input)
            #If I'm at the end, break out of the inner loop
            arrow += 1
        outputList.insert(0, input[arrow - 1])
        input.pop(arrow - 1)


    summedOutput = 0
    for i in input:
        summedOutput += i
    print(summedOutput)

    print(outputList)

    return outputList


#Treats the list like a deck of cards, takes the top card off the pile and slides it where it belongs in a seperate pile that is always sorted
def insertion(input):
    outputList = []
    arrow = 0


    while (len(input) > 0):
        heldValue = input[0]
        foundASpot = False
        
        if len(outputList) > 0:
            
            arrow = 0
            #Iterate through the sorted list
            foundASpot = False
            while arrow < len(outputList):
                
                #If this value is greater than me, the previous spot is my spot
                if outputList[arrow] > heldValue or outputList[arrow] == heldValue:
                    outputList.insert(arrow, heldValue)
                    foundASpot = True
                    break    
                else:
                    arrow += 1
                    
            if foundASpot == False:
                outputList.append(heldValue)
        # I am 4
        #  0, 1, 2, 3, 4, 5(arrow)
        #If this is the first iteration
        else:
            outputList = [heldValue]

        #Remove the item I sorted into the list
        input.pop(0)
    ##End of while

    return outputList


def selection(input):

    outputList = []
    lowestLocation = 1

    while (len(input) > 0):
        arrow = 0
        lowestLocation = 0
        
        #Iterate over the list elements
        for i in input:   
            
            #If this value is smaller than the previously grabbed lowest, this is the new lowest
            if (input[arrow] < input[lowestLocation]):
                lowestLocation = arrow
            arrow += 1


        if lowestLocation > 0:
            swap(0, lowestLocation, input)
        outputList.append(input[0])
        input.pop(0)

    return outputList


randList = []

for i in range(0,100,1):
    randList.append(i)

random.shuffle(randList)
    
randList.append(random.randint(0,99))

print(randList)


bubble(randList)

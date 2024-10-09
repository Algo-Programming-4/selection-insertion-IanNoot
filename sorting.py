
import random
import time

#Swaps two elements in a list
def swap(location1, location2, inputList):
    x = inputList[location2]
    inputList[location2] = inputList[location1]
    inputList[location1] = x
    return inputList
    

#Goes through the list, grabs the largest number and moves it until it finds a larger number, when the end of the list is found, deposit the largest number in a seperate list
def bubble(input):
    
    outputList = []
    arrow = 0
    
    
    while (len(input) > 0):
        highest = input[0]
        arrow = 0
        while (True):
            #Sets the first element as the highest value to start
            if arrow == 0:
                highest = input[arrow]
                input.pop(0)
            #If I find a higher value
            elif input[arrow] > highest:
                #place the old highest in its new spot
                input.insert(arrow, highest)
                #set the new highest
                highest = input[arrow + 1]
                input.pop(arrow + 1)
            #If I'm at the end, break out of the inner loop
            arrow += 1
            if arrow >= len(input):
                outputList.insert(0, highest)
                break
    for i in outputList:
        print("[" + str(i) + "]")


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
        while arrow < len(input) - 1:   
            
            #If this value is smaller than the previously grabbed lowest, this is the new lowest
            if (input[arrow] < input[lowestLocation]):
                lowestLocation = arrow
            arrow += 1


        if lowestLocation > 0:
            swap(0, lowestLocation, input)
        outputList.append(input[0])
        input.pop(0)

    return outputList

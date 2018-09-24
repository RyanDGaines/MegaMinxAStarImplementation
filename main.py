from Side import side
import random as rd
from datetime import datetime
import astar
import time


#Function for printing all cube sides
def printCube(megaminx):
    counter = 1
    for i in megaminx:
        print("Side " + str(counter) + ":")
        i.display()
        counter = counter + 1


def main():
    print("Initialzing the Megaminx...")
    megaMinx = list()
    counter = 1
    #Put intial values in megaminx, based off greek alphabet
    for i in "AΒΓΔΕΖΗΘΙΚΛΜ":
        temp = side(i)
        megaMinx.append(temp)
        print("Side", counter)
        temp.display()
        counter = counter + 1


    #adds all the relations, based off of map.png
    megaMinx[0].addrelations([megaMinx[1], megaMinx[2], megaMinx[3], megaMinx[4], megaMinx[5]])
    megaMinx[1].addrelations([megaMinx[0], megaMinx[5], megaMinx[7], megaMinx[11], megaMinx[2]])
    megaMinx[2].addrelations([megaMinx[3], megaMinx[0], megaMinx[1], megaMinx[11], megaMinx[10]])
    megaMinx[3].addrelations([megaMinx[9], megaMinx[4], megaMinx[0], megaMinx[2], megaMinx[10]])
    megaMinx[4].addrelations([megaMinx[9], megaMinx[8], megaMinx[5], megaMinx[0], megaMinx[3]])
    megaMinx[5].addrelations([megaMinx[4], megaMinx[8], megaMinx[7], megaMinx[1], megaMinx[0]])
    megaMinx[6].addrelations([megaMinx[7], megaMinx[8], megaMinx[9], megaMinx[10], megaMinx[11]])
    megaMinx[7].addrelations([megaMinx[6], megaMinx[11], megaMinx[1], megaMinx[5], megaMinx[8]])
    megaMinx[8].addrelations([megaMinx[9], megaMinx[6], megaMinx[7], megaMinx[5], megaMinx[4]])
    megaMinx[9].addrelations([megaMinx[3], megaMinx[10], megaMinx[6], megaMinx[8], megaMinx[4]])
    megaMinx[10].addrelations([megaMinx[3], megaMinx[2], megaMinx[11], megaMinx[6], megaMinx[9]])
    megaMinx[11].addrelations([megaMinx[10], megaMinx[2], megaMinx[1], megaMinx[7], megaMinx[6]])


    # While not quit, display options for code
    quit = False
    while (not quit):
        print("Please select an option:")
        print("S - Rotate a chosen side") # for solving or custom mixing!
        print("R - Randomly mix the megaminx (clockwise moves only!)") #randomly rotate (can do outside of 3-20 but tells you to enter 3-20)
        print("D - display a chosen side") #Displays side and neighbors
        print("A - solve using a* algorithm") #solve using A* (astar.py)
        print("Q - to quit")
        selection = input()


        # Rotate a given side L or R, print error message if not L or R and if not a valid side
        if (selection == "s" or selection == "S"):
            print("Which side to rotate clockwise? (1-12 based on map.png)")
            selection = input()
            try:
                print("Which direction?\nR for Clockwise and L for CounterClockWise:")
                direction = input()
                if (direction == "R"):
                    megaMinx[int(selection) - 1].rotateClock()
                    megaMinx[int(selection) - 1].displayRelations()
                elif(direction == "L"):
                    megaMinx[int(selection) - 1].rotateCounter()
                    megaMinx[int(selection) - 1].displayRelations()
                else:
                    raise ValueError()

            except ValueError and IndexError:
                print("Error! Invalid!")

        # Quits!
        elif (selection == "q" or selection == "Q"):
                quit = True

        #Displays a side, or the entire megaminx
        elif (selection == "d" or selection == "D"):
            print("Which side to display? (1-12 based on map.png) A for all")
            selection = input()
            if (selection == "A"):
                printCube(megaMinx)
            else:
                # Display side with relations
                try:
                    megaMinx[int(selection) - 1].displayRelations()
                except ValueError and IndexError:
                    print("Error not a valid number!")

        # Randomly rotate the cube k times, based off of system time
        elif (selection == "R" or selection == "r"):
            systemtime = datetime.now()
            rd.seed(systemtime)
            numRotates = input("How many k rotations?(3-20)")
            print("Rotating Clockwise! (this information is not stored!")
            for i in range(0, int(numRotates)):
                rotated = rd.randint(0,11)
                print("rotated:", rotated) # Again, not stored but printed to compare to results
                megaMinx[rotated].rotateClock()

            print("Mixed with", numRotates, "rotations clockwise!")

            #Redisplays the megaMinx
            counter = 1
            for i in megaMinx:
                print("Side", counter)
                i.display()
                counter = counter + 1

        #calls a* to solve the cube, calculates time to solve
        elif (selection == "A" or selection == "a"):
            start = time.time()
            solver = astar.aStar(megaMinx)
            print("Time: %s seconds" % (time.time() - start))
            print("Do you want to solve?")
            # Solves it for you so you can run again how nice of it
            response = input()
            if (response == "y" or response == "Y"):
                for i in solver:
                    megaMinx[i].rotateCounter()

main()
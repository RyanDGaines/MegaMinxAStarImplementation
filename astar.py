from Side import side
from math import floor, ceil
from queue import PriorityQueue


# THE FOLLOWING LINK IS WHERE I GOT ALOT OF HELP FOR A*
# https://www.redblobgames.com/pathfinding/a-star/implementation.html


# Create a node class, which holds the megaminx and the priority weight, as well as define
# custom comparisons to determine which one priority queue get call next
class Node:
    def __init__(self, item, weight):
        self.item = item
        self.priority = weight

    # Do comparisons based off of these priority comparisons
    def __eq__(self, other):
        return self.priority == other.priority
    def __ne__(self, other):
        return self.priority != other.priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __le__(self, other):
        return self.priority <= other.priority
    def __gt__(self, other):
        return self.priority > other.priority
    def __ge__(self, other):
        return self.priority >= other.priority


    # return the megaminx
    def returnMinx(self):
        return self.item

    # Add a direction to parent and child node
    def addClockwise(self, move):
        self.clockwiseMove = move
    def addCounter(self, move):
        self.counterMove = move


# Creates new megaminx so seperate one is called in memory, prevents same memoty location from constantly being called
def createNewMegaMinx(megaminx):
    newMegaminx = []
    for i in megaminx:
        newMegaminx.append(side(color=i.center, listofRelates=None, Movable=i.listofMovable[:]))
    newMegaminx[0].addrelations([newMegaminx[1], newMegaminx[2], newMegaminx[3], newMegaminx[4], newMegaminx[5]])
    newMegaminx[1].addrelations([newMegaminx[0], newMegaminx[5], newMegaminx[7], newMegaminx[11], newMegaminx[2]])
    newMegaminx[2].addrelations([newMegaminx[3], newMegaminx[0], newMegaminx[1], newMegaminx[11], newMegaminx[10]])
    newMegaminx[3].addrelations([newMegaminx[9], newMegaminx[4], newMegaminx[0], newMegaminx[2], newMegaminx[10]])
    newMegaminx[4].addrelations([newMegaminx[9], newMegaminx[8], newMegaminx[5], newMegaminx[0], newMegaminx[3]])
    newMegaminx[5].addrelations([newMegaminx[4], newMegaminx[8], newMegaminx[7], newMegaminx[1], newMegaminx[0]])
    newMegaminx[6].addrelations([newMegaminx[7], newMegaminx[8], newMegaminx[9], newMegaminx[10], newMegaminx[11]])
    newMegaminx[7].addrelations([newMegaminx[6], newMegaminx[11], newMegaminx[1], newMegaminx[5], newMegaminx[8]])
    newMegaminx[8].addrelations([newMegaminx[9], newMegaminx[6], newMegaminx[7], newMegaminx[5], newMegaminx[4]])
    newMegaminx[9].addrelations([newMegaminx[3], newMegaminx[10], newMegaminx[6], newMegaminx[8], newMegaminx[4]])
    newMegaminx[10].addrelations([newMegaminx[3], newMegaminx[2], newMegaminx[11], newMegaminx[6], newMegaminx[9]])
    newMegaminx[11].addrelations([newMegaminx[10], newMegaminx[2], newMegaminx[1], newMegaminx[7], newMegaminx[6]])
    return newMegaminx

# The actual a* formula
def aStar(megaminx):
    # Create a priority queue
    queue = PriorityQueue()
    # Create the inital node, with new memory location of megaminx
    n = Node(createNewMegaMinx(megaminx), 0)

    #Start flags
    n.addClockwise("START")
    n.addCounter("START")

    # put node in priority queue
    queue.put(n)

    # Get megaminx as string, this is the start of megaminx (used for dictionary)
    megaStringstart = MegaMinxAsString(megaminx)

    # Dictionaries to record cost so far based on key megaminxString and parent based on megaminxstring
    parent = {}
    costSoFar ={}

    #intial values
    parent[megaStringstart] = None
    costSoFar[megaStringstart] = 0

    #none have been expanded, lets start loop
    numExpanded = 0

    print(heuristic(megaminx))
    # while the queue is not empty
    while not queue.empty():
        # get the lowest on the queue, only megaminx though
        current = queue.get().returnMinx()
        # make the megaminx as string (for dictionary reasons)
        currStr = MegaMinxAsString(current)

        # if it is solved break we did it yay
        if isSolved(current):
            break

        # not solved we got to continue
        else:

            # Get all the next moves, and add
            neighbors = nextMoves(current)
            numExpanded = numExpanded + 12

            # dive into each neighbor node in detail
            for next in neighbors:
                # add one to the cost, and get the megaminx as string
                newCost = costSoFar[currStr] + 1
                nextStr = MegaMinxAsString(next)

                # if not in dictionaries or the cost is lower than a previously found cost
                if nextStr not in costSoFar or newCost < costSoFar[nextStr]:
                    # add this cost to dictionary
                    costSoFar[nextStr] = newCost
                    # computer priority with heurisitc
                    priority = newCost + heuristic(next)
                    # make new node
                    n = Node(next, priority)
                    # add which one is moved
                    n.addCounter(neighbors.index(next))
                    n.addClockwise(neighbors.index(next))

                    # put in queue and put in parent dictionary, along with information on the move
                    queue.put(n)
                    parent[nextStr] = [MegaMinxAsString(current), neighbors.index(next)]


    # get path to solve
    pathToSolve = []
    startString = "AAAAAAAAAAAΒΒΒΒΒΒΒΒΒΒΒΓΓΓΓΓΓΓΓΓΓΓΔΔΔΔΔΔΔΔΔΔΔΕΕΕΕΕΕΕΕΕΕΕΖΖΖΖΖΖΖΖΖΖΖΗΗΗΗΗΗΗΗΗΗΗΘΘΘΘΘΘΘΘΘΘΘΙΙΙΙΙΙΙΙΙΙΙΚΚΚΚΚΚΚΚΚΚΚΛΛΛΛΛΛΛΛΛΛΛΜΜΜΜΜΜΜΜΜΜΜ"
    nextStr = startString
    newMegaMinx = []
    # Put intial values in megaminx, based off greek alphabet
    for i in "AΒΓΔΕΖΗΘΙΚΛΜ":
        temp = side(i)
        newMegaMinx.append(temp)

    newMegaMinx[0].addrelations([newMegaMinx[1], newMegaMinx[2], newMegaMinx[3], newMegaMinx[4], newMegaMinx[5]])
    newMegaMinx[1].addrelations([newMegaMinx[0], newMegaMinx[5], newMegaMinx[7], newMegaMinx[11], newMegaMinx[2]])
    newMegaMinx[2].addrelations([newMegaMinx[3], newMegaMinx[0], newMegaMinx[1], newMegaMinx[11], newMegaMinx[10]])
    newMegaMinx[3].addrelations([newMegaMinx[9], newMegaMinx[4], newMegaMinx[0], newMegaMinx[2], newMegaMinx[10]])
    newMegaMinx[4].addrelations([newMegaMinx[9], newMegaMinx[8], newMegaMinx[5], newMegaMinx[0], newMegaMinx[3]])
    newMegaMinx[5].addrelations([newMegaMinx[4], newMegaMinx[8], newMegaMinx[7], newMegaMinx[1], newMegaMinx[0]])
    newMegaMinx[6].addrelations([newMegaMinx[7], newMegaMinx[8], newMegaMinx[9], newMegaMinx[10], newMegaMinx[11]])
    newMegaMinx[7].addrelations([newMegaMinx[6], newMegaMinx[11], newMegaMinx[1], newMegaMinx[5], newMegaMinx[8]])
    newMegaMinx[8].addrelations([newMegaMinx[9], newMegaMinx[6], newMegaMinx[7], newMegaMinx[5], newMegaMinx[4]])
    newMegaMinx[9].addrelations([newMegaMinx[3], newMegaMinx[10], newMegaMinx[6], newMegaMinx[8], newMegaMinx[4]])
    newMegaMinx[10].addrelations([newMegaMinx[3], newMegaMinx[2], newMegaMinx[11], newMegaMinx[6], newMegaMinx[9]])
    newMegaMinx[11].addrelations([newMegaMinx[10], newMegaMinx[2], newMegaMinx[1], newMegaMinx[7], newMegaMinx[6]])

    # backtrace through dictionary for path
    while (startString != megaStringstart):
        move = parent[nextStr]
        if move == None:
            break
        else:
            move = move[1]
        pathToSolve.append(move)
        newMegaMinx[move].rotateClock()
        nextStr = MegaMinxAsString(newMegaMinx)

    #print the path and return the path
    print("Path to solve:")
    for i in reversed(pathToSolve):
        print("Rotate Side #:", i)
    print("Number of nodes expanded:")
    print(numExpanded)
    pathToSolve.reverse()
    return pathToSolve






def nextMoves(current):
    #CREATE 12 COMPLETLY NEW MEGAMINX WITH SAME LAYOUT, MINUS ONE SIDE CHANGE
    nextMoves = []
    for i in current:
        i.rotateCounter()
        cop = createNewMegaMinx(current)
        nextMoves.append(cop)
        i.rotateClock()
    return nextMoves

# make
def MegaMinxAsString(megaminx):
    string = ""
    for side in megaminx:
        for i in side.listofMovable:
            string = string + i
        string = string + side.center
    return string


# heuristic is based off number out of place ceiling 10
def heuristic(megaminx):
    count = 0
    for sides in megaminx:
        for out in sides.listofMovable:
            if (out != sides.center):
                count = count + 1
    heur = floor(count/10.0)
    return heur

# finds out if every side is solved
def isSolved(megaminx):
    for sides in megaminx:
        for out in sides.listofMovable:
            if (out != sides.center):
                return False
    return True
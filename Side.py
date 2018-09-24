class side:
    def __init__(self, color, listofRelates=None, Movable = None):
        if Movable == None:
            self.listofMovable = list()
            counter = 1
            for i in range(0, 10):
                self.listofMovable.append(color)
                counter = counter + 1
        else:
            self.listofMovable = Movable
        self.center = color
        self.listofrelates = listofRelates



    def addrelations(self, listofRelates):
        self.listofrelates = listofRelates

    def display(self):
        print("     ", self.listofMovable[0], self.listofMovable[1] , self.listofMovable[2])
        print("  ", self.listofMovable[9], "       ", self.listofMovable[3])
        print(self.listofMovable[8], "     ", self.center,"     ", self.listofMovable[4])
        print("  ", self.listofMovable[7],"       ", self.listofMovable[5])
        print("       ", self.listofMovable[6])

    def rotateClock(self):
        temp = self.listofMovable.copy()
        for i in range(0,8):
            self.listofMovable[i+2] = temp[i]
        self.listofMovable[0] = temp[8]
        self.listofMovable[1] = temp[9]

        copy = self.listofrelates[0].listofMovable.copy()
        copy2 = self.listofrelates[1].listofMovable.copy()
        copy3 = self.listofrelates[2].listofMovable.copy()
        copy4 = self.listofrelates[3].listofMovable.copy()
        copy5 = self.listofrelates[4].listofMovable.copy()
        self.listofrelates[1].listofMovable[8] = copy3[6]
        self.listofrelates[1].listofMovable[9] = copy3[7]
        self.listofrelates[1].listofMovable[0] = copy3[8]

        self.listofrelates[2].listofMovable[6] = copy4[4]
        self.listofrelates[2].listofMovable[7] = copy4[5]
        self.listofrelates[2].listofMovable[8] = copy4[6]

        self.listofrelates[3].listofMovable[4] = copy5[2]
        self.listofrelates[3].listofMovable[5] = copy5[3]
        self.listofrelates[3].listofMovable[6] = copy5[4]

        self.listofrelates[4].listofMovable[2] = copy[0]
        self.listofrelates[4].listofMovable[3] = copy[1]
        self.listofrelates[4].listofMovable[4] = copy[2]

        self.listofrelates[0].listofMovable[0] = copy2[8]
        self.listofrelates[0].listofMovable[1] = copy2[9]
        self.listofrelates[0].listofMovable[2] = copy2[0]

    def rotateCounter(self):
        temp = self.listofMovable.copy()
        for i in range(0, 8):
            self.listofMovable[i] = temp[i+2]
        self.listofMovable[8] = temp[0]
        self.listofMovable[9] = temp[1]

        copy = self.listofrelates[0].listofMovable.copy()
        copy2 = self.listofrelates[1].listofMovable.copy()
        copy3 = self.listofrelates[2].listofMovable.copy()
        copy4 = self.listofrelates[3].listofMovable.copy()
        copy5 = self.listofrelates[4].listofMovable.copy()
        self.listofrelates[1].listofMovable[8] = copy[0]
        self.listofrelates[1].listofMovable[9] = copy[1]
        self.listofrelates[1].listofMovable[0] = copy[2]

        self.listofrelates[2].listofMovable[6] = copy2[8]
        self.listofrelates[2].listofMovable[7] = copy2[9]
        self.listofrelates[2].listofMovable[8] = copy2[0]

        self.listofrelates[3].listofMovable[4] = copy3[6]
        self.listofrelates[3].listofMovable[5] = copy3[7]
        self.listofrelates[3].listofMovable[6] = copy3[8]

        self.listofrelates[4].listofMovable[2] = copy4[4]
        self.listofrelates[4].listofMovable[3] = copy4[5]
        self.listofrelates[4].listofMovable[4] = copy4[6]

        self.listofrelates[0].listofMovable[0] = copy5[2]
        self.listofrelates[0].listofMovable[1] = copy5[3]
        self.listofrelates[0].listofMovable[2] = copy5[4]

    def displayUpsidedown(self):
        print("       ", self.listofMovable[6])
        print("  ", self.listofMovable[5],"       ", self.listofMovable[7])
        print(self.listofMovable[4], "     ", self.center,"     ", self.listofMovable[8])
        print("  ", self.listofMovable[3], "       ", self.listofMovable[9])
        print("     ", self.listofMovable[2], self.listofMovable[1] , self.listofMovable[0])


    def displayRelations(self):
        print("Displaying all affected sides:")
        print("Side called on:")
        self.display()
        counter = 1
        for i in self.listofrelates:
            print("Side", counter)
            i.displayUpsidedown()
            counter = counter + 1

    def getMovable(self):
        return self.listofMovable





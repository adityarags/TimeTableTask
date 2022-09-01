import pickle
ALLSLOTS = []
class Slot():
    def __init__(self):

        '''
        self.ccode = ""
        self.cname = ""
        self.type = ""
        self.credit = 0
        fno = 0
        self.slots = []
        self.seats = 0
        self.getvals()
        '''
        self.getvals()
    
    def getvals(self):
        self.ccode = input("Enter Course Code: ")
        self.cname = input("Enter Course Name: ")
        self.type = input("Enter Course Type: ")
        self.credit = int(input("Enter Course Credits: "))
        self.fno = int(input("Enter Faculty Number: "))
        self.slots = input("Enter slots: ").split()
        self.seats = int(input("Number of seats: "))
        
    
    def load(self, filename):
        self = open(filename).read()
    
    def __str__(self):
        joinedslots = "+".join(self.slots)
        return f"{self.cname} course with {self.ccode} course code taken up by {self.fno} in {joinedslots} slots with {self.seats} seats"


def storeData(filename):
    f = open(filename, "wb")
    pickle.dump(ALLSLOTS, f)

def loadData(filename):
    global ALLSLOTS
    ALLSLOTS = pickle.load(open(filename, "rb"))

def getData():
    n = int(input("Number of slots: "))
    for i in range(n):
        ALLSLOTS.append(Slot())

def displayData():
    for _ in ALLSLOTS:
        print(_)

if __name__ == "__main__":
    # getData()
    # storeData("actdata/sampledata.dat")
    loadData("actdata/sampledata.dat")
    displayData()


class Movables():
    name = ""
    state = "left"

    def __init__(self, name):
        self.name = name

    def move(self, state):
        if state == "left":
            self.state = "right"
        else:
            self.state == "left"

    def getName(self):
        return self.name

    def getState(self):
        return self.state



class PrintToCLI():
    @staticmethod
    def printAll(list):
        left = ""
        right = ""
        for Objects in list:
            if Objects.state == "left":
                left += Objects.name
            elif Objects.state == "right":
                right += Objects.name
        print(left + "||" + right)


class UsefullMethods():
    @staticmethod
    def getsEaten(o1, o2):
        if o1.name == "G" and o2.name == "C":
            return True
        elif o1.name == "W" and o2.name == "G":
            return True
        else: return False

    @staticmethod
    def checkGoalState(list):
        for Objects in list:
            if Objects.state == "left":
                return False



class Main():
    objectList = []

    objectList.append(Movables("F"))
    objectList.append(Movables("C"))
    objectList.append(Movables("G"))
    objectList.append(Movables("W"))

    UsefullMethods.getsEaten(objectList.__getitem__(0), objectList.__getitem__(2))

    UsefullMethods.checkGoalState(objectList)

    PrintToCLI.printAll(objectList)

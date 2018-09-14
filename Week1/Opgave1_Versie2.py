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

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state



class PrintToCLI():
    @staticmethod
    def print_all(list):
        left = ""
        right = ""
        for o in list:
            if o.state == "left":
                left += o.name
            elif o.state == "right":
                right += o.name
        print(left + "||" + right)


class UsefullMethods():
    @staticmethod
    def gets_eaten(o1, o2):
        if o1.name == 'G' and o2.name == 'C':
            return True
        elif o1.name == 'W' and o2.name == 'G':
            return True
        else: return False

    @staticmethod
    def check_goal_state(list):
        for o in list:
            if o.state == "left":
                return False



class Main():
    object_list = []

    object_list.append(Movables("F"))
    object_list.append(Movables("C"))
    object_list.append(Movables("G"))
    object_list.append(Movables("W"))

    UsefullMethods.gets_eaten(object_list.__getitem__(0), object_list.__getitem__(2))

    UsefullMethods.check_goal_state(object_list)

    PrintToCLI.print_all(object_list)

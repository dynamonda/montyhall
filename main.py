""" Monty Hall Problem """
import random

class Door:
    """ Door """
    def __init__(self):
        self.answer = False
        self.opened = False

    def set_answer(self):
        """ set True to answer """
        self.answer = True    

class Field:
    """ Doors have many door """
    def __init__(self, dnum):
        self.doors = list()
        for _ in range(dnum):
            self.doors.append(Door())
        self.doors[random.randrange(dnum)].set_answer()
        self.selected = -1

    def select_door(self, index):
        """ select index door """
        self.selected = index
    
    def open_door(self):
        """ open incorrect and not selected door """
        for i in range(len(self.doors)):
            if (not self.doors[i].answer) and (not i is self.selected):
                self.doors[i].opened = True
                print("open incorrect door {0}".format(i))
                break
    
    def change_selected_door(self):
        """ change selected door """
        for i in range(len(self.doors)):
            if (not self.doors[i].opened) and (not i is self.selected):
                print("change {0} to {1}".format(self.selected, i))
                self.selected = i
                break

    def check_answer(self):
        """ check answer """
        if self.doors[self.selected].answer:
            print("Correct Answer!")
            return True
        else:
            print("Incorrect Answer...")
            return False

def main():
    """ main function """
    print("Monty Hall Simulator")
    correct_num = 0
    incorrect_num = 0
    for num in range(1,101):
        print("Round {0}".format(num))
        field = Field(3)
        select_id = random.randrange(3)
        field.select_door(select_id)
        print("select {0} door".format(select_id))
        field.open_door()
        #field.change_selected_door()
        if field.check_answer():
            correct_num += 1
        else:
            incorrect_num += 1
        print()
    print()
    print("Correct:{0}, Incorrect:{1}".format(correct_num, incorrect_num))

main()

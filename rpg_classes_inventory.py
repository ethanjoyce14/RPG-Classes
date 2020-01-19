# Ethan Joyce
# Ms Cotcher
# 2020/01/15
# CS30
# RPG Classes

import rpg_classes_map


# Inventory items
items = ['wallet']


class Inventory:
    """
    A class for all inventory access options
    """
    def __init__(self, enable):
        self.enable = enable

    def inv_rm1(self):
        # Inventory access for room 1
        for item in items:
            print(item)
        response = input("Input 'back' to go back.\n")
        if response == 'back':
            rpg_classes_map.game.move_rm1()
        else:
            print("Input invalid\n")
            self.inv_rm1()

    def inv_rm2(self):
        # Inventory access for room 2
        for item in items:
            print(item)
        response = input("Input 'back' to go back.\n")
        if response == 'back':
            rpg_classes_map.game.move_rm2()
        else:
            print("Input invalid\n")
            self.inv_rm2()

    def inv_rm3(self):
        # Inventory access for room 3
        for item in items:
            print(item)
        response = input("Input 'back' to go back.\n")
        if response == 'back':
            rpg_classes_map.game.move_rm3()
        else:
            print("Input invalid\n")
            self.inv_rm3()

    def inv_rm4(self):
        # Inventory access for room 4
        for item in items:
            print(item)
        response = input("Input 'back' to go back.\n")
        if response == 'back':
            rpg_classes_map.game.move_rm4()
        else:
            print("Input invalid\n")
            self.inv_rm4()

    def inv_start(self):
        # Inventory access for starting room
        for item in items:
            print(item)
        response = input("Input 'back' to go back.\n")
        if response == 'back':
            rpg_classes_map.game.start_room()
        else:
            print("Input invalid\n")
            self.inv_start()


inv = Inventory(1)

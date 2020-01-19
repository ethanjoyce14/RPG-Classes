# Ethan Joyce
# Ms Cotcher
# 2020/01/15
# CS30
# RPG Classes


import rpg_classes_inventory

# List of available pickups in room 4
pickups_rm4 = ['key']


class Room:
    """
    A class for all room descriptions
    """
    def __init__(self, desc):
        self.desc = desc


# All rooms and their descriptions
starting_room = Room("You wake up to find yourself in a strange office with" +
                     " papers scattered everywhere.\n")
room_1 = Room("A strange office with papers scattered everywhere.\n")
room_2 = Room("What looks to be a surgical theatre. Traces of blood are" +
              " everywhere.\n")
room_3 = Room("An equipment room. Much of the surgical tools are gone. There" +
              " is a door in the corner.\n")
room_4 = Room("A storage closet. A lone broom stands in the corner. There is" +
              " a key hanging on the wall.\n")


class Room_move:
    """
    A class for all room movement and options
    """
    def __init__(self, enable):
        self.enable = enable

    def start_room(self):
        # Starting room
        print(starting_room.desc)
        directions = ['up', 'right']
        for direction in directions:
            print(direction)
        # Movement options
        response = input("\nWhat direction would you like to move? Input" +
                         " 'inv' for inventory.\n")
        if response == 'up':
            print(room_4.desc)
            self.move_rm4()
        elif response == 'right':
            print(room_2.desc)
            self.move_rm2()
        elif response == 'inv':
            rpg_classes_inventory.inv.inv_start()
        else:
            print("Invalid input\n")
            self.move_rm1()

    def move_rm1(self):
        # Room 1, same as starting room
        directions = ['up', 'right']
        for direction in directions:
            print(direction)
        # Movement options
        response = input("\nWhat direction would you like to move? Input" +
                         " 'inv' for inventory.\n")
        if response == 'up':
            print(room_4.desc)
            self.move_rm4()
        elif response == 'right':
            print(room_2.desc)
            self.move_rm2()
        elif response == 'inv':
            rpg_classes_inventory.inv.inv_rm1()
        else:
            print("Invalid input\n")
            self.move_rm1()

    def move_rm2(self):
        # Room 2
        directions = ['up', 'left']
        for direction in directions:
            print(direction)
        # Movement options
        response = input("\nWhat direction would you like to move? Input" +
                         " 'inv' for inventory.\n")
        if response == 'up':
            print(room_3.desc)
            self.move_rm3()
        elif response == 'left':
            print(room_1.desc)
            self.move_rm1()
        elif response == 'inv':
            rpg_classes_inventory.inv.inv_rm2()
        else:
            print("Invalid input\n")
            self.move_rm2()

    def move_rm3(self):
        # Room 3
        directions = ['down', 'left']
        for direction in directions:
            print(direction)
        # Movement options
        response = input("\nWhat direction would you like to move? Input" +
                         " 'inv' for inventory, 'open' to check the door.\n")
        if response == 'down':
            print(room_2.desc)
            self.move_rm2()
        elif response == 'left':
            print(room_4.desc)
            self.move_rm4()
        elif response == 'inv':
            rpg_classes_inventory.inv.inv_rm3()
        elif response == 'open':
            if 'key' in rpg_classes_inventory.items:
                print("You exit the building. You've escaped." +
                      " That was easy.\n")
                quit()
            else:
                print("It's locked.\n")
                self.move_rm3()
        else:
            print("Invalid input\n")
            self.move_rm3()

    def move_rm4(self):
        # Room 4
        directions = ['down', 'right']
        for direction in directions:
            print(direction)
        # Movement options
        response = input("\nWhat direction would you like to move? Input" +
                         " 'inv' for inventory, 'pickup' to take key.\n")
        if response == 'down':
            print(room_1.desc)
            self.move_rm1()
        elif response == 'right':
            print(room_3.desc)
            self.move_rm3()
        elif response == 'inv':
            rpg_classes_inventory.inv.inv_rm4()
        elif response == 'pickup':
            if 'key' not in rpg_classes_inventory.items:
                rpg_classes_inventory.items.append('key')
                pickups_rm4.remove('key')
                print("You pickup the key\n")
                self.move_rm4()
            else:
                print("You've already picked up the key\n")
                self.move_rm4()
        else:
            print("Invalid input\n")
            self.move_rm4()


game = Room_move(1)

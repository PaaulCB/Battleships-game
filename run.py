from pprint import pprint
from random import randint

class Ship():
    """
    Creates an instance of Ship
    """
    def __init__(self, coordinates):
        self.coordinates = coordinates


class BigShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 1


class MediumShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 2


class SmallShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 3


class Board():
    """
    Creates an instance of Board
    """
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.ships = []
        self.misses = []
        self.sunked = []


    def print(self):
        """
        Prints the board separeted by an empty space to the terminal
        """
        for row in self.board:
            print(" ".join(row))


    def guess(self, x, y):
        """
        Iterate through the coordinates of the ships in the ships attribute and  
        if the guess its correct changes all the coordinates of the hitted ship, 
        add the coordenates to the sunked attribute, remove the ship from
        the ships attribute and return "Hit".
        If not, mark the guess as fail, add the guess to the misses attribute and return "Miss"
        """
        for ship in self.ships:
            if [x, y] in ship.coordinates:
                for coordinate in ship.coordinates:
                    self.board[coordinate[0]][coordinate[1]] = "\u00D8"
                    self.sunked.append(coordinate)
                self.ships.remove(ship)
                return "Hit"
        self.board[x][y] = "X"
        self.misses.append([x, y])
        return "Miss"

    def add_ship(self, ship):
        """
        Add ships to the board.
        If the type it's "Player" shows the ship on the board.
        """
        self.ships.append(ship)
        if self.type == "Player":
            for i in ship.coordinates:
                self.board[i[0]][i[1]] = "O"

def random_coordinate(size, type):
    """
    Return a random coordinate accordly to the size and type.
    The type variable avoid getting a coordinate that are off the board 
    for mediums and big ships.
    """
    if (type == 1):
        return [randint(0, size - 1),randint(0, size - 1)]
    elif (type == 2):
        return [randint(0, size - 2),randint(0, size - 2)]
    elif (type == 3):
        return [randint(0, size - 3),randint(0, size - 3)]


def get_invalid_ship_position(board):
    """
    Return a list with the coordenates of the ships that are on the board
    """
    invalid_coordinates = []
    for ship in board.ships:
        for coordinate in ship.coordinates: 
            invalid_coordinates.append(coordinate)
    return invalid_coordinates


def generate_ships(board, quantity, type):
    """
    Generate ships on empty coordinates and add them to the board current ships.
    The quantity variable it's use generate x numbers of ships.
    The type it's used to generate the differents type of ships
    1=small 2=medium 3=big
    """
    for i in range(0, quantity):
        #Get the coordinates that are already taken
        invalid_coordinates = get_invalid_ship_position(board)
        invalid=True
        while invalid :
            invalid=False
            #generate a random coordinate for the ship type
            coordinate = random_coordinate(board.size, type)
            ship_coordinates=[]
            for x in range(coordinate[0],coordinate[0]+type):
                for y in range(coordinate[1],coordinate[1]+type):
                    if [x, y] in invalid_coordinates:
                        #if the coordinate it's already taken break the loop
                        invalid=True
                        break
                    ship_coordinates.append([x, y])
            if invalid:
                continue
            #Depending on the type creates a new instance of Small, Medium or BigShip
            if (type == 1):
                new_ship = SmallShip(ship_coordinates)
            elif (type == 2):
                new_ship = MediumShip(ship_coordinates)
            elif (type == 3):
                new_ship = BigShip(ship_coordinates)
            #Add the new ship to the current board ships 
            board.add_ship(new_ship)

#testing data
test = Board("Paul","Player", 10)
generate_ships(test, 2, 3)
generate_ships(test, 5, 2)
generate_ships(test, 1, 1)
test.guess(4,5)
test.guess(5,5)
test.guess(2,2)
print("Sunked----------------------")
pprint(test.sunked)
test.print()
print(f"Misses\n{test.misses}")
pprint(test.ships)


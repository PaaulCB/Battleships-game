from pprint import pprint


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

#testing data
test = Board("Paul","Player", 8)
ship1=BigShip([[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])
ship2=MediumShip([[3,3],[3,4],[4,3],[4,4]])
ship3=SmallShip([[5,5]])
test.add_ship(ship1)
test.add_ship(ship2)
test.add_ship(ship3)
test.print()
pprint(test.ships)
test.guess(4,5)
test.guess(5,5)
test.guess(2,2)
pprint(test.sunked)
test.print()
print(f"Misses\n{test.misses}")
pprint(test.ships)
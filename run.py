from pprint import pprint
from random import randint
#Constant that stores the number of ships and turns for every board size
GAME_SETTINGS = [
    {"size":4, "small_ships":2, "medium_ships":0, "big_ships":0, "turns":10},
    {"size":5, "small_ships":3, "medium_ships":1, "big_ships":0, "turns":15},
    {"size":6, "small_ships":4, "medium_ships":2, "big_ships":0, "turns":20},
    {"size":7, "small_ships":5, "medium_ships":2, "big_ships":1, "turns":30},
    {"size":8, "small_ships":6, "medium_ships":2, "big_ships":2, "turns":40},
    {"size":9, "small_ships":7, "medium_ships":3, "big_ships":2, "turns":50},
    {"size":10, "small_ships":8, "medium_ships":3, "big_ships":3, "turns":60}
]


class Game():
    """
    Creates an instance of Game
    """
    def __init__(self, turns, name):
        self.turns = turns
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
    

    def print_scores(self):
        """Prints the scores"""
        print(f"{self.player_name}: {self.player_score} Computer: {self.computer_score}")


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
    The quantity variable it's used to generate x numbers of ships.
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


def get_settings(size):
    """
    Return a diccionary with the game settings depending on the size variable
    """
    for settings in GAME_SETTINGS:
        if settings["size"] == size:
            return settings


def populate_board(board):
    """
    Popupate the board accordly to the size using the GAME_SETTINGS constant
    """
    settings = get_settings(board.size)
    generate_ships(board, settings["big_ships"], 3)#Big ships
    generate_ships(board, settings["medium_ships"], 2)#Medium ships
    generate_ships(board, settings["small_ships"], 1)#Small ships


def get_guess():
    """
    Asks for a row and a column to guess and return it in a list
    """
    y = input("Introduce a column to guess\n")
    x = input("Introduce a row to guess\n")
    
    return [x, y]


def print_boards(player_board, computer_board):
    """
    Prints the boards passed as parameters
    """
    print(f"\n{player_board.name}'s Board")
    player_board.print()
    print(f"\n{computer_board.name}'s Board")
    computer_board.print()

def play_round(player_board, computer_board):
    """
    Play a round of the game
    """
    guess = get_guess()
    random_guess = random_coordinate(player_board.size, 1)
    computer_board.guess(int(guess[0]),int(guess[1]))
    player_board.guess(int(random_guess[0]),int(random_guess[1]))
    print_boards(player_board, computer_board)

def play_game(player_board, computer_board):
    """
    Play the game
    """
    game_over = False
    while(not game_over):
        play_round(player_board, computer_board)
        if not player_board.ships or not computer_board.ships:
            game_over = True
    print("game over")


def new_game():
    print("Welcome to Battleships Game\n")
    name = input("Please introduce your name\n")
    size = int(input("Please introduce the size of the board (options availables 4-10)\n"))
    turns = get_settings(size)["turns"]
    game = Game(turns, name)
    game.print_scores()
    player_board = Board(name, "Player", size)
    computer_board = Board("Computer", "Player", size)#Change Player to computer after testings
    populate_board(player_board)
    populate_board(computer_board)
    print_boards(player_board,computer_board)
    play_game(player_board,computer_board)
    
    

new_game()

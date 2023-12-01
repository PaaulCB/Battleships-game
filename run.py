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


    def increment_score(self, type, value):
        """
        Increments player or computer score
        """
        if(type == "Player"):
            self.player_score += value
        else:
            self.computer_score += value

    def turns_remaining(self):
        """
        Prints the turns remaining
        """
        print(f"Turns remaining: {self.turns}")


class Ship():
    """
    Creates an instance of Ship
    """
    def __init__(self, coordinates):
        self.coordinates = coordinates


    def get_type(self):
        """
        Returns the type of the ship
        """
        return self.type
    
    
    def get_value(self):
        """
        Returns the value of the ship
        """
        return self.value

class BigShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 1
        self.type = "big ship"


class MediumShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 2
        self.type = "medium ship"


class SmallShip(Ship):
    """
    Subclass of the superclass Ship
    """
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.value = 3
        self.type = "small ship"


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
        Also shows the column and row numbers
        """
        column_num = "  "
        for i in range(self.size):
            column_num += f"{i} "
        print(column_num) 
        for i, row in enumerate(self.board):
            row_to_print = " ".join(row)
            print(f"{i} {row_to_print}")


    def guess(self, x, y, game):
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
                type = ship.get_type()
                value = ship.get_value()
                if(self.type == "Player"):
                    game.increment_score("Computer",value)
                else:
                    game.increment_score("Player",value)
                self.ships.remove(ship)
                return f"hit a {type} and gains {value} points"
        self.board[x][y] = "X"
        self.misses.append([x, y])
        return "miss the shot"

    def add_ship(self, ship):
        """
        Add ships to the board.
        If the type it's "Player" shows the ship on the board.
        """
        self.ships.append(ship)
        #commented for testings
        #if self.type == "Player":
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


def print_boards(player_board, computer_board):
    """
    Prints the boards passed as parameters
    """
    print(f"\n{player_board.name}'s Board")
    player_board.print()
    print(f"\n{computer_board.name}'s Board")
    computer_board.print()


def get_winner(game):
    """
    Prints the winner
    """
    if(game.player_score == game.computer_score):
        print("It's a tie")
    elif(game.player_score > game.computer_score):
        print(f"{game.player_name} wins")
    else:
        print("Computer wins")



def decrease_turns(game):
    """
    Decrease the turns of the game by 1
    """
    game.turns -= 1


def validate_name(name):
    """
    Returns False if the name it's empty, contains invalid characters or
    if doesn't have between 4-11 characters. Also prints a descriptive error.
    Otherwise return True.
    """
    try:
        if not name:#Checks if name it's empty
            raise ValueError("Username cannot be empty.")
        
        for c in name:#Checks all the characthers are digit, letter or space.
            if c.isalpha() or c.isspace() or c.isdigit():
                continue
            else:
                raise ValueError("Username only can contain letters, digits or spaces")

        if len(name) < 4:#Checks if name has less then 4 characters
            raise ValueError("Username too short.")
        elif len(name) > 11:#Checks if name has more then 11 characters
            raise ValueError("Username too long.")
        return True#If any error has been triggered return True

    except ValueError as e:
        print(f"\n{e}")#Prints the error and return False
        return False


def get_name():
    """
    Returns name after checking if it's valid with the validate_name() function
    """
    name = input("Please introduce your username (4-11 characters)\n")
    while True:#Infinte loop
        if validate_name(name):
            break#Break the loop if the name it's valid
        else:#Asks fot the name again
            name = input("Please introduce a valid username (4-11 characters)\n")
    return name#Returns name when it's valid


def validate_size(size):
    """
    Returns False if the size it's empty, or
    if is not between 4-11. Also prints a descriptive error.
    Otherwise return True.
    """
    try:
        if not size:#Checks if size it's empty
            raise ValueError("Size cannot be empty.")

        if int(size) < 4 or int(size) > 11:#Checks if size it's between 4-11
            raise ValueError("Invalid size option")
        
        return True#If any error has been triggered return True

    except ValueError as e:
        print(f"\n{e}")#Prints the error and return False
        return False
            

def get_size():
    """
    Returns size converted to integer after checking 
    if it's valid with the validate_size() function
    """
    size = input("\nPlease introduce the size of the board (options availables 4-10)\n")
    while True:#Infinte loop
        if validate_size(size):
            break#Break the loop if the size it's valid
        else:#Asks for the size again
            size = input("Please introduce a valid size (options availables 4-10)\n")
    return int(size)#Returns size when it's valid


def is_invalid(coordinate, invalid):
    """
    Returns True if coordinate is on invalid otherwise return False
    """
    if coordinate in invalid:
        return True
    else:
        return False


def validate_guess(x, y, board):
    """
    Returns False if x or y are empty, if they are not digits
    or if they are not between 0 and board.size -1. 
    Also prints a descriptive error.
    Otherwise return True.
    """
    try:
        if not x or not y:#Check if x or y are empty
            raise ValueError("Row and column cannot be empty.")

        if not x.isdigit() or not y.isdigit():#Checks if x or y are digits
            raise TypeError("Row and column must be intenger numbers.")
        
        if int(x) < 0 or int(x) > board.size - 1:#Checks if x has a valid range 
            raise ValueError(f"Row and column must be between 0 - {board.size - 1}.")
        
        if int(y) < 0 or int(y) > board.size - 1:#Checks if y has a valid range 
            raise ValueError(f"Row and column must be between 0 - {board.size - 1}.") 
        if is_invalid([int(x), int(y)] , board.sunked):
            raise ValueError(f"You have already sunk a ship on [{x}, {y}]") 
        if is_invalid([int(x), int(y)] , board.misses):
            raise ValueError(f"You have already missed a shot on [{x}, {y}]")

        return True#If any error has been triggered return True

    except ValueError as e:
        print(f"\n{e}")#Prints the error and return False
        return False 
    except TypeError as e:
        print(f"\n{e}")#Prints the error and return False
        return False

def get_guess(board):
    """
    Asks for a row and a column,validate it with validate_guess function
    and returns it in a list.
    """
    y = input("Introduce a column to guess\n")
    x = input("Introduce a row to guess\n")
    while True:
        if validate_guess(x, y ,board):
            break
        else:
            y = input("Introduce a valid column to guess\n")
            x = input("Introduce a valid row to guess\n")
    return [x, y]


def get_computer_guess(board):
    """
    Generate a random coordinate with the function random_coordinate until it's valid. 
    """
    invalid = board.sunked+board.misses
    while True:
        guess=random_coordinate(board.size, 1)
        if guess in invalid:
            continue
        else:
            break
    return guess
        

def play_round(player_board, computer_board, game):
    """
    Play a round of the game
    """
    guess = get_guess(computer_board)
    random_guess = get_computer_guess(player_board)
    print("\n"+"*"*30)
    print(f"{player_board.name} {computer_board.guess(int(guess[0]),int(guess[1]),game)}")
    print(f"{computer_board.name} {player_board.guess(int(random_guess[0]),int(random_guess[1]),game)}")
    decrease_turns(game)
    game.turns_remaining()
    print("--Current scores--")
    game.print_scores()
    print_boards(player_board, computer_board)
    print("*"*30+"\n")


def play_game(player_board, computer_board, game):
    """
    Play the game
    """
    settings=get_settings(player_board.size)
    print("\n\n"+"-"*30)
    print(f"Turns limit for the game: {game.turns}")
    print("Each board has:\n")
    print(f"{settings['small_ships']} Small ships with a value of 3 points each")
    print(f"{settings['medium_ships']} Medium ships with a value of 2 points each")
    print(f"{settings['big_ships']} Big ships with a value of 1 points each")
    print_boards(player_board,computer_board)
    print("\nGood Luck!")
    print("-"*30+"\n\n")
    game_over = False
    while(not game_over):
        play_round(player_board, computer_board, game)
        if (not player_board.ships or not computer_board.ships) or game.turns == 0:
            game_over = True
    game.print_scores()
    get_winner(game)


def new_game():
    print("-"*30)
    print("Welcome to Battleships Game!")
    print("Press enter to start")
    print("-"*30)
    input("")
    name = get_name()
    size = get_size()
    turns = get_settings(size)["turns"]
    game = Game(turns, name)
    player_board = Board(name, "Player", size)
    computer_board = Board("Computer", "Computer", size)
    populate_board(player_board)
    populate_board(computer_board)
    play_game(player_board,computer_board, game)
    
    

new_game()

from random import randint
# Constant that stores the number of ships and turns for every board size
GAME_SETTINGS = [
    {"size": 4, "small_ship": 2, "medium_ship": 0, "big_ship": 0, "turns": 10},
    {"size": 5, "small_ship": 3, "medium_ship": 1, "big_ship": 0, "turns": 15},
    {"size": 6, "small_ship": 4, "medium_ship": 2, "big_ship": 0, "turns": 20},
    {"size": 7, "small_ship": 5, "medium_ship": 2, "big_ship": 1, "turns": 25},
    {"size": 8, "small_ship": 6, "medium_ship": 2, "big_ship": 2, "turns": 35},
    {"size": 9, "small_ship": 7, "medium_ship": 3, "big_ship": 2, "turns": 40},
    {"size": 10, "small_ship": 8, "medium_ship": 3, "big_ship": 3, "turns": 50}
]


class Game():
    """
    Creates an instance of Game
    """
    def __init__(self, turns, name, player_board, computer_board):
        self.turns = turns
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        self.player_board = player_board
        self.computer_board = computer_board

    def print_scores(self):
        """
        Prints the scores
        """
        print(
            f"{self.player_name}: {self.player_score}"
            f" Computer: {self.computer_score}"
            )

    def increment_score(self, type, value):
        """
        Increments player or computer score
        """
        if type == "Player":
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
        # Code taken from code institute portfolio project 3 scope video
        self.board = [["." for x in range(size)] for y in range(size)]
        self.ships = []
        self.misses = []
        self.sunked = []

    def print(self):
        """
        Prints the board separeted by an empty space to the terminal
        Also shows the column and row numbers
        """
        # Prints the column numbers
        column_num = "  "
        for i in range(self.size):
            column_num += f"{i} "
        print(column_num)
        # Prints the board along with the row numbers
        for i, row in enumerate(self.board):
            row_to_print = " ".join(row)
            print(f"{i} {row_to_print}")

    def guess(self, x, y, game):
        """
        Iterate through the coordinates of the ships in the ships attribute and
        if the guess its correct changes all the coordinates of the hitted ship
        add the coordinates to the sunked attribute, remove the ship from
        the ships attribute and return a hit message.
        If not, mark the guess as fail, add the guess to the misses attribute
        and return a miss message
        """
        # Loops through each ship of the board
        for ship in self.ships:
            # Checks if [x, y] it's on the ship coordinates
            if [x, y] in ship.coordinates:
                # Loops through each coordinate of the ship
                for coordinate in ship.coordinates:
                    # Replaces the coordinate on the board with "\u00D8"
                    self.board[coordinate[0]][coordinate[1]] = "\u00D8"
                    # Adds the coordinate to the sunked attribute
                    self.sunked.append(coordinate)
                # Gets the ship type
                type = ship.get_type()
                # Gets the ship value
                value = ship.get_value()
                # Checks if it's a player or computer board
                if self.type == "Player":
                    # Increments computer score
                    game.increment_score("Computer", value)
                else:
                    # Increments player score
                    game.increment_score("Player", value)
                # Removes the ship form the ships attribute
                self.ships.remove(ship)
                # Returns a hit message
                return f"hit a {type} and gains {value} points"
        # Replaces the coordinate on the board with "X"
        self.board[x][y] = "X"
        # Adds the coordinate to the misses attribute
        self.misses.append([x, y])
        # Returns a miss message
        return "miss the shot"

    def add_ship(self, ship):
        """
        Add ships to the board
        """
        self.ships.append(ship)

    def show_ships(self):
        """
        Show the ships on the board
        """
        for ship in self.ships:
            for i in ship.coordinates:
                self.board[i[0]][i[1]] = "O"


def random_coordinate(size, type):
    """
    Return a random coordinate accordly to the size and type.
    The type variable avoid getting a coordinate that are off the board
    for medium and big ships.
    """
    if (type == 1):
        return [randint(0, size - 1), randint(0, size - 1)]
    elif (type == 2):
        return [randint(0, size - 2), randint(0, size - 2)]
    elif (type == 3):
        return [randint(0, size - 3), randint(0, size - 3)]


def get_invalid_ship_position(board):
    """
    Return a list with the coordinates of the ships that are on the board
    """
    invalid_coordinates = []
    for ship in board.ships:
        for coordinate in ship.coordinates:
            invalid_coordinates.append(coordinate)
    return invalid_coordinates


def generate_ships(board, quantity, type):
    """
    Generate ships on empty coordinates and add them to the board current ships
    The quantity variable it's used to generate x numbers of ships.
    The type it's used to generate the differents type of ships
    1=small 2=medium 3=big
    """
    for i in range(0, quantity):
        # Get the coordinates that are already taken
        invalid_coordinates = get_invalid_ship_position(board)
        invalid = True
        while invalid:
            invalid = False
            # Generates a random coordinate for the ship type
            coordinate = random_coordinate(board.size, type)
            ship_coordinates = []
            for x in range(coordinate[0], coordinate[0]+type):
                for y in range(coordinate[1], coordinate[1]+type):
                    if [x, y] in invalid_coordinates:
                        # If the coordinate it's already taken break the loop
                        invalid = True
                        break
                    ship_coordinates.append([x, y])
            if invalid:
                continue
            # Creates a new instance of Small, Medium or BigShip
            if (type == 1):
                new_ship = SmallShip(ship_coordinates)
            elif (type == 2):
                new_ship = MediumShip(ship_coordinates)
            elif (type == 3):
                new_ship = BigShip(ship_coordinates)
            # Add the new ship to the current board ships
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
    Populates the board accordly to the size using the GAME_SETTINGS constant
    """
    settings = get_settings(board.size)
    generate_ships(board, settings["big_ship"], 3)  # Big ships
    generate_ships(board, settings["medium_ship"], 2)  # Medium ships
    generate_ships(board, settings["small_ship"], 1)  # Small ships


def print_boards(*boards):
    """
    Prints the boards passed as parameters
    """
    for board in boards:
        print(f"\n{board.name}'s Board")
        board.print()


def get_winner(game):
    """
    Prints the winner
    """
    if game.player_score == game.computer_score:
        print("It's a tie")
    elif game.player_score > game.computer_score:
        print(f"{game.player_name} wins!")
    else:
        print("Computer wins!")


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
        if not name:  # Checks if name it's empty
            raise ValueError("Username cannot be empty.")
        # Checks if all the characthers are digit, letter or space.
        for c in name:
            if c.isalpha() or c.isspace() or c.isdigit():
                continue
            else:
                raise ValueError(
                    "Username only can contain letters, digits or spaces"
                    )
        # Checks if name has less then 4 characters
        if len(name) < 4:
            raise ValueError("Username too short.")
        # Checks if name has more then 11 characters
        elif len(name) > 11:
            raise ValueError("Username too long.")

        # Checks if name starts or ends with space
        if name[0].isspace() or name[-1].isspace():
            raise ValueError("Username cannot start or end with a space.")

        previous_was_space = False
        # Checks if there are 2 space in a row.
        for c in name:
            if c.isspace():
                if previous_was_space:
                    raise ValueError(
                        "Username cannot have more than one space in a row"
                        )
                previous_was_space = True
            else:
                previous_was_space = False
        # If none errors has been triggered return True
        return True
    except ValueError as e:
        # Prints the error and return False
        print(f"\n{e}")
        return False


def get_name():
    """
    Returns name after checking if it's valid with the validate_name() function
    """
    name = input("Please introduce your username (4-11 characters)\n")
    while True:  # Infinte loop
        if validate_name(name):
            break  # Break the loop if the name it's valid
        else:  # Asks fot the name again
            name = input(
                "Please introduce a valid username (4-11 characters)\n"
                )
    return name  # Returns name when it's valid


def validate_size(size):
    """
    Returns False if the size it's empty, not positive integer or
    if is not between 4-11. Also prints a descriptive error.
    Otherwise return True.
    """
    try:
        if not size:  # Checks if size it's empty
            raise ValueError("Size cannot be empty.")
        if not size.isdigit():  # Checks if size it's an positive integer
            raise TypeError("Size must be an positive intenger number.")
        if int(size) < 4 or int(size) > 11:  # Checks if size it's between 4-11
            raise ValueError("Invalid size option")

        return True  # If none errors has been triggered return True

    except ValueError as e:
        print(f"\n{e}")  # Prints the error and return False
        return False
    except TypeError as e:
        print(f"\n{e}")  # Prints the error and return False
        return False


def get_size():
    """
    Returns size converted to integer after checking
    if it's valid with the validate_size() function
    """
    size = input(
        "\nPlease introduce the size of the board (options availables 4-10)\n"
        )
    while True:  # Infinte loop
        if validate_size(size):
            break  # Break the loop if the size it's valid
        else:  # Asks for the size again
            size = input(
                "Please introduce a valid size (options availables 4-10)\n"
                )
    return int(size)  # Returns size when it's valid


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
        if not x or not y:  # Check if x or y are empty
            raise ValueError("Row and column cannot be empty.")
        if not x.isdigit() or not y.isdigit():  # Checks if x or y are digits
            raise TypeError("Row and column must be intenger numbers.")
        # Checks if x and y have a valid range
        if not (0 <= int(x) < board.size and 0 <= int(y) < board.size):
            raise ValueError(
                f"Row and column must be between 0 and {board.size - 1}."
                )
        # Checks if it's already a ship sunked on the coordinate
        if is_invalid([int(x), int(y)], board.sunked):
            raise ValueError(f"You have already sunk a ship on [{x}, {y}]")
        # Checks if it's already a ship sunked on the coordinate
        if is_invalid([int(x), int(y)], board.misses):
            raise ValueError(f"You have already missed a shot on [{x}, {y}]")

        return True  # If any error has been triggered return True

    except ValueError as e:
        print(f"\n{e}")  # Prints the error and return False
        return False
    except TypeError as e:
        print(f"\n{e}")  # Prints the error and return False
        return False


def get_guess(board):
    """
    Asks for a row and a column,validate it with validate_guess function
    and returns it in a list.
    """
    y = input("Introduce a column to guess\n")
    x = input("Introduce a row to guess\n")
    while True:
        if validate_guess(x, y, board):
            break
        else:
            y = input("Introduce a valid column to guess\n")
            x = input("Introduce a valid row to guess\n")
    return [x, y]


def get_computer_guess(board):
    """
    Generate a random coordinate with the function random_coordinate
    """
    invalid = board.sunked+board.misses
    while True:
        guess = random_coordinate(board.size, 1)
        if guess in invalid:
            continue
        else:
            break
    return guess


def play_round(game):
    """
    Play a round of the game.
    Gets the player and computer guesses and with the guess method
    checks if the hit or not.
    After that decrease the game turns by one.
    """
    guess = get_guess(game.computer_board)
    # r_guess stands for random guess
    r_guess = get_computer_guess(game.player_board)
    print("\n"+"*"*30)
    print(
        f"{game.player_name} "
        f"{game.computer_board.guess(int(guess[0]), int(guess[1]), game)}"
        )
    print(
        f"Computer "
        f"{game.player_board.guess(int(r_guess[0]), int(r_guess[1]), game)}"
        )
    decrease_turns(game)


def validate_play_again(answer):
    """
    Returns False if answer is empty
    or if it's not "n", "N", "y" or "Y".
    Also prints a descriptive error.
    Otherwise return True.
    """
    try:

        if not answer:  # Checks if answer it's empty
            raise ValueError(
                "Input cannot be empty (Valids inputs: Y, y, N, n)"
                )
        # Checks if the answer has a valid value
        if answer.upper() not in ["Y", "N"]:
            raise ValueError(
                f"{answer} is not a valid input (Valids inputs: Y, y, N, n)"
                )
        return True  # If none errors has been triggered return True
    except ValueError as e:
        print(f"\n{e}")  # Prints the error and return False
        return False


def play_again():
    """
    Checks if the player wants to keep playing
    Ask for "N" or "Y" and after validating if the input it's valid
    if the player introduced "Y" starts a new game
    if introduced "N" prints a thanks for playing messege
    """
    keep_playing = input("Introduce Y to play again or N to stop\n")
    while True:  # Validate keep_playing
        if validate_play_again(keep_playing):
            break
        else:
            keep_playing = input("Introduce Y to play again or N to stop\n")

    if keep_playing.upper() == "Y":
        print("\n\n\n")
        new_game()  # Starts a new game
    else:
        print("Thanks for playing!")


def play_game(game):
    """
    Plays a game of Battleships game with turns limit.
    Prints game turns limits and information about the ships on this game
    Plays a round of the game until turns reaches 0,
    or player or computer runs out of ships.
    When that happens shows the game_over_message, scores, winner, boards
    and checks if the user wants to play again.
    """
    # Gets the settings for this game
    settings = get_settings(game.player_board.size)
    print("\n\n"+"-"*30)
    # Prints the turns limit for this game
    print(f"Turns limit for the game: {game.turns}")
    # Prints the number and the value of each type of ship on the board
    print("\nEach board has:")
    print(
        f"{settings['small_ship']} Small ships with a value of 3 points each"
        )
    print(
        f"{settings['medium_ship']} Medium ships with a value of 2 points each"
        )
    print(
        f"{settings['big_ship']} Big ships with a value of 1 point each"
        )
    # Prints player and computer boards
    print_boards(game.player_board, game.computer_board)
    print("\nGood Luck!")
    print("-"*30+"\n\n")
    game_over = False
    game_over_message = "*"*30+"\n"+"*"*10+"GAME**OVER"+"*"*10+"\n"+"*"*30
    # Plays a round of the game until game_over it's True
    while not game_over:
        # Play a round of the game
        play_round(game)
        # If the player or computer ships attribute are empty
        # or the turns reaches 0
        # Set game_over to True and add a custom message to game_over_message
        if not game.player_board.ships:
            game_over = True
            game_over_message += f"\nAll {game.player_name}'s ships sunked"
        elif not game.computer_board.ships:
            game_over = True
            game_over_message += f"\nAll Computers's ships sunked"
        elif game.turns == 0:
            game_over = True
            game_over_message += "\nTimes up!"
        # If the game_over still False
        # Prints the ramaining turns, scores, and the boards
        if not game_over:
            game.turns_remaining()
            print("--Current scores--")
            game.print_scores()
            print("*"*30)
            print_boards(game.player_board, game.computer_board)
            print("")
    # Prints game_over_message
    print("\n\n"+game_over_message)
    # Shows the ships on the computer board
    game.computer_board.show_ships()
    # Prints the boards
    print_boards(game.player_board, game.computer_board)
    # Prints the final scores
    print("\n--Finals scores--")
    game.print_scores()
    # Prints the winner
    get_winner(game)
    print("\n\n")
    # Checks if the user wants to play again
    play_again()


def new_game():
    """
    This function starts a new game.
    Gets the username, board size and game turns.
    Initialize player and computer boards, and the game class.
    Populates the boards and shows the ships on the player board.
    Calls play_game() to start playing the game.
    """
    # Welcome message
    print("-"*30)
    print("Welcome to Battleships Game!")
    print("Press enter to start")
    print("-"*30)
    input("")
    # Gets the username
    name = get_name()
    # Gets the board size
    size = get_size()
    # Gets the turns
    turns = get_settings(size)["turns"]
    # Initialize player and computer boards, and game classes
    player_board = Board(name, "Player", size)
    computer_board = Board("Computer", "Computer", size)
    game = Game(turns, name, player_board, computer_board)
    # Populates the player_board
    populate_board(game.player_board)
    # Shows the ships on the player_board
    game.player_board.show_ships()
    # Populate computer_board
    populate_board(game.computer_board)
    # Start to play the game
    play_game(game)


# Starts a new game
new_game()

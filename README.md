# Battleships game

## Testing

### Manual testing

- Username

    **Test**|**Expected outcome**|**Test performed**|**Outcome**|**Test passed**
    ---|---|---|---|:---:
    Empty|Username cannot be empty. Please introduce a valid username (4-11 characters)|Introduced empty username|Username cannot be empty. Please introduce a valid username (4-11 characters)|Yes
    Not alphanumeric|Username only can contain letters, digits or spaces. Please introduce a valid username (4-11 characters)|Introduced "#"|Username only can contain letters, digits or spaces. Please introduce a valid username (4-11 characters)|Yes
    Less than 4 characters|Username too short. Please introduce a valid username (4-11 characters)|Introduced "123"|Username too short. Please introduce a valid username (4-11 characters)|Yes
    More than 11 characters|Username too long. Please introduce a valid username (4-11 characters)|Introduced "0123456789abcd"|Username too long. Please introduce a valid username (4-11 characters)|Yes
    Starts with space|Username cannot start or end with a space. Please introduce a valid username (4-11 characters)|Introduced " Paul"|Username cannot start or end with a space. Please introduce a valid username (4-11 characters)|Yes
    Ends with space|Username cannot start or end with a space. Please introduce a valid username (4-11 characters)|Introduced "Paul "|Username cannot start or end with a space. Please introduce a valid username (4-11 characters)|Yes
    Two spaces in a row|Username cannot have more than one space in a row. Please introduce a valid username (4-11 characters)|Introduced "Pa&nbsp;&nbsp;ul"|Username cannot have more than one space in a row. Please introduce a valid username (4-11 characters)|Yes
    Valid|Please introduce the size of the board(options availables 4-10)|Introduced "Paul"|Please introduce the size of the board(options availables 4-10)|Yes

- Size

    **Test**|**Expected outcome**|**Test performed**|**Outcome**|**Test passed**
    ---|---|---|---|:---:
    Empty|Size cannot be empty. Please introduce a valid size (options availables 4-10)|Introduced empty size|Size cannot be empty. Please introduce a valid size (options availables 4-10)|Yes
    Not numeric|Size must be a positive intenger number. Please introduce a valid size (options availables 4-10)|Introduced "Paul"|Size must be a positive intenger number. Please introduce a valid size (options availables 4-10)|Yes
    Not positive numeric|Size must be a positive intenger number. Please introduce a valid size (options availables 4-10)|Introduced "-1"|Size must be a positive intenger number. Please introduce a valid size (options availables 4-10)|Yes
    Less than 4|Invalid size option. Please introduce a valid size (options availables 4-10)|Introduced "3"|Invalid size option. Please introduce a valid size (options availables 4-10)|Yes
    Greater than 10|Invalid size option. Please introduce a valid size (options availables 4-10)|Introduced "11"|Invalid size option. Please introduce a valid size (options availables 4-10)|Yes
    4|Turns: **10** Small ships: **2** Medium ships: **0** Big ships: **0** Random generated **4x4** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "4"|![Board size 4](assets/images/board_size_4.png)|Yes
    5|Turns: **15** Small ships: **3** Medium ships: **1** Big ships: **0** Random generated **5x5** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "5"|![Board size 5](assets/images/board_size_5.png)|Yes
    6|Turns: **20** Small ships: **4** Medium ships: **2** Big ships: **0** Random generated **6x6** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "6"|![Board size 6](assets/images/board_size_6.png)|Yes
    7|Turns: **25** Small ships: **5** Medium ships: **2** Big ships: **1** Random generated **7x7** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "7"|![Board size 7](assets/images/board_size_7.png)|Yes
    8|Turns: **35** Small ships: **6** Medium ships: **2** Big ships: **2** Random generated **8x8** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "8"|![Board size 8](assets/images/board_size_8.png)|Yes
    9|Turns: **40** Small ships: **7** Medium ships: **3** Big ships: **2** Random generated **9x9** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "9"|![Board size 9](assets/images/board_size_9.png)|Yes
    10|Turns: **50** Small ships: **8** Medium ships: **3** Big ships: **3** Random generated **10x10** board for player and computer (Only shows the ships on the player's board. Also shows username above player board)|Introduced "10"|![Board size 10](assets/images/board_size_10.png)|Yes
    

### Validator testing

- No errors were returned when passing through [CI Python Linter](https://pep8ci.herokuapp.com/)

    ![Python validation](assets/images/python_validator.png)
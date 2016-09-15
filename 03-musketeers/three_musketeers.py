# The Three Musketeers Game
# by David Matuszek and <insert your name here>.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    row_lookup = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4 }
    col_lookup = { '1': 0, '2': 1, '3': 2, '4': 3, '5': 4 }
    return (row_lookup[s[0]], col_lookup[s[1]])

def string_to_location_2(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    # ord              return the unicode value of a single letter
    # ord("A")         get the numeric value of the capital letter A
    A = ord("A")
    # ord(s[0])        get the numeric value of the FIRST LETTER in the string_to_location
    # ord(s[0]) - A    take the numeric value of the first letter of the string_to_location
    #                  and subtract the value of the FIRST AVAILABLE letter
    #                  so SINCE the ASCII code of the letter A is 65, this is similar to saying 
    #                  NUMBER_OF FIRST_LETTER - 65
    #
    # int(s[1])        convert the SECOND letter of the string to an integer
    # int(s[1]) - 1    set this number to the equivalent of a ZERO-BASED array 
    return (ord(s[0]) - A, int(s[1]) - 1)
    # alternative:
    # return (ord(s[0]) - 65, int(s[1]) - 1)

def location_to_string(location):
    """Returns the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    # 65 is the known ASCII number value of the capital letter A
    # if we convert 65 to a character using the `chr` function
    # we get the letter A
    # so if we pass a `0` as position 1 of the location, we get the CHARACTER 'A' + 0 (additional letters)
    # if we pass a `1` as position 1 of the location, we get the CHARACTER 'A' + 1 additional letters which is 'B'
    # and so on.
    #
    # similarly, we are looking for a string version of the number in position 2 of the location
    # so we *first* add one because the coordinate system starts with 1 and not 0
    # then we turn that increased number into a string using the str function
    #
    # finally we concatenate that string using + and return it.  
    return chr(location[0]+65) + str(location[1]+1)

def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    pass # Replace with code

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, column) = location
    pass # Replace with code

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    assert at(location) == 'M'
    pass # Replace with code

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'
    pass # Replace with code

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction."""
    pass # Replace with code

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    pass # Replace with code

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    pass # Replace with code

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available."""
    pass # Replace with code

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    pass # Replace with code
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    pass # Replace with code
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    pass # Replace with code

def make_move(location, direction):
    """Moves the piece in location in the indicated direction."""
    pass # Replace with code

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    pass # Replace with code

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    pass # Replace with code

#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = "")
        for j in range(0, 5):
            print(board[i][j] + " ", end = "")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    

    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if move[0] in 'ABCDE' and move[1] in '12345' and move[2] in 'LRUD':
        return (string_to_location(move[0:2]), directions[move[2]])
    print("Illegal move--'" + move + "'")
    print_instructions()
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
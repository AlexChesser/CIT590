# This is a Lunar Lander game
# The purpose of the game is to safely land your Lunar Lander on the moon
# The Lunar Lander is X meters above the moon's surface
# Gravity is pulling it down at an increasing velocity
# Everytime the user burns fuel, the velocity slows down
# The user has a finite amount of fuel 
# The user must input the correct amount of fuel to burn at the right time to land safely on the moon's surface

def play_game(play_game_text):
    # this function checks to see if the user wants to play the game
    user_response = input(play_game_text)
    if len(user_response) == 0:
        print("Incorrect response. ")   
        play_game("Enter Y or N. ")
    else:
        user_response = user_response[0].lower()
        if user_response == "y":
            start_game()
        elif user_response == "n":
            print("Your loss. ")
        else:
            print("Incorrect response. ")
            play_game("Enter Y or N. ")

global current_altitude
global current_fuel
global current_velocity

def start_game():
# this function launches the Lunar Lander game
    global current_altitude
    current_altitude = 1000
    global current_fuel
    current_fuel = 1000
    global current_velocity
    current_velocity = 0
    while current_altitude > 0:
        report_user_status()
        fuel_burned = ask_user_to_burn_fuel()
        process_gravity_and_fuel(fuel_burned)
        assess_safe_landing()
    play_game("Do You Want to Play Again?\nEnter Y or N. ")
      
def report_user_status():
    # this function tells the user their current_altitude, current_velocity, current_fuel
    print("Your current altitude is:", current_altitude)
    print("Your current velocity is:", current_velocity)
    print("Your current fuel level is:", current_fuel)

def ask_user_to_burn_fuel():
    # this function asks the user how much fuel they want to burn each turn
    global current_fuel 
    fuel_input = input("How much fuel would you like to burn?\nEnter a number: ")
    if len(fuel_input) == 0:
        fuel_input = 0
    else:
        fuel_input = int(fuel_input)
    if fuel_input <= 0:
        fuel_input = 0
    elif fuel_input > current_fuel:
        fuel_input = current_fuel
    current_fuel = current_fuel - fuel_input
    return fuel_input       

def process_gravity_and_fuel(fuel_burned):
    #this function calculates how far the Lunar Lander has fallen and how much fuel has been burned
    global current_velocity
    current_velocity = current_velocity + 1.6 - 0.15*fuel_burned
    global current_altitude
    current_altitude = current_altitude - current_velocity

def assess_safe_landing():
    if current_altitude <= 0:
        if current_velocity <= 10:
            win_condition()
        else: 
            lose_condition()

def win_condition():
    global current_altitude 
    current_altitude = 0
    global current_velocity
    current_velocity = 0
    report_user_status()
    print("Congratulations cosmonaut!\nYou have landed safely on the moon! ")

def lose_condition():
    crater_size = current_velocity*2
    print("Oh no!\nYou have crashed on the moon.\nYou made a crater that is " + str(crater_size) + " meters deep! ")

play_game("Would you like to play Lunar Lander?\nEnter Y or N. ")

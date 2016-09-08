# This is a Lunar Lander game
# The purpose of the game is to safely land your Lunar Lander on the moon
# The Lunar Lander is X meters above the moon's surface
# Gravity is pulling it down at an increasing velocity
# Everytime the user burns fuel, the velocity slows down
# The user has a finite amount of fuel 
# The user must input the correct amount of fuel to burn at the right time to land safely on the moon's surface


# this function checks to see if the user wants to play the game
user_response = input("Would you like to play Lunar Lander?\nEnter Y or N. ")
if len(user_response) == 0:
    print("Incorrect response. ")   
    # play_game("Enter Y or N. ")
else:
    user_response = user_response[0].lower()
    if user_response == "y":
        current_altitude = 1000
        current_fuel = 1000
        current_velocity = 0
        while current_altitude > 0:
            print("Your current altitude is:", current_altitude)
            print("Your current velocity is:", current_velocity)
            print("Your current fuel level is:", current_fuel)

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

            current_velocity = current_velocity + 1.6 - 0.15*fuel_input
            current_altitude = current_altitude - current_velocity

            if current_altitude <= 0:
                if current_velocity <= 10:
                    current_altitude = 0
                    current_velocity = 0
                    print("Your current altitude is:", current_altitude)
                    print("Your current velocity is:", current_velocity)
                    print("Your current fuel level is:", current_fuel)
                    print("Congratulations cosmonaut!\nYou have landed safely on the moon! ")
                else: 
                    crater_size = current_velocity*2
                    print("Oh no!\nYou have crashed on the moon.\nYou made a crater that is " + str(crater_size) + " meters deep! ")
    elif user_response == "n":
        print("Your loss. ")
    else:
        print("Incorrect response. ")   
        #play_game("Enter Y or N. ")

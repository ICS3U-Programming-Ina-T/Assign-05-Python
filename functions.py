#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 20, 2022
# This program calculates three different things:
# current, acceleration, and speed. It asks the user to enter
# numbers for the necessary variables.


# function calculates the speed of an object
def calc_speed(distance, time):
    speed = distance / time
    # copies result to main function
    return speed


# function calculates the acceleration of an object
def calc_accel(force, mass):
    acceleration = force / mass
    # copies result to main function
    return acceleration


# function calculates the current in a circuit
def calc_current(voltage, resistance):
    current = voltage / resistance
    # copies result to main function
    return current


# function gets input, check for invalid data
# and displays results to user
def main():
    # display opening message
    print("Today we will calculate three different values: "
          "current, acceleration, and speed.")
    print("")
    print("We will start off by calculating current, according to Ohm's Law.")
    print("")

    while True:
        # gets input from user
        voltage_user = input("Enter the voltage (V): ")
        try:
            # converts string to float
            voltage_float = float(voltage_user)

            # checks if value is negative
            if voltage_float < 0:
                print("Please enter a positive integer!")
                print("")
                continue
            while True:
                # gets input from user
                resistance_user = input("Enter the resistance (Ω): ")
                try:
                    # converts string to float
                    resistance_float = float(resistance_user)
                    # checks if value is negative
                    if resistance_float < 0:
                        print("Please enter a positive integer!")
                        print("")
                        continue
                    # assigns variable to function call
                    current_user = calc_current(voltage_float,
                                                resistance_float)
                    # displays results to user
                    print("")
                    print("The current through a {:,.2f}V battery "
                          "and a {:,.2f}Ω resistor is {:,.2f}A"
                          .format(voltage_float, resistance_float,
                                  current_user))
                    print("")
                    print("----------------------------------"
                          "----------------------------------"
                          "---------------------")
                    print("")
                    print("Second, we will calculate the acceleration "
                          "of an object, according to Newton's Second Law.")
                    print("")

                    while True:
                        # gets input from user
                        force_user = input("Enter the Force (N): ")
                        try:
                            # converts string to float
                            force_float = float(force_user)
                            # checks if value is negative
                            if force_float < 0:
                                print("Please enter a positive integer!")
                                print("")
                                continue
                            while True:
                                # gets input from user
                                mass_user = input("Enter the mass (kg): ")
                                try:
                                    # convert string to float
                                    mass_float = float(mass_user)
                                    # checks if value is negative
                                    if mass_float < 0:
                                        print("Please enter a positive "
                                              "integer!")
                                        print("")
                                        continue
                                    # assigns variable to function call
                                    acceleration_user = calc_accel(force_float,
                                                                   mass_float)
                                    # displays results to the user
                                    print("")
                                    print("The acceleration of an object with "
                                          "a force of {:,.2f}N and a mass of "
                                          "{:,.2f}kg is {:,.2f}N/kg"
                                          .format(force_float, mass_float,
                                                  acceleration_user))
                                    print("")
                                    print("-----------------------------"
                                          "-----------------------------"
                                          "-------------------------------")
                                    print("")
                                    print("Lastly, we will calculate the "
                                          "speed of an object, given its "
                                          "total distance travelled and time.")
                                    print("")

                                    while True:
                                        # gets input from user
                                        distance_user = input("Enter the "
                                                              "total distance "
                                                              "(m): ")
                                        try:
                                            # converts string to float
                                            distance_float = \
                                                float(distance_user)
                                            # checks if value is negative
                                            if distance_float < 0:
                                                print("Distance cannot "
                                                      "be negative!")
                                                print("")
                                                continue
                                            while True:
                                                # gets input from the user
                                                time_user = input("Enter "
                                                                  "the time "
                                                                  "(s): ")
                                                try:
                                                    # converts string
                                                    # input to float
                                                    time_float = \
                                                        float(time_user)
                                                    # checks if
                                                    # value is negative
                                                    if time_float < 0:
                                                        print("Time cannot "
                                                              "be negative!")
                                                        print("")
                                                        continue
                                                    # initializes variable
                                                    # to end the loop
                                                    stop_loop = 2

                                                    # checks if variable
                                                    # has been initialized
                                                    # if so, displays results
                                                    # to the user, then breaks
                                                    # out of loop
                                                    if stop_loop == 2:
                                                        speed_user = \
                                                            calc_speed(
                                                                distance_float,
                                                                time_float)
                                                        print("")
                                                        print("The speed "
                                                              "of an "
                                                              "object that "
                                                              "travelled a "
                                                              "distance of "
                                                              "{:,.2f}m in "
                                                              "{:,.2f}s is "
                                                              "{:,.2f}m/s"
                                                              .format(
                                                            distance_float,
                                                            time_float,
                                                            speed_user))
                                                        break
                                                # checks if input is a string
                                                except Exception:
                                                    print("{} is an invalid "
                                                          "entry."
                                                          .format(time_user))
                                                    print("")
                                            # ends the loop
                                            break
                                        except Exception:
                                            print("{} is an invalid entry."
                                                  .format(distance_user))
                                            print("")
                                    # ends the loop
                                    break
                                # checks if input is an invalid string
                                except Exception:
                                    print("{} is an invalid entry."
                                          .format(mass_user))
                                    print("")
                            # ends the loop
                            break
                        # checks if input is an invalid string
                        except Exception:
                            print("{} is an invalid entry."
                                  .format(force_user))
                            print("")
                    # ends the loop
                    break
                # checks if input is an invalid string
                except Exception:
                    print("{} is an invalid entry." .format(resistance_user))
                    print("")
            # ends the loop
            break
        # checks if input is an invalid string
        except Exception:
            print("{} is an invalid entry." .format(voltage_user))
            print("")


if __name__ == "__main__":
    main()

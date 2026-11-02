# Erly Cherizar
# short story based game where you go through the day in the life of Erly

if __name__ == "__main__":
    is_running = False
    print("-" * 80)
    print(" " * 30, "The Early Adventures", " " * 30)
    print("Welcome!\nCongratulations on being the first player of", end=" ")
    print("The Early Adventures!")
    playing = input("Would you like to play? [Y/N] ")
    print("-" * 80)
    # the * string operator makes it easier to do a nice separator between print statements
    if playing.upper() == "Y":
        is_running = True
    while is_running:
        def subtraction(first, second):
            print("Boom! Here it is:", int(num8 - num9))
            # the - operator subtracts together the two integer variables.
        print("You wake up on a Monday morning...\nWhat would you like to do?\n" +
              "|Go to all classes [1]|\n|Skip Comp II and Calc I and workout [2]|\n" +
              "|Skip all classes and chud [3]|\n")
        # the + string operator is to make this single print statement more readable
        route = int(input("Enter 1, 2, or 3 "))
        if route != 1 and route != 2 and route != 3:
            print("\nNot a valid input")
        else:
            """
        while True:
            route = int(input("Enter 1, 2, or 3 "))
            if route != 1 and route != 2 and  route !=3:
                print("\nNot a valid input")
                route = input("Enter 1, 2, or 3 ")
            else:
                break"""
            if route == 1:
                print("-" * 80 + "\nYou go to Comp II... it was boring.\nYou then go to Calculus I!\n" +
                      "It's time to do the math quiz game for today!")
                ready = input("Are you ready? [Y/N]")
                if ready.upper() == "Y":
                    pass
                else:
                    print("Fine then don't do it...")
                    break
                print("-" * 80 + "\nI am your calculator! You need to multiply 2 numbers to equal 25!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if num1 * num2 == 25:
                    print("You did it!")
                    # the * operator multiples the two input variables for the if statement
                else:
                    print("Awwww better luck next time! You lose the game!")
                    break
                print("-" * 80)
                num3 = float(input("Give me a number to square that equals 64: "))
                if num3 ** 2 == 64:
                    print("You're pretty smart, nice!")
                    # the ** operater raises the input variable to a power for the if statement
                else:
                    print("Awwww better luck next time! You lose the game!")
                    break
                print("-" * 80)
                num4 = int(input("Give me a number to divide by 2 " +
                                 "that will equal a whole number: "))
                if num4 % 2 == 0:
                    quotient = num4 / 2
                    print("You're good at this!", "Here's your quotient:", quotient)
                    # the % operator returns the remainder of the variable over 2 for the if statement
                    # the / operator divides the variable by a number, which will return the user's quotient
                else:
                    print("Awwww better luck next time! You lose the game!")
                    break
                print("-" * 80)
                num5 = float(input("Lets make this fun ;)\nGive me a number with a bunch of decimals: "))
                new_num = num5 // 1
                print("Tadaaaa!\n" + "Your number:", int(new_num), "\nAll the decimals went poof!")
                # the // operator rounds down the quotient of the equation to the nearest whole number.
                input("Press Enter to Continue! ")
                print("-" * 80)
                print("Okay for the last two things, you will get a magic trick!")
                print("Im actually a mastermind who knows everything, so...")
                num6 = float(input("Give me a biiig number to do addition: "))
                num7 = float(input("Give me the second number: "))
                print("Bam! Your sum:", int(num6 + num7), sep=" | ")
                # the + operator adds together the two integer variables.
                print("-" * 80)
                print("Last but not least, lets do it for subtraction!")
                num8 = float(input("First number please: "))
                num9 = float(input("Second number please: "))
                subtraction(num8,num9)
                print("Impressive eh? no? anyways...\nThanks for Playing!")
                print("-" * 80)

                empty = []
                if ord("A") < ord("a") and ord("A") < ord("g"):
                    if not 3 > 5 or 1 > 2:
                        for x in range(3):
                            empty.append(x)

                is_running = False

            if route == 2:
                print("So... you really thought you were gonna skip class to workout?")
                print("Get out of here man! GO TO SCHOOL")
                is_running = False

            if route == 3:
                print("Wowww, skipping the WHOLE day huh?")
                print("Absolutely NOT! Expelled!!!!")
                is_running = False
# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
# CS 31, Kolboth Kong, November 8, 2026

def display_title():
    print("Welcome to Jack's Mad Libs!")
    print()

def play_game():
    player_name = input("What is your name? ")
    print()
    print(f"Hello, {player_name}! Which story would you like to use?")
    print(
        """
a. Jack's day at the playground
b. Jack's weekend with the family
""")
    choice = input("What is your choice? ")
    while choice.upper() != "A":
        if choice.upper() == "B":
            break
        else:
            print("Invalid input. Please try again.")
            choice = input("Please enter a or b ")
    if choice.upper() == "A":
        print()
        print("Let's collect words for Jack's playground adventure!")
        print()
        friend = input("1) Enter a friend's name: ")
        adjective = input("2) Enter an adjective: ")
        snack = input("3) Enter your favorite midnight snack: ")
        animal = input("4) Enter an animal: " )
        action = input("5) Enter a verb ending in -ing: ")
        number = input("6) Enter a number from 1 to 10: ")

        print()
        print(f"{player_name}, here is your story:")
        print()
        print(
            f"Jack and {friend} visited a {adjective} playground. \n"
            f"They brought {number} bags of {snack} "
            "for their afternoon picnic. \n"
            f"Suddenly, a {animal} appeared and started "
            f"{action} on the slide. \n"
            f"While Jack watched, {friend} ate all the snacks. \n"
            "Jack decided that next time, he would bring "
            "a lunchbox with a lock."
        )
    elif choice.upper() == "B":
        print()
        print("Let's collect words for Jack's family weekend!")
        print()
        family_member = input("1) Enter a family member's name: ") 
        place = input("2) Enter a place you want to visit next year: ")
        vehicle = input("3) Enter a type of transportation: ")
        color = input("4) Enter the color of your shirt: ")
        clothing = input("5) Enter an item of clothing: ")
        hours = int(input("6) Enter a number from 1 to 10: "))
        print()
        print(f"{player_name}, here is your story:")
        print()
        print(
            f"Jack and his family decided to visit {place} "
            "for the weekend. \n"
            f"They packed their bags into a {color} {vehicle} "
            f"and traveled for {hours} hours. \n"
            f"When they arrvied, {family_member} realized "
            f"their suitcase contained nothing but a single {clothing}. \n"
            "Jack opened his own suitcase and found "
            "a television remote and three empty ceareal boxes. \n"
            "The family agreed that next time "
            "an adult would supervise the packing."
        )

def main():
    display_title()

    counter = 0
    again = input("Would you like to play? y/n: ")
    print()
    while again.upper() != "Y":
        if again.upper() == "N":
            break
        else:
            print("Invalid input. Please try again.")
            again = input("Please enter y or n: ")

    while again.upper() == "Y":
        play_game()
        counter += 1 
        print()

        if counter == 1:
            print("You have created 1 story.")
        else:
            print(f"You have created {counter} stories.")
        print()
        again = input("Would you like to play again? y/n: ")
        while again.upper() != "Y":
            if again.upper() == "N":
                break
            else:
                print("Invalid input. Please try again. ")
                again = input("Please enter y or n: ")
        print()
    print("Thanks for playing! Goodbye!")

main()

# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Kol K. 10/7/26

print("NBA Trivia")
print()
print("* " * 20)
print()
username = input("What is your name? ")
print(f"Hello, {username}!")
print()
start_quiz = input("Do you want to take this quiz? Y/N ")
if start_quiz.upper() == "Y":
    print("Great! Let's get started")
    print()
    counter = 0

    # Question 1

    print("1. Which NBA Team won the championship in the 2025-2026 season?" )
    print("     A. San Antonio Spurs")
    print("     B. Oklahoma City Thunder")
    print("     C. New York Knicks")
    print("     D. Boston Celtics") 
    print()
    q1 = input("Your Answer: " )
    if q1.upper() == "C":
        counter += 1
        print()
        print("You are correct! The New York Knicks won the NBA Championship in the 2025-2026 season.")
        print()
        print(" * " * 20)
        print()
    else:
        print("You are incorrect!")
        print()
        print(" * " * 20)
        print ()

    # Question 2

    print("2. Who won the NBA Most Valuable Player award in the 2025-2026 season?")
    print("     A. Luka Doncic")
    print("     B. Nikola Jokic")
    print("     C. Victor Wembanyama")
    print("     D. Shai Gilgeous-Alexander")
    print()
    q2 = input("Your Answer: " )
    if q2.upper() == "D":
        counter += 1
        print()
        print("You are correct! Shai Gilgeous-Alexander won back to back MVPs.")
        print()
        print(" * " * 20)
        print()
    else:
        print("You are incorrect!")
        print()
        print(" * " * 20)
        print()

    # Question 3 

    print("3. Which NBA team has the most championships?")
    print("     A. Los Angeles Lakers")
    print("     B. Golden State Warriors")
    print("     C. Boston Celtics")
    print("     D. Chicago Bulls")
    print()
    q3 = input("Your Answer: " )
    if q3.upper() == "C":
        counter += 1
        print()
        print("You are correct! The Boston Celtics has the most championships with 18.")
        print()
        print(" * " * 20)
        print()
    else:
        print("You are incorrect!")
        print()
        print(" * " * 20)
        print()

    # Question 4 
    
    print("4. Which NBA player won the scoring title in the 2025-2026 season?")
    print("     A. Luka Doncic")
    print("     B. Giannis Antetokounmpo")
    print("     C. Shai Gilgeous-Alexander")
    print("     D. Anthony Edwards")
    print()
    q4 = input("Your Answer: " )
    if q4.upper() == "A":
        counter += 1
        print()
        print("You are correct! Luka Doncic led the NBA with 33.5 PPG.")
        print()
        print(" * " * 20)
        print()
    else:
        print("You are inncorect!")
        print()
        print(" * " * 20)
        print()

    # Question 5

    print("5. Which NBA Player had the most technical foul in the 2025-2026 season?")
    print("     A. Devin Booker")
    print("     B. Dillion Brooks")
    print("     C. Draymond Green")
    print("     D. Jaylen Brown")
    print()
    q5 = input("Your Answer: " )
    if q5.upper() == "B":
        counter += 1
        print()
        print("You are correct! Dillion Brooks ended the season with 17 technical fouls.")
        print()
        print(" * " * 20)
        print()
    else:
        print("You are incorrect!")
        print()
        print(" * " * 20)
        print()

    print("* * * Your Final Score * * *")
    print(f"Your Final Score Is: {counter}/5")

    if counter == 5:
        print("Great job! You got them all right.")
    elif counter >= 3 and counter < 5:
        print("Solid work! You got good NBA knowledge!")
    elif counter >= 1 and counter < 3:
        print("You almost had it! Try again.")
    else:
        print("Maybe this isn't your sport.")

elif start_quiz.upper() == "N":
    print("Sorry, maybe next time!")
else:
    print(f"Sorry, \"{start_quiz}\" is an invalid response. Try again")

print("Thank you for taking this trivia. Have a nice day!")
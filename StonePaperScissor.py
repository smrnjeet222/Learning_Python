import random

computer_score = 0
user_score = 0

while True:
    option = ["stone", "paper", "scissor"]
    a = random.choice(option)
    user_input = input(
        """ Enter Your Option:
    1) STONE
    2) PAPER
    3) SCISSOR
    Press Q to exit.

    """
    )
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input <= 3 and user_input > 0:

            if option[user_input - 1] == a:
                computer_score, user_score = computer_score, user_score

            elif option[user_input - 1] == "stone":
                if a == "paper":
                    computer_score = computer_score + 1
                    print("Computer Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")
                if a == "scissor":
                    user_score = user_score + 1
                    print("User Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")

            elif option[user_input - 1] == "paper":
                if a == "scissor":
                    computer_score = computer_score + 1
                    print("Computer Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")
                if a == "stone":
                    user_score = user_score + 1
                    print("User Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")

            elif option[user_input - 1] == "scissor":
                if a == "stone":
                    computer_score = computer_score + 1
                    print("Computer Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")
                if a == "paper":
                    user_score = user_score + 1
                    print("User Wins")
                    print(
                        "Computer Score : ",
                        computer_score,
                        " User Score : ",
                        user_score,
                    )
                    print(" ")
        else:
            print("Invalid Input")

    elif user_input.isdigit() == False:
        if str(user_input).lower() == "q":
            print("Final Score")
            print("Computer Score : ", computer_score, "User Score : ", user_score)
            break
        else:
            print("Invalid Input")


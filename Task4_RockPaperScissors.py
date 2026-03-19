import random

def check_winner(user,computer):
    if user==computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

choices=["rock","paper","scissors"]

user_score=0
computer_score=0

print("\n===== Rock Paper Scissors Game =====")

while True:

    try:
        user_choice=input("Enter rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice! please enter rock, paper or scissors!")
            continue

        computer_choice=random.choice(choices)

        print("your choice is:",user_choice)
        print("computer choice is:",computer_choice)

        result=check_winner(user_choice,computer_choice)

        if result=="tie":
            print("it's a tie!")
        elif result=="user":
            print("you win!")
            user_score+=1
        else:
            print("computer wins!")
            computer_score+=1

        print("score:")
        print("your score:",user_score)
        print("computer score:",computer_score)

        play_again=input("do you want to play again? (yes/no)").lower()

        if play_again!="yes":
            if user_score>computer_score:
                print("Congratulations! you are the overall winner!")

            elif computer_score>user_score:
                print("Computer is the overall winner! better luck next time!")

            else:
                print("It's a tie overall! well played!")

            print("Game over!")
            break
    except Exception:
        print("An error occurred! please try again!")
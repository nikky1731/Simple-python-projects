import random

print('Rules: \n'
      'Rock vs Paper -> paper wins\n'
      'Rock vs Scissors - > Rock wins\n'
      'Paper vs Scissors -> Scissor wins\n')

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper\n 3 - Scissor\n")
    choice = int(input("enter your choice"))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = "Paper"
    else: choice_name = "Scissors"

    print("Users choice is ", choice_name)
    print("now its computer turn")

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else: comp_choice_name = "Scissors"

    print("Computer choice is ", comp_choice_name)
    print(choice_name, "Vs" , comp_choice_name)

    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = "Scissors"

    if result == "Draw":
        print("its a tie")
    elif result  == choice_name :
        print("user Wins")
    else:
        print("Computer wins")

    print("Do you want to play again? Y/N")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing ")
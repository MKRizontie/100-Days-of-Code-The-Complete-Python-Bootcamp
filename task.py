import random

rock = '''
         _______
     ---'   ____)_
            (_____)
            (_____)
            (____)
     ---.__(___)
'''

paper = '''
         _______
     ---'   ____)____
               ______)
              _______)
             _______)
     ---.__________)
'''

scissors = '''
         _______
     ---'   ____)____
               ______)
            __________)
           (____)
     ---.__(___)
'''

gestures = {"0": ("rock", rock), "1": ("paper", paper), "2": ("scissors", scissors)}
print("Welcome to Rock, Paper, Scissors!")
print("Select your choice: \n0 for Rock, 1 for Paper, 2 for Scissors")

player_score = 0
computer_score = 0

while True:
    user_input = input("Enter your choice (0, 1, 2 or 'quit' to exit): ").lower()
    if user_input == "quit":
        print("Thanks for playing!")
        print(f"Final Scores - Player: {player_score}, Computer: {computer_score}")
        break

    if user_input not in gestures:
        print("Invalid choice. Please choose 0, 1, or 2.")
        continue

    user_choice, user_gesture = gestures[user_input]
    computer_choice, computer_gesture = random.choice(list(gestures.values()))

    print(f"You chose:\n{user_gesture}")
    print(f"Computer chose:\n{computer_gesture}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Current Scores - Player: {player_score}, Computer: {computer_score}")
    print("-" * 30)

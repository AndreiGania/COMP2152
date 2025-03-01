import random

# Define the choices array
choices = ["Rock", "Paper", "Scissor"]

def main(): #main function
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()

        # Validate the user input
        if user_input not in choices:
            raise ValueError("Invalid choice, Please enter a valid choice.")

        # Convert the user input to an index
        playerChoice = choices.index(user_input)

        computerChoice = random.randint(0, 2)

        print(f"Player choice: {choices[playerChoice]}")
        print(f"Computer choice: {choices[computerChoice]}")


        # Determine the winner
        if  playerChoice == computerChoice:
            print("Draw")
        elif (playerChoice == 0 and computerChoice == 2) or \
             (playerChoice == 1 and computerChoice == 0) or \
             (playerChoice == 2 and computerChoice == 1):
            print("Player wins!")
        else:
            print("Computer wins!")
    except ValueError as e:
        print(f"Error: {e}")

# Run the game through the main function
if __name__ == "__main__":
    main()

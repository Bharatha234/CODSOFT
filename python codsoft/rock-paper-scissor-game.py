import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"
def show_menu():
    print("\nRock-Paper-Scissors Game")
    print("1. Play")
    print("2. Exit")
def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return None, None
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")
    return result
def main():
    user_score = 0
    computer_score = 0
    while True:
        show_menu()
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            result = play_round()
            if result:
                if result == "win":
                    user_score += 1
                elif result == "lose":
                    computer_score += 1
            print(f"\nScore - You: {user_score} | Computer: {computer_score}")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for playing!")
                break
        elif choice == '2':
            print("Thank you for playing!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()

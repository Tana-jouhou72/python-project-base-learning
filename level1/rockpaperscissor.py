import random


def main():
    print("\nWelcome to Rock-Paper-Scissor Game!")

    while True:    
        user, computer = get_user_and_computer_choice()
        print_result(user, computer)
        try:
            next_game = input("\nDo you wnat to play next game? (y/n): ").lower()
            if next_game == 'y':
                continue
            elif next_game == 'n':
                break
            else:
                continue
        except ValueError:
            raise ValueError("Enter (y/n): ")


def get_user_and_computer_choice():
    choices = ['r', 'p', 's']
    user_choice = input("Choose r:rock, p:paper, s:scissor : ")
    while user_choice not in choices:
        print("Please enter a valid input")
        user_choice = input("Choose r:rock, p:paper, s:scissor : ")
    computer_choice = random.choice(choices)
    return user_choice, computer_choice

def win(user, computer):
    choice = ['r', 'p', 's']
    if user == computer:
        return "Tie"
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "You won"
    else:
        return "computer won"

def print_result(user, computer):
    lists = {
        "r": "rock",
        "s": "scissor",
        "p": "paper"
    }

    print(f"You chose: {lists[user].title()}")
    print(f"Computer chose: {lists[computer].title()}")
    print(win(user, computer))





if __name__ == "__main__":
    main()
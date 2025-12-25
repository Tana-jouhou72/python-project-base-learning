import random
from typing import List

class RockPaperScissor:

    def __init__(self):
        self.choices = ['r', 'p', 's']

    def get_user_and_computer_choice(self):
        user_choice = input("\nChoose r:rock, p:paper, s:scissor : ")
        while user_choice not in self.choices:
            print("Please enter a valid input")
            user_choice = input("\nChoose r:rock, p:paper, s:scissor : ")
        computer_choice = random.choice(self.choices)
    
        return user_choice, computer_choice
    
    def win(self, user, computer):
        if user == computer:
            return "Tie"
        elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
            return "You won"
        else:
            return "Computer won"

    def print_result(self, user, computer):
        lists = {
        "r": "rock",
        "s": "scissor",
        "p": "paper"
        }
        print(f"You chose: {lists[user].title()}")
        print(f"Computer chose: {lists[computer].title()}")
        print(self.win(user, computer))

    #or main()    
    def play(self):
        user_choice, computer_choice = self.get_user_and_computer_choice()
        self.print_result(user_choice, computer_choice)

if __name__ == "__main__":
    game = RockPaperScissor()

    while True:
        game.play()
        continue_game = input("Do you want to play again? (y/n): ")
        if continue_game == 'n':
            break

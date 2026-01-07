import random
from typing import List

class NumberGuessingGame:

    def __init__(self, max_value: int = 1000):
        self.max_value = max_value
        self.secretNumber = random.randint(1, max_value)
        self.list: List[int] = []
        self.isFinished = False

    def make_guess(self, guess: int) -> str:

        if self.isFinished:
            return "The game is already finished. Please start a new game."
        
        if not 1 <= guess <= self.max_value:
            return f"Please enter a number between 1 and {self.max_value}."
        
        self.list.append(guess)

        if guess == self.secretNumber:
            self.isFinished = True
            return "correct"
        elif guess > self.secretNumber:
            return "high"
        else:
            return "low"
        

    def tamanhoLista (self) -> int:
        return len(self.list)
    

def run_game(): 

    game = NumberGuessingGame()

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {game.max_value}. Can you guess it?")

    while not game.isFinished:
        try:
            number = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        response = game.make_guess(number)

        if response == "high":
            print("Your guess is too high. Try again!")
        elif response == "low":
            print("Your guess is too low. Try again!")
        elif response == "correct":
            print("Congratulations! You've guessed the correct number!")    
            print(f"You made {game.tamanhoLista()} attempts.")
            print("Your guesses were:", game.list)
        else:
            print(response)

if __name__ == "__main__":
    run_game()
import random
import os
import json
from typing import List, Dict

class HangmanGame:
    def __init__(self):
        # Word lists categorized by difficulty
        self.word_categories = {
            'easy': [
                'python', 'code', 'game', 'play', 'fun', 
                'hello', 'world', 'smile', 'happy', 'cat'
            ],
            'medium': [
               
                'computer', 'program', 'challenge', 'learning', 
                'algorithm', 'software', 'network', 'system'
            ],
            'hard': [
                'algorithm', 'cryptography', 'sophisticated', 
                'engineering', 'artificial', 'intelligence'
            ]
        }

        # ASCII art for hangman stages
        self.hangman_stages = [
            '''
             +---+
             |   |
                 |
                 |
                 |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
                 |
                 |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
             |   |
                 |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
            =========''',
            '''
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
            ========='''
        ]

        # Game configuration
        self.max_attempts = 6
        self.current_difficulty = 'medium'

    def clear_screen(self):
        """
        Clear the console screen for a better game experience.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def select_difficulty(self) -> str:
        
        while True:
            print("\nSelect Difficulty:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            difficulty_map = {
                '1': 'easy',
                '2': 'medium',
                '3': 'hard'
            }
            
            if choice in difficulty_map:
                return difficulty_map[choice]
            
            print("Invalid choice. Please try again.")

    def choose_word(self, difficulty: str) -> str:
        
        return random.choice(self.word_categories[difficulty])

    def display_word(self, word: str, guessed_letters: List[str]) -> str:
        
        return ' '.join(
            letter if letter in guessed_letters else '_' 
            for letter in word
        )

    def play(self):
        """
        Main game loop for Hangman.
        """
        while True:
            self.clear_screen()
            print("===== HANGMAN GAME =====")
            
            # Select difficulty
            difficulty = self.select_difficulty()
            
            # Choose word
            word = self.choose_word(difficulty)
            guessed_letters = set()
            incorrect_guesses = 0
            
            while incorrect_guesses < self.max_attempts:
                # Display current game state
                print("\n" + self.hangman_stages[incorrect_guesses])
                print("\nWord: " + self.display_word(word, guessed_letters))
                print(f"Attempts Left: {self.max_attempts - incorrect_guesses}")
                print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
                
                # Get player guess
                guess = input("\nGuess a letter: ").lower().strip()
                
                # Validate input
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single letter.")
                    input("Press Enter to continue...")
                    continue
                
                # Check guess
                if guess in guessed_letters:
                    print("You already guessed that letter!")
                    input("Press Enter to continue...")
                    continue
                
                guessed_letters.add(guess)
                
                if guess not in word:
                    incorrect_guesses += 1
                    print("Incorrect guess!")
                
                # Check win condition
                if set(word) <= guessed_letters:
                    self.clear_screen()
                    print("\n=== CONGRATULATIONS! ===")
                    print(f"You guessed the word: {word}")
                    break
                
                # Check lose condition
                if incorrect_guesses == self.max_attempts:
                    self.clear_screen()
                    print("\n=== GAME OVER! ===")
                    print(f"The word was: {word}")
                    break
            
            # Play again prompt
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        
        print("\nThanks for playing Hangman!")

def main():
    game = HangmanGame()
    game.play()

if __name__ == "__main__":
    main()

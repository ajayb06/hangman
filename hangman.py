import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_lives = num_lives
        self.letters_tried = set()
        print(f"The mystery word has {len(self.word)} characters: {' '.join(self.word_guessed)}")

    def guess_letter(self, letter):
        if letter in self.letters_tried:
            return f"You have already tried '{letter}'. Try another letter."
        
        self.letters_tried.add(letter)
        if letter in self.word:
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
            return "Correct!"
        else:
            self.num_lives -= 1
            return f"Wrong! You have {self.num_lives} lives left."

    def is_finished(self):
        return '_' not in self.word_guessed or self.num_lives <= 0

    def display_state(self):
        return ' '.join(self.word_guessed)

def get_user_input():
    return input("Enter a letter: ").lower()

def play_game(word_list):
    game = Hangman(word_list)
    while not game.is_finished():
        print(game.display_state())
        user_input = get_user_input()
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please, enter just one alphabetic character.")
            continue
        print(game.guess_letter(user_input))
    
    if '_' not in game.word_guessed:
        print(f"Congratulations! You guessed the word: {game.word}")
    else:
        print(f"You lost! The word was '{game.word}'.")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)


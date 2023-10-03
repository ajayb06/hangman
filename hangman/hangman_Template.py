import random

# Create a Hangman class to represent the game
class Hangman:

    # Constructor initializes the game
    def __init__(self, word_list, num_lives=5):
        # Choose a random word from the provided list and convert it to lowercase
        self.word = random.choice(word_list).lower()
        # Initialize a list to represent the word being guessed with underscores
        self.word_guessed = ['_'] * len(self.word)
        # Count the number of unique letters in the word
        self.num_letters = len(set(self.word))
        # Set the number of lives for the game
        self.num_lives = num_lives
        # Initialize a list to keep track of letters that have been tried
        self.list_letters_tried = []
        # Print the initial message with the number of characters in the word
        print(f"The mystery word has {self.num_letters} characters")
        # Display the initial state of the word being guessed with underscores
        print(' '.join(self.word_guessed))

    # Method to check if a guessed letter is in the word
    def check_letter(self, letter):
        if letter in self.word:
            # If the letter is in the word, replace underscores with the letter
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            # Decrement the count of unique letters in the word
            self.num_letters -= 1
        else:
            # If the letter is not in the word, decrement the number of lives
            self.num_lives -= 1

    # Method to ask the player for a letter
    def ask_letter(self):
        while True:
            letter = input("Enter a letter: ").lower()  # Convert input to lowercase
            if len(letter) != 1:
                print("Please, enter just one character")
                continue
            if letter in self.list_letters_tried:
                print(f"{letter} was already tried")
                continue
            # Check if the guessed letter is in the word
            self.check_letter(letter)
            # Add the guessed letter to the list of tried letters
            self.list_letters_tried.append(letter)
            # Display the current state of the word being guessed
            print(' '.join(self.word_guessed))
            break

# Function to play the Hangman game
def play_game(word_list):
    # Create a Hangman game instance
    game = Hangman(word_list, num_lives=5)

    # Continue the game until either the player wins or runs out of lives
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()

    # Check the game outcome and print the corresponding message
    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was '{game.word}'")

# Entry point of the program
if __name__ == '__main__':
    # Define a list of words for the game
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    # Start the Hangman game
    play_game(word_list)

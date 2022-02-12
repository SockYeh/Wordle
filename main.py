import random, requests
from colored import bg, attr, fg
from bs4 import BeautifulSoup


class Wordle:
    def __init__(self):
        self.guesses = 6
        self.guessed = "None"
        self.word = self.assign_word()
        self.start_game()

    def assign_word(self):
        r = requests.get("https://www.thefreedictionary.com/5-letter-words.htm")
        soup = BeautifulSoup(r.text, "html.parser")
        wordsl = soup.find("div", "TCont")
        for words in wordsl:
            words = [word.text.upper() for word in words.children]
            return random.choice(words)

    def grey(self, text):
        return f"{fg(0)}{bg(241)} {text} {attr(0)} "

    def yellow(self, text):
        return f"{fg(0)}{bg(3)} {text} {attr(0)} "

    def green(self, text):
        return f"{fg(0)}{bg(10)} {text} {attr(0)} "

    def display_board(self):

        if self.guessed == self.word:
            print("".join(self.green(letter) for letter in self.word))
            print("Congrats! You Won!")
            self.guesses = 0
            return
        for index, letter in enumerate(self.guessed):
            letter = letter.upper()

            if letter in list(self.word) and list(self.word)[index] == letter:
                print(self.green(letter.upper()), end="")
            elif letter in list(self.word) and list(self.word)[index] != letter:
                print(self.yellow(letter.upper()), end="")
            else:
                print(self.grey(letter.upper()), end="")
        print()

    def start_game(self):
        print(f"Welcome to Wordle!")
        print(f"Guess a 5 letter word!")
        print(f"You have 6 guesses!")
        print(f"Good Luck!")
        while self.guesses != 0:
            if self.guesses != 6:
                self.display_board()
            if self.guesses == 0:
                break
            while True:
                guess = input("Guess: ")
                if len(guess) == 5:
                    break
                else:
                    print("Please enter a 5 letter word!")
            self.guessed = guess
            self.guesses -= 1


Wordle()

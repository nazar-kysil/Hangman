import random

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guesses = []
        self.misses = 0

    def guess(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            print('Please enter a letter only!')
            return
        if letter in self.guesses:
            print('You already guessed this letter!')
            return
        self.guesses.append(letter)
        if letter not in self.word:
            self.misses += 1
            print('You missed this letter!')
            return

    def display(self):
        result = ''
        for i in self.word:
            if i not in self.guesses:
                result += '.'
            else:
                result += i
        return result.strip()

def get_random_word():
    with open('words.txt', 'r') as f:
        word = f.read().splitlines()
    return random.choice(word)

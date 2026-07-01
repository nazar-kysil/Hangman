# This is the main file to start the game
# You may add any additional modules and other files you wish

from hangman import Hangman
from hangman import get_random_word
from art import art
from new_game_option import new_game

word = get_random_word()
max_mistakes = 6
game = Hangman(word)

print('Welcome to Hangman!')
while True:
    print(art[game.misses])
    print(f'\nThe guessed word is {game.display()}')
    print(f'You have {max_mistakes - game.misses} guesses left')
    if '.' not in game.display():
        print('You have guessed the word!')
        if new_game():
            word = get_random_word()
            game = Hangman(word)
            continue
    elif game.misses == max_mistakes:
        print('You have lost the game!')
        print(f'The word was {game.word.upper()}')
        if new_game():
            word = get_random_word()
            game = Hangman(word)
            continue
        else:
            print('Thanks for playing!')
            break
    guess = input('Guess a letter: ')
    game.guess(guess)



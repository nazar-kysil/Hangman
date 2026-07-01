def new_game():
    choice = input('Would you like to play again? (y/n): ').lower()
    while choice not in 'yn':
        choice = input('Please enter y or n ').lower()
    return choice == 'y'
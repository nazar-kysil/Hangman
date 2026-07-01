The goal of the project was to write a hangman game. The program randomly draw a word from some set
and then show the template in the form: `......`, where each dot corresponds to an unknown letter.
In subsequent turns the player guesses letters. He wins when he guesses the whole word and losses when
the maximum number of mistakes is reached.

In every time the program show a template with uncovered letters (`..a..t.`) and indicate the number
of mistakes so far.

- verification of the correctness of the entered character: only one character entered, it is a letter,
  the letter has not been entered before;

- possibility of giving both lowercase and uppercase letters;

- a separate list of words, loaded from a file;

- ASCII art improves the game process.

The main file is `main.py`.

<img width="194" height="259" alt="1" src="https://github.com/user-attachments/assets/3e1aed94-4ec7-43cf-a744-61e877a80ca7" />
<img width="215" height="233" alt="2" src="https://github.com/user-attachments/assets/f00cd890-a194-462b-afc1-9944b409a39a" />
<img width="242" height="280" alt="3" src="https://github.com/user-attachments/assets/d56d9d1c-ae9d-43eb-bc9b-7f46b5094938" />

def print_welcome_screen(max_tries):
    """
    This function prints the welcome screen and num of tries.
    :param max_tries: num of wrong guesses that user can make
    :type max_tries: int
    :return: none
    """
    print(TGREEN + """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/  By Konyshev S.
""" + str(max_tries), ENDC)


def path_input_and_validation():
    """
    This function gets path from user and validates it.
    :return: validated path to the file
    :rtype: str
    """
    while True:
        try:
            path = input("Enter path:")
            open(path, 'r')
        except FileNotFoundError:
            print("File not found. Try again.")
        else:
            break
    return path


def num_input_and_validation():
    """
    This function gets num from user, validates it and casts to integer.
    :return: integer
    :rtype: int
    """
    while True:
        try:
            num = int(input("Enter index:"))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            break
    return num


def choose_word(file_path, index):
    """
    This function makes a list of unique words from the file.
    :param file_path: path to the file with words
    :type file_path: str
    :param index: index of the word in the file
    :type index: int
    :return: one word from the file
    :rtype: str
    """
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    words = []
    for word in text.split(' '):
        if word not in words:
            words.append(word)
    while index > len(words):
        index -= len(words)
    return words[index - 1].lower()


def print_hangman_and_the_word(first_print):
    """
    This function prints the hangman photo and shows the hidden word.
    :return: none
    """
    print(first_print + TRED + HANGMAN_PHOTOS[num_of_tries], ENDC + "\n" + show_hidden_word(secret_word, old_letters))


def check_win(word_to_guess, old_letters_guessed):
    """
    This function checks if the user wins.
    :param word_to_guess: word that user needs to guess
    :type word_to_guess: str
    :param old_letters_guessed: list of letters that user already guessed
    :type old_letters_guessed: list
    :return: bool whether  user wins or not
    :rtype: bool
    """
    word = ''
    for letter in word_to_guess:
        if not (letter in old_letters_guessed):
            break
        word = word + letter
    if word_to_guess == word:
        return True
    else:
        return False


def show_hidden_word(word_to_guess, old_letters_guessed):
    """
    This function shows the hidden words and the guessed letters that in this word.
    :param word_to_guess: word that user needs to guess
    :type word_to_guess: str
    :param old_letters_guessed: list of letters that user already guessed
    :type old_letters_guessed: list
    :return: ready to print word made from "_" and letters
    :rtype: str
    """
    word = ''
    for letter in word_to_guess:
        if letter in old_letters_guessed:
            word = word + ' ' + letter
            continue
        word = word + " _"
    return word


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks validation of users last guessed letter.
    :param letter_guessed: users last guessed letter
    :type letter_guessed: str
    :param old_letters_guessed: list of letters that user already guessed
    :type old_letters_guessed: list
    :return: bool whether users last guessed latter is valid or not
    :rtype: bool
    """
    english_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    if len(letter_guessed) > 1:
        return False
    elif letter_guessed not in english_alphabet:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function adds last guessed letter to the list of guessed letters
    if it was validate, if not prints "X' and all guessed letters.
    :param letter_guessed: users last guessed letter
    :type letter_guessed: str
    :param old_letters_guessed: list of letters that user already guessed
    :type old_letters_guessed: list
    :return: bool whether users last guessed latter is valid or not
    :rtype: bool
    """
    old_letters_guessed.sort()
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(*old_letters_guessed, sep=' -> ')
        return False
    else:
        old_letters.append(letter_guessed)
        return True


def check_the_guess(letter_guessed, word_to_guess):
    """
    This function checks if the last guessed word is in the secret word
    and prints updated hidden word updated hangman
    :param word_to_guess: word that user needs to guess
    :type word_to_guess: str
    :param letter_guessed: users last guessed letter
    :type letter_guessed: str
    :return: non
    """
    global num_of_tries
    if letter_guessed in word_to_guess:
        print(show_hidden_word(word_to_guess, old_letters))
    else:
        num_of_tries = num_of_tries + 1
        print_hangman_and_the_word(":-(\n\n")


TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults

HANGMAN_PHOTOS = {0: "    x-------x", 1: """    x-------x
    |
    |
    |
    |
    |""", 2: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}
num_of_tries = 0
MAX_TRIES = 6
old_letters = []
secret_word = ''


def main():
    global secret_word
    print_welcome_screen(MAX_TRIES)
    secret_word = choose_word(path_input_and_validation(), num_input_and_validation())
    print_hangman_and_the_word("\nLet’s start!\n\n")
    while not check_win(secret_word, old_letters):
        letter_guessed = input('\nPlease enter a letter:').lower()
        while not try_update_letter_guessed(letter_guessed, old_letters):
            letter_guessed = input('\nPlease enter a letter:').lower()
        check_the_guess(letter_guessed, secret_word)
        if num_of_tries == MAX_TRIES:
            print("You lose! The secret word was: " + secret_word)
            break
    if check_win(secret_word, old_letters):
        print(TGREEN + "You win!", ENDC)


if __name__ == '__main__':
    main()

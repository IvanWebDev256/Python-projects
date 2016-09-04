import random


def generate_word():
    words = [
        "pizza",
        "cake",
        "fish"
    ]
    word = words[random.randint(0, len(words) - 1)]
    return word


def show_word(word):
    for character in word:
        print(character, " ", end="")
    print()


def get_guess():
    print("Enter a letter: ")
    return input()


def process_letter(letter, secret_word, blanked_word):
    found = False
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter and blanked_word[i] != letter:
            found = True
            blanked_word[i] = letter
            break
    return found


def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X", end="")
    print()


def play_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = generate_word()
    blanked_word = list("_" * len(word))
    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)
        if not found:
            strikes += 1
            print_strikes(strikes)
        if strikes >= max_strikes:
            playing = False
        if "_" not in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("You lose!!!")
    else:
        print("You win")
    message = "A word: {0}"
    print(message.format(word))


print("Game started")
play_game()



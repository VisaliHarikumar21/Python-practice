# Hangman game
import random
from wordlist import words
MAX_WRONG = 6

print("****************************************************")
print("                      HANGMAN GAME                  ")
print("****************************************************")

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "/  "),
    6: (" O ",
        "/|\\",
        "/ \\"),
}

def display_man(wrong_guesses):
    print("****************************************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************************************************")

def display_hint(hint):
    print(f"HINT: {''.join(hint)}")

def display_answer(answer):
    return answer

def main():
    answer = random.choice(words)
    is_running = True
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed = set()

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter to guess: ").lower()

        if guess in guessed:
            print(f"{guess} is already guessed. Try a new guess!")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input")
            continue

        if guess in answer:
            print("Valid guess")
            guessed.add(guess)
            for idx in range(len(answer)):
                if answer[idx] == guess:
                    hint[idx] = guess
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You win!")
                break
            display_hint(hint)
        else:
            wrong_guesses += 1
            if wrong_guesses == MAX_WRONG:
                print("****************************************************")
                print("               GAME OVER! You lose!                 ")
                print(f"The correct answer is {display_answer(answer)}     ")
                print("****************************************************")
                break
            display_man(wrong_guesses)

if __name__ == "__main__":
    main()
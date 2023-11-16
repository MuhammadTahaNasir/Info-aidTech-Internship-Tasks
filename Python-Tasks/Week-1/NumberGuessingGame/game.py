import random
import starting

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 10


def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return


def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"Congratulations! You've guessed the correct number, which was {answer}.")
        return 0


def game():
    print(starting.logo)
    name = input("What's your name? ")
    print(f"Hello, {name}! I've selected a random number between 1 and 100. Try to guess it within 10 attempts.")
    answer = random.randint(1, 100)

    while True:
        level = input("Choose level of difficulty... Type 'easy' or 'hard': ")
        attempts = set_difficulty(level)
        if attempts == EASY_LEVEL_ATTEMPTS or attempts == HARD_LEVEL_ATTEMPTS:
            break
        else:
            print("You have entered the wrong difficulty level. Play again!")

    guessed_number = 0
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:
            print(f"Sorry, {name}. You've run out of attempts. The correct number was {answer}.")

    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    play_again = play_again_input == 'yes'

    print("Thanks for playing!")

    while play_again:
        game()


game()



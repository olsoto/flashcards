from flashcard import Flashcard
import time
import random

def main():
    score = 0

    cards = [
        Flashcard("2 + 2", "4"),
        Flashcard("1 + 2", "3"),
        Flashcard("3 + 4", "7"),
        Flashcard("7 + 1", "8")
    ]

    while True: 
        random.shuffle(cards)
        for card in cards:
            print(card.get_question())
            input("Press ENTER to show answer ")
            print(card.get_answer())
            answer = input("Did you get it right? (y/n) ")
            if (answer == 'y'):
                score += 1
            time.sleep(1)
            print()

        replay = input("Do you wish to study again? (y/n) ")
        print()
        if replay == 'n':
            print("Session ended.")
            print(f"Your final score was {score}!")
            return
        else:
            print(f"New session. Your current score is {score}!")


if __name__ == "__main__":
    main()
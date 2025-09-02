from flashcard import Flashcard
import time
import random

def main():
    score = 0
    cards = []

    version = input("Type 'f' to use input file for flashcards, or 'm' to manually enter flashcards ")
    while (version != "f" and version != "m"):
        print("That is not a valid input!")
        version = input("Type 'f' to use input file for flashcards, or 'm' to manually enter flashcards ")
    
    while version == "f":
        filename = input("Enter the name of the file to be scanned: ")
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    card = line.split(",")
                    cards.append(Flashcard(card[0], card[1]))
                break
        except FileNotFoundError:
            print("Invalid file name!")
    
    while version == "m":
        print("Enter a flashcard in format: '(question), (answer)' OR enter 'q' once completed.")
        line = input().strip()
        if not line:
            continue
        if line.lower() == "q":
            break
        if "," not in line:
            print("Missing comma. Please use '(question), (answer)'.")
            continue
        q, a = [s.strip() for s in line.split(",", 1)]
        if not q or not a:
            print("Both question and answer must be non-empty.")
            continue
        cards.append(Flashcard(q,a))


    while True: 
        random.shuffle(cards)
        print()
        print("Shuffling cards and starting session.")
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
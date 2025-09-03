from flashcard import Flashcard
import time
import random

def main():
    score = 0
    cards = []

    version = input("Type 'f' to use input file for flashcards, or 'm' to manually enter flashcards \n")
    while (version != "f" and version != "m"):
        print("That is not a valid input!")
        version = input("Type 'f' to use input file for flashcards, or 'm' to manually enter flashcards \n")
    
    while version == "f":
        filename = input("Enter the name of the file to be scanned: ")
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    q, a = [s.strip() for s in line.split(",", 1)]
                    cards.append(Flashcard(q, a))
                print("File successfully scanned. Launching session. \n")
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
        missed_cards = [] 
        random.shuffle(cards)
        print()
        print("Shuffling cards and starting session...")
        for card in cards:
            print(card.get_question())
            input("Press ENTER to show answer ")
            print(card.get_answer())
            answer = input("Did you get it right? (y/n) ")
            if (answer == 'y'):
                score += 1
            elif (answer == 'n'):
                missed_cards.append(card)
            time.sleep(1)
            print()
        

        if len(missed_cards) > 0:
            replay = input("Do you want to study your missed cards? (y/n) ")
            print()
            if replay == 'n':
                print("Session ended.")
                print(f"Your final score was {score}!")
            else:
                print(f"Reviewing missed cards...")
                cards = missed_cards
                continue
        
        replay = input("Do you want to start a new session? (y/n) ")
        if replay == "y":
            print()
            main()
        else:
            print("Game over! ")
            break


if __name__ == "__main__":
    main()
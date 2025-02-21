Word = "cola"
Chance = 5
guessed_word = ["_"] * len(Word)
guessed_letters = set()

def guess():
    global Chance
    while Chance > 0 and "_" in guessed_word:
        a = input("Guess a letter:").strip().lower()
        if a in guessed_letters:
            print(f"You already guessed '{a}'. Try a different letter.")
            continue
        guessed_letters.add(a)
        if a in Word :
            print("You have guessed one letter right", a)
            for i, letter in enumerate(Word):
                if letter == a :
                    guessed_word[i] = a
                    # guessed_word.append(a)
            print("So far:", " ".join(guessed_word))
            # print("Guess the next letter: ")

        else:
            print("You have guessed it wrong")
            Chance = Chance - 1
            print(f"You have {Chance} chances left")

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", Word)
            return
    if Chance == 0:
        print("Game Over! The word was:", Word)

print("Welcome to the guess the word game")
guess()


#Alternate Code
# word = "Hablu"
# chances = 5
# GuessAdd = []
# done = False
# while not done:
#     for letter in word:
#         if letter.lower() in GuessAdd:
#             print(letter, end = " ")
#         else:
#             print("_", end = " ")
#     MyGuess = input(f"Your chances is {chances}, Guess the letter: ")
#     GuessAdd.append((MyGuess.lower()))
#     if MyGuess.lower() not in word.lower():
#         chances -= 1
#         if chances == 0:
#             break
#     done = True
#     for letter in word:
#         if letter.lower() not in GuessAdd:
#             done = False
# if done:
#     print(f"Yes, you have won the game, the word is {word} ")
# else:
#     print("You have lost the game")
#

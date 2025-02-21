import random

print("Welcome to dice rolling game")
a = input("Let's begin with the first roll: Yes/No").strip().lower()
if a == "yes":
    dicerolling = True
    while dicerolling :
        print(random.randint(1,6))
        b = input("Do you want to roll again? Yes/No").strip().lower()
        if b == "yes" :
            continue
        else:
            print("The game has ended")
            break
else:
    print("The game has ended")

# import random
#
# print("Welcome to dice rolling game")
# a = input("Let's begin with the first roll: Yes/No").strip().lower()
# if a == "yes":
#     for i in range(1000):  # Arbitrary large number
#         print(random.randint(1, 6))
#         b = input("Do you want to roll again? Yes/No").strip().lower()
#         if b != "yes":
#             print("The game has ended")
#             break
# else:
#     print("The game has ended")

# import random
#
# def roll_dice():
#     print(random.randint(1, 6))
#     b = input("Do you want to roll again? Yes/No").strip().lower()
#     if b == "yes":
#         roll_dice()  # Calls itself again
#     else:
#         print("The game has ended")
#
# print("Welcome to dice rolling game")
# a = input("Let's begin with the first roll: Yes/No").strip().lower()
# if a == "yes":
#     roll_dice()
# else:
#     print("The game has ended")

# def countdown(n):
#     if n == 0:
#         print("Blast off!")
#         return
#     else:
#         print(n)
#         countdown(n - 1)  # Recursive call
#
# print("Starting countdown...")
# countdown(5)

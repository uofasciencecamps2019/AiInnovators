import random

print("Welcome to Hacking!\nTry guessing the password from the following list. \nGood luck!\n")

passwords = ["cool", "password", "spy", "mission"]
index = random.randint(0,4)
tries = 3

for word in passwords:
    print(word)
print("\n")

while tries > 0:
    guess = input("Enter your guess: ")
    if passwords[index] == guess:
        print("Congrats! You hacked the password")
        break
    else:
        tries = tries - 1
        print("\nNot quite right, try again")
        if tries > 0:
            print("You have " + str(tries) + " tries left\n")
        else:
            print("Game over")
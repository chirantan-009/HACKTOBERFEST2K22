import random
number = random.randint(1, 100)
print("Number of guesses is limited to only 9 times")
number_of_guesses = 1
while number_of_guesses <= 9:
    guess_number = int(input("guess the number"))
    if guess_number < number:
        print("Too Low")
    elif guess_number > number:
        print("Too High")
    else:
        print("You Won!!")
    print(9-number_of_guesses, "no. of guesses left")
    number_of_guesses += 1
if number_of_guesses > 9:
    print("Game Over")


import random

number_to_guess = random.randint(1,100)
while True:
    try:
        Guess = int(input("Guess The Number Between 1 and 100 : "))
        if(Guess < number_to_guess):
            print("Too Low!")

        elif(Guess > number_to_guess):
            print("Too High!")

        else:
            print("Congratulations ! You Guess The Number.")
            break

    except ValueError:
        print("Please Enter a Valid Number!")



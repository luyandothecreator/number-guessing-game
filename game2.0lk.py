import random

print("Welcome to the Guessing Game made by LUYANDO!")
number = random.randint(1, 5)  # computer picks a number

while True:  # loop forever until you break out
    guess = int(input("Guess a number between 1 and 5: "))
    
    if guess == number:
        print("🎉 You guessed it right!")
        break  # stop the loop when correct
    else:
        print("😅 Wrong guess, the number was==ran")
     
         
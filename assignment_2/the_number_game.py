# import random 

# random_num = random.randint(1 , 100)
# while True:
#  guess = int(input(f"Guess a number between 1 and 100 : "))
#  if guess < random_num:
#   print("you gueesed to low ")
#  elif guess > random_num:
#   print("you guessed to high")
#  else :
#   print(f"Congrates you guessed right")
  
#   while guess != random_num:
    





import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
      
    
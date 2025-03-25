# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).


try:
    inputs = input("What is your favorite animal? ")
    if inputs == "":
        raise NameError
    if inputs != str:
        raise NameError
    print(f"My favorite animal is also {inputs}!")
except NameError:
    print("Please enter a valid input")

def main():
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  
    quotient = str(quotient)
    remainder: int = dividend % divisor 
    remainder = str(remainder)
    
    print("The result of this division is " + (quotient) + " with a remainder of " + (remainder))


main()

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

    
length1 = input("Enter the length of first side of triangle : ")
length2 = input("Enter the length of second side of triangle : ")
length3 = input("Enter the length of third side of triangle : ")

length1 = float(length1)
length2 = float(length2)
length3 = float(length3)
    
perimeter = length1 + length2 + length3
            
print(f"The perimeter of the triangle is {perimeter}")
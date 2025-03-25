# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

feet :float = input("Enter value in Feet : ")
feet = float(feet)
inches = feet * 12.0
inches = float(inches)
inches  = round(inches, 2)
print("there are", inches, "inches in", feet, "feet")

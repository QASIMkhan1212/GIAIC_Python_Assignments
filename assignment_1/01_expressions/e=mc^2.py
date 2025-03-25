# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2

m = input("Enter kilos of mass:")
m = float(m)
c = 299792458
e = m * c**2
d = round(e, 3)
print("Energy equivalent of mass", m, "is", d)

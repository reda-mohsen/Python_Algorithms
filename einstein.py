"""
E=mc^2, wherein E represents energy (measured in Joules),
 m represents mass (measured in kilograms), and
 c represents the speed of light (measured approximately as 300000000 meters per second)

Prompts the user for mass as an integer (in kilograms)
 and then outputs the equivalent number of Joules as an integer.
 Assume that the user will input an integer.
"""
mass = int(input("Enter mass(in kilograms): "))
result = mass*(pow(300000000,2))
print(result)

<<<<<<< HEAD
import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
=======
import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
        print( filename)
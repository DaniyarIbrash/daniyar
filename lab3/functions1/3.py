<<<<<<< HEAD
def solve(numheads, numlegs):
    for chickens in range (1, numheads):
        for rabbits in range (1, numheads):
            solveproblem = 2*chickens + 4*rabbits
            if solveproblem == numlegs and chickens + rabbits == numheads:
                print(rabbits, chickens)
                exit(0)
=======
def solve(numheads, numlegs):
    for chickens in range (1, numheads):
        for rabbits in range (1, numheads):
            solveproblem = 2*chickens + 4*rabbits
            if solveproblem == numlegs and chickens + rabbits == numheads:
                print(rabbits, chickens)
                exit(0)
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
solve(int(input()), int(input()))
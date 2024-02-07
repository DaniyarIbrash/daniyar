<<<<<<< HEAD
import itertools 
def permut(s):
    perm = set(itertools.permutations(s))
    for i in perm:
        print(*i, sep='')
=======
import itertools 
def permut(s):
    perm = set(itertools.permutations(s))
    for i in perm:
        print(*i, sep='')
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
permut(input())
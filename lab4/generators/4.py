<<<<<<< HEAD
def sq(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
=======
def sq(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(list(sq(a,b)))
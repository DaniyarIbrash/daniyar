<<<<<<< HEAD
def gen(n):
    i=0
    while i<n:
        yield i**2
        i+=1
        
for i in gen(int(input())):
=======
def gen(n):
    i=0
    while i<n:
        yield i**2
        i+=1
        
for i in gen(int(input())):
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
    print(i)
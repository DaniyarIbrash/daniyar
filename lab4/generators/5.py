<<<<<<< HEAD
def down(n):
    i=n
    while i>0:
        yield i
        i-=1    
        if i==0:
            break
        
        
for i in down(int(input())):
=======
def down(n):
    i=n
    while i>0:
        yield i
        i-=1    
        if i==0:
            break
        
        
for i in down(int(input())):
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
    print(i)
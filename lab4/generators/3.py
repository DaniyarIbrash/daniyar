<<<<<<< HEAD
def div(n):
   for i in range(0,n+1):
       if i%3==0 and i%4==0:
           yield i
           
=======
def div(n):
   for i in range(0,n+1):
       if i%3==0 and i%4==0:
           yield i
           
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(list(div(int(input()))))
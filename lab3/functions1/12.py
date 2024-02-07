<<<<<<< HEAD
def histogram(a):
    for i in range(len(a)):
        a[i] = '*'*a[i]
    return a
=======
def histogram(a):
    for i in range(len(a)):
        a[i] = '*'*a[i]
    return a
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(*histogram(list(map(int, input().split()))),sep='\n')
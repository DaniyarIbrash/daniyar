<<<<<<< HEAD
def unique(a):
    c = []
    for i in a:
        if i not in c:
            c.append(i)
    return c
=======
def unique(a):
    c = []
    for i in a:
        if i not in c:
            c.append(i)
    return c
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(*unique(list(map(int,input().split()))))
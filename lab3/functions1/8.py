<<<<<<< HEAD
def spygame(a):
    s = ''
    for i in a:
        if i == 0 or i == 7: 
            s += str(i)
    if '007' in s:
        return True
    else: return False
=======
def spygame(a):
    s = ''
    for i in a:
        if i == 0 or i == 7: 
            s += str(i)
    if '007' in s:
        return True
    else: return False
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(spygame(list(map(int, input().split()))))
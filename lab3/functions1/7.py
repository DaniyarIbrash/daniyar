<<<<<<< HEAD
def has_33 (nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3 and i != len(nums) - 1:
            return True
    return False
=======
def has_33 (nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3 and i != len(nums) - 1:
            return True
    return False
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(has_33(list(map(int,input().split()))))
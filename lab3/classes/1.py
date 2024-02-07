<<<<<<< HEAD
class String:
    def __init__ (self):
        pass
    
    def get_string(self, string):
        self.string = string
    
    def print_string(self):
        return self.string.upper()
        
Mystr = String()
Mystr.get_string(input())
=======
class String:
    def __init__ (self):
        pass
    
    def get_string(self, string):
        self.string = string
    
    def print_string(self):
        return self.string.upper()
        
Mystr = String()
Mystr.get_string(input())
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(Mystr.print_string())
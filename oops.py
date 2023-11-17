# class Employee:
#     salary=89

# ram =Employee()

# print(ram.salary)

# -------------------------------------------------------------------------

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary    
    def getSalary(self):
        print( self.salary)
        
ram =Employee("shivam","9999999999")
print(ram.name)
print(ram.salary)
ram.getSalary()


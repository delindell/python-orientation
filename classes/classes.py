
# Blueprint / machine / recipe / template for making instance objects

# Base or parent class
class Employee:
    def __init__(self, name=''):
        self.name = name
        self.title = ''
        self.start_date = ''

    def payEmployee(self):
        print(f'we {self.name} pay rent now')

    def take_vacation(self):
        print(f'{self.name} takes a nice paid vacation')

    def __str__(self):
        return f"this is an employee name {self.name}"



# Child classes or derived
class ConstractEmployee(Employee):
    
    # We don't execute this dunder method
    def __init__(self, name='', wage=0):
        # call parents __init__
        super().__init__(name)
        self.hourly_wage = wage

    # method overridding
    def take_vacation(self):
        print(f'{self.name} took time off')

    

class SalariedEmployee(Employee):
    
    # We don't execute this dunder method
    def __init__(self, name, wage=0):
        super().__init__(name)
        self.hourly_wage = wage

    # def payEmployee(self):
    #     print(f'we {self.name} pay rent now')

    # def __str__(self):
    #     return f"this is an employee name {self.name}"


# An instance is a combo of predictable/repeated properties with unique values
fred = SalariedEmployee("fred")
fred.take_vacation()
# fred's value is an object
print(fred)

bubbs = ConstractEmployee('Bubba')
bubbs.take_vacation()

# linda = Employee('Linda', 'Boss', '01/23/1999')
# print(linda.title)

# linda.payEmployee()

# print(linda.__dict__)

class Company:

    def __init__(self, name, date, product):
        self.name = name
        self.date_founded = date
        self.product = product
        self.employees = []
    
    def addEmployees(self, employees):
        self.employees.extend(employees)

    def __str__(self):
        return f'{self.name} makes {self.product}'

widget_co = Company('Widget Co', '7/16/2020', 'the finest widgets')
print(widget_co)

widget_co.addEmployees([fred])

# print(widget_co.employees)

class Product():

    def __init__(self):
        # self.price = 0 <= we dont need this now
        self.title = ''
        self.desription = ''

    # decorator (getter)
    @property
    def price(self):
        try:
            return self.__price
        except AttributeError:
            return 0

    # setter
    @price.setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError('please provide a floating point value for price')



kite = Product()
# kite.price = 14.99
kite.title = 'A red kite'
kite.desription = 'Flies forever'
kite.price = 2.99
print(kite.price)

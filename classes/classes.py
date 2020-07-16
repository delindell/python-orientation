
# Blueprint / machine / recipe / template for making instance objects
class Employee:
    
    # We don't execute this dunder method
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def payEmployee(self):
        print(f'we {self.name} pay rent now')

    def __str__(self):
        return f"this is an employee name {self.name}"

# An instance is a combo of predictable/repeated properties with unique values
fred = Employee("fred", "supervisor", "01/02/2020")
# fred's value is an object
print(fred)

linda = Employee('Linda', 'Boss', '01/23/1999')
print(linda.title)

linda.payEmployee()

print(linda.__dict__)

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

print(widget_co.employees)

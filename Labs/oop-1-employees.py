class Employee:
    """Fill in the details"""

    def __init__(self, _name='John Doe', _title='nothing', _salary=0):
        self.__name = _name
        self.title = _title
        self.salary = _salary

    def __str__(self):
        return self.__name + ' ' + self.title + ' ' + str(self.salary)

    def get_name(self):
        """return the name of the employee"""
        return self.__name

    def set_salary(self, _salary):
        """Changes the salary of the employee"""
        self.salary = _salary


employee3 = Employee()
print(employee3)

scrooge_and_marley_employees = [(Employee("Bob Cratchit", 'clerk', 15)), (Employee('Ebenezer', 'founder', 1000))]
for employee in scrooge_and_marley_employees:
    print(employee.get_name())

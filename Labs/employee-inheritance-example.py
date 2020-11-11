class Employee:
    """Stores base attributes for an Employee"""

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return self.name + " (" + self.title + ") "

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getPay(self):
        return 0


class HourlyEmployee(Employee):
    """Extends the behavior of Employee class for an hourly employee"""

    def __init__(self, name, title):
        Employee.__init__(self, name, title)
        self.hourlyRate = 0
        self.hoursWorked = 0

    def setHourlyRate(self, rate):
        self.hourlyRate = rate

    def setHoursWorked(self, hours):
        self.hoursWorked = hours

    def getPay(self):
        return self.hourlyRate * self.hoursWorked


class SalariedEmployee(Employee):
    """Has a salary"""
    def __init__(self, name, title):
        Employee.__init__(self, name, title)
        self.salary = 0

    def setSalary(self, salary):
        self.salary = salary

    def getPay(self):
        return self.salary


class CommissionedEmployee(Employee):
    """Has a commission rate"""
    def __init__(self, name, title):
        Employee.__init__(self, name, title)
        self.base_salary = 0
        self.commission_rate_as_percent = 0
        self.sales_volume = 0

    def setBaseSalary(self, salary_dollars):
        self.base_salary = salary_dollars

    def setCommissionRate(self, commission_rate_as_percent):
        self.commission_rate_as_percent = commission_rate_as_percent

    def setSalesVolume(self, sales_volume):
        self.sales_volume = sales_volume

    def getPay(self):
        return self.base_salary + self.commission_rate_as_percent * self.sales_volume


zhiang = SalariedEmployee('Zhiang', 'TA')
zhiang.setSalary(1000)
ethan = HourlyEmployee('Ethan', 'Student Worker')
john_doe = CommissionedEmployee('JD', 'evangelist')
john_doe.setBaseSalary(1)
john_doe.setCommissionRate(10)
john_doe.setSalesVolume(5)

ethan.setHourlyRate(100)
ethan.setHoursWorked(10)

print(zhiang.getPay())
print(ethan.getPay())
print(john_doe.getPay())

print(Employee.__dict__)
print(SalariedEmployee.__dict__)
print(CommissionedEmployee.__dict__)
print(HourlyEmployee.__dict__)
print(zhiang.__dict__)
print(ethan.__dict__)
print(john_doe.__dict__)


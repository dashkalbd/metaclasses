class Employee:
    department = "IT"

    def describe(self):
        return self.department


employee = Employee()
print(employee.describe())

# employee is an instance (object). It was created by the class Employee.

print(type(employee))

# Employee is a class. It was created by the metaclass type.
print(type(Employee))

# type is a metaclass. It creates itself, so its type is also type.
print(type(type(Employee)))

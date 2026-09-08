from abc import ABC,abstractmethod
#abstraction
class employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    #encapsulation
    # getter   
    def get_salary(self):
        return self.__salary
    #setter with validation
    def set_salary(self,salary):
        if salary>=0:
            self.__salary=salary
        else:
            print("salary cannot be negative")
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def display(self):
        pass
    #inheritance
class developer(employee):
    #polymorephism/method overriding
    def work(self):
        print("developer writes code")
    def display(self):
        print("name:",self.name)
        print("role:developer")
        print("salary:",self.get_salary())
class manager(employee):
    def work(self):
        print("manager works team")
    def display(self):
        print("name:",self.name)
        print("role:mnager")
        print("salary:",self.get_salary())    
#employee management system
class EmployeeManagementSystem:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully")

    def display_all(self):
        if not self.employees:
            print("No employees found")
            return

        for employee in self.employees:
            employee.display()
            employee.work()
            print("--------------------")

    def update_salary(self, name, new_salary):
        for employee in self.employees:
            if employee.name == name:
                employee.set_salary(new_salary)
                print("Salary updated successfully")
                return

        print("Employee not found")

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("Employee removed successfully")
                return

        print("Employee not found")


# Objects
system = EmployeeManagementSystem()

developer1 = developer("Gayathri", 40000)
manager1 = manager("Ravi", 60000)

system.add_employee(developer1)
system.add_employee(manager1)

print("\nAll Employees:")
system.display_all()

print("\nUpdating salary:")
system.update_salary("Gayathri", 45000)

print("\nAfter salary update:")
system.display_all()

print("\nRemoving employee:")
system.remove_employee("Ravi")

print("\nAfter removing Ravi:")
system.display_all()

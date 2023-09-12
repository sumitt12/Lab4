class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search(self, param, value):
        results = []
        for employee in self.employees:
            if param == "Age" and employee.age == value:
                results.append(employee)
            elif param == "Name" and employee.name == value:
                results.append(employee)
            elif param == "Salary":
                operators = {
                    ">": employee.salary > value,
                    "<": employee.salary < value,
                    ">=": employee.salary >= value,
                    "<=": employee.salary <= value
                }
                if operators.get(">", False) or operators.get("<", False) or operators.get(">=", False) or operators.get("<=", False):
                    results.append(employee)
        return results

if __name__ == "__main__":
    database = EmployeeDatabase()
    
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("Search options:")
        print("1. Age")
        print("2. Name")
        print("3. Salary (>, <, <=, >=)")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            age = int(input("Enter age to search: "))
            results = database.search("Age", age)
        elif choice == "2":
            name = input("Enter name to search: ")
            results = database.search("Name", name)
        elif choice == "3":
            operator = input("Enter operator (>, <, <=, >=): ")
            salary = int(input("Enter salary to search: "))
            results = database.search("Salary", salary)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        if results:
            print("Search results:")
            for employee in results:
                print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
        else:
            print("No results found.")

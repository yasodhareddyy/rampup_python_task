class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")


class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# Function to get employee information with exception handling
def get_employee_info():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: $"))
            return emp_id, name, salary
        except ValueError:
            print("Invalid input. Please enter valid values for Employee ID, Name, and Salary.")


# Function to get manager information with exception handling
def get_manager_info():
    while True:
        try:
            emp_id, name, salary = get_employee_info()
            team_size = int(input("Enter Team Size: "))
            return emp_id, name, salary, team_size
        except ValueError:
            print("Invalid input. Please enter valid value for Team Size.")


# Function to get developer information with exception handling
def get_developer_info():
    while True:
        try:
            emp_id, name, salary = get_employee_info()
            programming_language = input("Enter Programming Language: ")
            return emp_id, name, salary, programming_language
        except ValueError:
            print("Invalid input. Please enter a valid value for Programming Language.")


# Create instances based on user input
while True:
    try:
        choice = int(input("Select an option:\n1. Add Employee\n2. Add Manager\n3. Add Developer\n4. Exit\nChoice: "))

        if choice == 1:
            employee1 = Employee(*get_employee_info())
            employee1.display_info()
        elif choice == 2:
            manager1 = Manager(*get_manager_info())
            manager1.display_info()
        elif choice == 3:
            developer1 = Developer(*get_developer_info())
            developer1.display_info()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")


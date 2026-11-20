import csv

def bonus(salary, rate=0.1, *extras, **options):
    total = (salary * rate) + sum(extras)
    if "cap" in options and total > options["cap"]:
        return options["cap"]
    return total

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Team: {self.team_size}"

emp_list = []
with open("data/employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["salary"] = int(row["salary"])
        emp_list.append(row)

above_50k = [e["name"] for e in emp_list if e["salary"] > 50000]
print("Above 50000:", above_50k)

raised_sal = list(map(lambda e: round(e["salary"] * 1.1, 2), emp_list))

chennai_emp = list(filter(lambda e: e["city"] == "Chennai", emp_list))
chennai_names = [e["name"] for e in chennai_emp]
print("Chennai:", chennai_names)

sal_checks = [e["salary"] for e in emp_list]
for s in sal_checks:
    if s == 0:
        continue
    if s > 85000:
        break

mgr = Manager("Divya", 75000, 5)
b_amt = bonus(50000, 0.1, 2000, 1000, cap=7000)

try:
    bad_emp = Employee("Test", -500)
except InvalidSalaryError as err:
    print("Error:", err)
finally:
    print("Transaction finished")
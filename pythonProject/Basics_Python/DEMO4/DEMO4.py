class Employee:

    def __init__(self, name, wage_per_hour):
        self.name = name
        self.wage = self.calculate_wage()
        self.wage_per_hour = wage_per_hour

    def calculate_wage(self):
        total_wage=10
        return total_wage


class Company:
    def __init__(self, name):
        self.name = name
        self.employee_dict = {}

    def display_emoployee(self):
        for employee_name, employee in self.employee_dict.items():
            print(employee_name, employee.name, employee.wage)

if __name__ == '__main__':
    emp1=input("Enter first employee name")
    emp2=input("Enter second employee name")

    employee1 = Employee(emp1, 10)
    employee2 = Employee(emp2, 20)

    # print(employee1.name)
    # print(employee2.name)
    # print(employee1.wage)
    # company = Company("tata")
    # company.employee_dict.update({employee1.name: employee1})
    # company.employee_dict.update({employee2.name: employee2})
    # print(company.employee_dict)
    # employee=company.employee_dict.get("monu")
    # print(employee)
    # company.display_emoployee()
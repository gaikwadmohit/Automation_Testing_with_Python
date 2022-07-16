import random

class EmployeeWage:

    def employee(self):

        try:
            wage_per_hour = 20
            daily_work_hour = 8
            rand = random.randint(0, 1)
            if rand == 0:
                print("Employee is present")
                daily_wage = daily_work_hour * wage_per_hour
                print(f"The total wage of a day : {daily_wage}")

            else:
                print("Employee is absent")
                daily_wage = daily_work_hour * 0
                print(f"The total wage of a day : {daily_wage}")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        obj = EmployeeWage()
        obj.employee()
    except Exception as e:
        print(e)
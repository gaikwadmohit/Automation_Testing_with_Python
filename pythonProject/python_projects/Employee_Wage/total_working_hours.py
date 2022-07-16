
import random


class EmployeeWage:
    def __init__(self, wage_per_hour, monthly_working_day, total_working_hour):
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.total_working_hour = total_working_hour

    def check_attendance(self,rand):

        try:
            if rand == 0:
                daily_work_hour = 8
                print(" Employee is present ")
            elif rand == 1:
                daily_work_hour = 4
                print(" Employee is present for part-time ")
            else:
                daily_work_hour = 0
                print(" Employee is absent ")
            return daily_work_hour
        except Exception as e:
            print(e)

    def calculating_wage(self):

        try:
            total_wage = 0
            no_of_working_days = 0
            working_hours = 0
            while no_of_working_days < self.monthly_working_day and working_hours <= self.total_working_hour:
                no_of_working_days += 1
                rand = random.randint(0, 2)
                print("------------------------------------------------")
                daily_work_hour = self.check_attendance(rand)
                print(f" The working days is : {no_of_working_days}")
                working_hours += daily_work_hour
                print(f" The working hours is : {working_hours}")
                daily_wage = self.wage_per_hour * daily_work_hour
                print(f" The daily wage is : {daily_wage}")
                total_wage += daily_wage
            print(f"The monthly wage is : {total_wage}")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        obj = EmployeeWage(20, 20, 100)
        obj.calculating_wage()
    except Exception as e:
        print(e)
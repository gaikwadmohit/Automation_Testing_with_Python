import random


class Employee:

    def __init__(self, wage_per_hour=20, full_time_hr=8, part_time_hr=4, max_hr=160, max_day=20):
        """
        here using constructor we are declaring global variables
        :param wage_per_hour:
        :param full_time_hr:
        :param part_time_hr:
        :param max_hr:
        :param max_day:
        """
        self.company_employee_wage_list = []
        self.wage_per_hour = wage_per_hour
        self.full_time_hr = full_time_hr
        self.part_time_hr = part_time_hr
        self.max_hr = max_hr
        self.max_day = max_day

    def calculate_employee_wage_pr_day(self, number):

        try:
            emp_check_dict = {1: self.full_time_hr, 2: self.part_time_hr, 0: 0}
            return emp_check_dict.get(number)
        except Exception as e:
            print(e)

    def calculating_wage_per_mnth(self):

        try:
            daily_wage_dict = {}
            total_hrs = 0
            total_days = 1

            while total_hrs <= self.max_hr and total_days <= self.max_day:
                number = random.randint(0, 2)
                work_hrs = self.calculate_employee_wage_pr_day(number)
                work_hrs_per_day = work_hrs
                daily_wage = work_hrs_per_day * self.wage_per_hour
                total_hrs += work_hrs_per_day
                daily_wage_dict.update({total_days: daily_wage})
                total_days += 1

            monthly_emp_wage = self.wage_per_hour * total_hrs

            return daily_wage_dict, monthly_emp_wage
        except Exception as e:
            print(e)


if __name__ == "__main__":

    emp1 = Employee()
    daily_wage_dict, monthly_emp_wage = emp1.calculating_wage_per_mnth()
    print(
         f"Person earns {monthly_emp_wage} rupees this month \nDaily Emp Wage daywise:\n{daily_wage_dict} respectively. ")
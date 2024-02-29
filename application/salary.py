
from datetime import date

ext_salary = []
def calculate_salary(self, days):
    salary = self.wage * days
    pay_day = date.today()
    ext_salary.append(salary)
    return salary, print(f'На {pay_day.strftime("%d/%m/%Y")} сотрудник {self.name} к получению: {salary}')


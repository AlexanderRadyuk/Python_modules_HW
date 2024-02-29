
from salary import calculate_salary, ext_salary
from people import people

import matplotlib.pyplot as plt
import seaborn as sns


class Employee:

    def __init__(self, name):
        self.name = name
        self.wage = people.get(name)

    def __str__(self):
        return f'{self.name} имеет ставку {self.wage}'


if __name__ == '__main__':
    worker_to_be_paid_1 = Employee('Иванов')
    worker_to_be_paid_2 = Employee('Петров')
    worker_to_be_paid_3 = Employee('Сидоров')



    accountant_list = [worker_to_be_paid_1, worker_to_be_paid_2, worker_to_be_paid_3]
    for pers_ in accountant_list:
        calculate_salary(pers_, 30)


    x = [worker_to_be_paid_1.name, worker_to_be_paid_2.name, worker_to_be_paid_3.name]
    y = [ext_salary[0], ext_salary[1], ext_salary[2]]


    sns.barplot(x=x, y=y);
    plt.show()

from datetime import datetime
import time


class Time:

    def __enter__(self):
        self.a = datetime.now()
        print(f'Время начала работы цикла {self.a}')

    def __exit__(self, exp_type, exp_value, traceback):
        self.b = datetime.now()
        print(f'Время окончания работы цикла {self.b}')
        print(f'Время работы цикла {self.b - self.a}')


try:
    counter = int(input('Введите количество итераций: '))
    with Time():
        for i in range(counter):
            time.sleep(0.1)
except ValueError as er:
    print('Вы ввели некоректные данные')




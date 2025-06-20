# Schedule generator
# Module name: Task_3

from datetime import datetime, timedelta

def main():
    print_hi()
    dates_list = []
    days = input('Введи кількість днів розкладу: ')
    work_days = input_verification_working_days(days)
    rest_days = input_verification_rest_days(days, work_days)
    schedule_start_date = input('Введи дату початку розкладу (yyyy-mm-dd):')
    adding_working_days(dates_list, schedule_start_date, days, work_days, rest_days)
    print('days:' + str(days) + ', work_days:' + str(work_days) + ', rest_days:' + str(rest_days) + ', start_date: datetime(' + schedule_start_date + ') ->')
    print('[')
    print("\n".join(map(str, dates_list)))
    print(']')


def input_verification_working_days(days):
    # Input and verification of working days
    while True:
        try:
            user_input = input('Введи кількість робочих днів: ')
            if (int(user_input) < int(days)) or (int(user_input) == int(days)):
                return user_input
                break
            else:
                print('Кількість робочих не може бути більша за кількість днів графіка!')
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть число.")

def input_verification_rest_days(days, work_days):
    # Input and verification of rest days
    while True:
        try:
            user_input = input('Введи кількість днів відпочинку: ')
            if (int(user_input) < (int(days) - int(work_days))) or (int(user_input) == (int(days) - int(work_days))):
                return user_input
                break
            else:
                print('Сума робочих днів та днів відпочинку не може бути більша за кількість днів графіка!')
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть число.")

def adding_working_days(dates_list, schedule_start_date, days, work_days, rest_days):
    schedule_days = days
    schedule_new_date = schedule_start_date
    while int(schedule_days) > 0:
        if int(work_days) > int(schedule_days):
            work_days = schedule_days
        dates_list.extend([datetime.strptime(schedule_new_date, "%Y-%m-%d") + timedelta(days=i) for i in range(int(work_days))])
        schedule_days = int(schedule_days) - int(work_days) - int(rest_days)
        schedule_new_date = dates_list[-1] + timedelta(days=int(rest_days) + 1)
        schedule_new_date = str(schedule_new_date.date())

def print_hi():
    print(f'Привіт!')

if __name__ == '__main__':
    main()
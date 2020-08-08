# Программа для ***
# Подсчет количества отсутсвия сотрудника на точке(время, раз)

import datetime


def welcome():
    print('''                                 
                                 Программа для ***.
                                 Пожалуйста начните работу.
                                 Введите R - reset, для перехода к слд. сотруднику.


                                                                           v.1
                                                                           ***                                                                                                                                                                                               
          ''')


def valid(arg):
    while True:
        if arg.isdigit():
            return int(arg)
        elif arg == 'R' or arg == 'r':
            valid_res()
            print('[NEXT] Готово! Переходим к следующему сотруднику.')
            return -1
        else:
            print('[Error] Ошибка! Введите корректные данные.')
            return -1


def valid_res():
    global res, score
    res = 0
    score = 0
    return res, score


def math(time_h, time_m, time_h2, time_m2):
    global res
    # Математическая часть, подсчёт
    t1 = datetime.timedelta(hours=time_h, minutes=time_m)
    t2 = datetime.timedelta(hours=time_h2, minutes=time_m2)

    delta = t2 - t1
    sec = delta.seconds
    res = res + sec

    minutes = (res % 3600) // 60
    hours = res // 3600
    return hours, minutes


def quest():
    # Iter for while
    valid_time_h = -1
    valid_time_m = -1

    while valid_time_h < 0:
        time_h = input('Введите первое значение времени H: ')
        valid_time_h = valid(time_h)
    while valid_time_m < 0:
        time_m = input('Введите первое значение времени M: ')
        valid_time_m = valid(time_m)
    return valid_time_h, valid_time_m


def quest_two():
    #Iter for while
    valid_time_h2 = -1
    valid_time_m2 = -1

    while valid_time_h2 < 0:
        time_h2 = input('Введите второе значение времени H: ')
        valid_time_h2 = valid(time_h2)
    while valid_time_m2 < 0:
        time_m2 = input('Введите второе значение времени M: ')
        valid_time_m2 = valid(time_m2)
    return valid_time_h2, valid_time_m2


def final_print(score, hours, minutes):
    print('Cотрудник отходил: %d time. %d hour %d minute' % (score, hours, minutes))


def main():
    global res, score
    res = 0
    score = 0
    welcome()
    while True:
        time_h, time_m = quest()
        time_h2, time_m2 = quest_two()
        hours, minutes = math(time_h, time_m, time_h2, time_m2)
        score += 1
        final_print(score, hours, minutes)


# Start program
main()






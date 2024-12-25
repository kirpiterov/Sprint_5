import random


def generate_reg_data():
    name = 'kirpit' + str(random.randint(1000, 999999))
    login = name + '@ya.ru'
    password = str(random.randint(100000,999999))
    return name, login, password


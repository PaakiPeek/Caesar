from random import *

# Начальные данные
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Приветствие
print('Умный генератор безопасных паролей.')
print('Задайте парамметры, под которые должен подходить пароль.')


# Защита ввода от любых нежелательных знаков
def defender(num):
    correct = False
    while not correct:
        if num.isdigit() and int(num) > 0:
            correct = True
            return int(num)
        elif num == '/help':
            print('Ввод должен быть исключительно положительным числом.')
            num = input('Введите корректное число: ')
            defender(num)
        else:
            print('Если вам нужна помощь, то введите команду "/help"')
            num = input('Введите корректное число: ')
            defender(num)


counts = defender(input('Сколько создать паролей: '))
length = defender(input('Какой длины: '))

di_yes = input('Включать ли в него цифры: ')
while di_yes.lower() != 'да' or di_yes.lower() != 'нет':
    if di_yes.lower() == 'да':
        chars += digits
        break
    elif di_yes.lower() == 'нет':
        break
    elif di_yes.lower() != 'да' or di_yes.lower() != 'нет':
        di_yes = input('Включать ли в него цифры: ')

lo_yes = input('Включать ли прописные буквы: ')
while lo_yes.lower() == 'да' or lo_yes.lower() == 'нет':
    if lo_yes.lower() == 'да':
        chars += lowercase_letters
        break
    elif lo_yes.lower() == 'нет':
        break
    elif lo_yes.lower() != 'да' or lo_yes.lower() != 'нет':
        lo_yes = input('Включать ли прописные буквы: ')

up_yes = input('Включать ли заглавные буквы: ')
while up_yes.lower() == 'да' or up_yes.lower() == 'нет':
    if up_yes.lower() == 'да':
        chars += uppercase_letters
        break
    elif up_yes.lower() == 'нет':
        break
    elif up_yes.lower() != 'да' or up_yes.lower() != 'нет':
        up_yes = input('Включать ли заглавные буквы: ')

pun_yes = input('Включать ли спец. символы: ')
while pun_yes.lower() == 'да' or pun_yes.lower() == 'нет':
    if pun_yes.lower() == 'да':
        chars += punctuation
        break
    elif pun_yes.lower() == 'нет':
        break
    elif pun_yes.lower() != 'да' or pun_yes.lower() != 'нет':
        pun_yes = input('Включать ли спец. символы: ')
chars = list(chars)
shuffle(chars)

def generate_password(length, chars):
def generate_password(length, chars):
    passwords = []
    for j in range(counts):
        s = ''
        for i in range(length):
            shuffle(chars)
            s += chars[i]
        passwords.append(s)
    return passwords


print('Ваши пароли: ', *generate_password(length, chars), sep = '\n')
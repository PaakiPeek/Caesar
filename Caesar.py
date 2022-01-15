eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

text = input('Введите текст: ')
leng = input('Введите язык текста ru/eng: ')

print(' Шифруем или дешифруем?')
answer = input('Введите h/d: ')

if leng.lower() == 'ru':
    listl = rus_lower_alphabet
    listu = rus_upper_alphabet
elif leng.lower() == 'eng':
    listl = eng_lower_alphabet
    listu = eng_upper_alphabet

if answer == 'h' and leng.lower() == 'ru':
    print('Вы выбрали "Шифруем".')
    def shifr(name):
        c = int(input('Введите код шифра (цифра): '))
        texth = list(name)
        for i in range(len(texth)):
            if texth[i] in listl:
                if listl.index(texth[i]) + c < 32:
                    texth[i] = listl[listl.index(texth[i]) + c]
                else:
                    texth[i] = listl[listl.index(texth[i]) + c - 32]

            elif texth[i] in listu:
                if listu.index(texth[i]) + c < 32:
                    texth[i] = listu[listu.index(texth[i]) + c]
                else:
                    texth[i] = listu[listu.index(texth[i]) + c - 32]
            else:
                continue
        return texth
    print(''.join(shifr(text)))
    print('Пойдет?')
    t = input('д/н: ')
    if t == 'н':
        while t == 'н':
            print(''.join(shifr(text)))
    else:
        print('Немец не пройдет!')

if answer == 'd' and leng.lower() == 'ru':
    print('Вы выбрали "Дешифруем".')
    def deshifr(name):
        c = int(input('Введите код шифра (цифра): '))
        texth = list(name)
        for i in range(len(texth)):
            if texth[i] in listl:
                if 0 <= listl.index(texth[i]) - c < 32:
                    texth[i] = listl[listl.index(texth[i]) - c]
                else:
                    texth[i] = listl[listl.index(texth[i]) - c +32]

            elif texth[i] in listu:
                if 0 <= listu.index(texth[i]) - c < 32:
                    texth[i] = listu[listu.index(texth[i]) - c]
                else:
                    texth[i] = listu[listu.index(texth[i]) - c + 32]
            else:
                continue
        return texth
    print(''.join(deshifr(text)))
    print('Пойдет?')
    t = input('д/н: ')
    if t == 'н':
        while t == 'н':
            print(''.join(deshifr(text)))
    else:
        print('Немец не пройдет!')


if answer == 'h' and leng.lower() == 'eng':
    print('Вы выбрали "Шифруем".')
    def shifr(name):
        c = int(input('Введите код шифра (цифра): '))
        texth = list(name)
        for i in range(len(texth)):
            if texth[i] in listl:
                if listl.index(texth[i]) + c < 26:
                    texth[i] = listl[listl.index(texth[i]) + c]
                else:
                    texth[i] = listl[listl.index(texth[i]) + c - 26]

            elif texth[i] in listu:
                if listu.index(texth[i]) + c < 26:
                    texth[i] = listu[listu.index(texth[i]) + c]
                else:
                    texth[i] = listu[listu.index(texth[i]) + c - 26]
            else:
                continue
        return texth
    print(''.join(shifr(text)))
    print('Пойдет?')
    t = input('y/n: ')
    if t == 'n':
        while t == 'n':
            print(''.join(shifr(text)))
    else:
        print('Немец не пройдет!')

if answer == 'd' and leng.lower() == 'eng':
    print('Вы выбрали "Дешифруем".')
    def deshifr(name):
        c = int(input('Введите код шифра (цифра): '))
        texth = list(name)
        for i in range(len(texth)):
            if texth[i] in listl:
                if 0 <= listl.index(texth[i]) - c < 26:
                    texth[i] = listl[listl.index(texth[i]) - c]
                else:
                    texth[i] = listl[listl.index(texth[i]) - c + 26]

            elif texth[i] in listu:
                if 0 <= listu.index(texth[i]) - c < 26:
                    texth[i] = listu[listu.index(texth[i]) - c]
                else:
                    texth[i] = listu[listu.index(texth[i]) - c + 26]
            else:
                continue
        return texth
    print(''.join(deshifr(text)))
    print('Пойдет?')
    t = input('y/n: ')
    if t == 'n':
        while t == 'n':
            print(''.join(deshifr(text)))
    else:
        print('Немец не пройдет!')

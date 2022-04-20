

if __name__ == '__main__':
    st = str(input('Введите строку: '))

    if len(st) == 0:
        print('Строка пустая')
        quit()

    count_zero = 0;
    count_one = 0;

    for i in st:
        if i == '0':
            count_zero += 1
        elif i == '1':
            count_one += 1

    if count_zero < count_one:
        print('Необходимо перевернуть', count_zero, 'монетки')
    elif count_zero > count_one:
        print('Необходимо перевернуть', count_one, 'монетки')
    else:
        print('Необходимо перевернуть', count_zero, 'монетки')

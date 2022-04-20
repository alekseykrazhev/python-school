

if __name__ == '__main__':
    st = str(input('Введите строку: '))
    a = str(input('Введите символ: '))

    if a in st:
        print('Символ', a, ' встречается в строке ', st)
    else:
        print('Символ', a, 'не встречается в строке', st)



if __name__ == '__main__':
    n = int(input('Введите число:'))
    b = int(input('Введите второе число:'))

    lower = -1
    found = False
    if n >= b:
        lower = b
    else:
        lower = n   

    for i in range (2, lower + 1):
        if n % i == 0 and b % i == 0:
            print ('Числа', n, 'и', b, 'не взаимно простые')
            found = True
            break

    if not found:
        print ('Числа', n, 'и', b, 'взаимно простые')
        
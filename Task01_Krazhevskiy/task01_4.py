

if __name__ == '__main__':
    n = int(input('Введите число: '))
    n_n = n
    d = 2
    s = 0

    while d ** 2 <= n:
        if n % d == 0:
            s += d
            n //= d
        else:
            d += 1

    if n > 1:
        s += n

    if s > 0:
        print ('Сумма простых делителей числа', n_n, 'равна', s)
    else:
        print ('Число', n_n, 'не имеет простых делителей')

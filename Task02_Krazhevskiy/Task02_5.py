
res = 0


def decimal_to_any(n, to):
    if n < to:
        print(n, end='')
    else:
        decimal_to_any(n//to, to)
        if (n % to) < 10:
            print(n % to, end='')
        else:
            print(chr(n % to + 55), end='')


def any_to_decimal(n, used, count = 0):
    if n >= used:
        any_to_decimal(n // used, used)
    print(n % 2, end='')


if __name__ == '__main__':
    used = str(input("Система счисления вводимого числа (числом):"))
    if used.isdigit():
        used = int(used)
    else:
        print("Введено не число")
        exit(-1)

    n = str(input("Введите число: "))
    if n.isdigit():
        n = int(n)
    else:
        print("Вы ввели не число")
        exit(-1)

    to = str(input("Введите нужную систему счисления (числом): "))
    if to.isdigit():
        to = int(to)
    else:
        print("Вы ввели не число")
        exit(-1)
    
    any_to_decimal(n, used)

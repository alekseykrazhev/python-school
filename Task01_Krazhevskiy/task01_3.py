

if __name__ == '__main__':
    n = str(input('Введите число: '))
    s = 0

    for i in n:
        if i != ',' and i != '.':
            s += int(i)
    
    print(s)

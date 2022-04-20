

def generate(n = -1):
    if n != -1:
        for i in range(1, n + 1):
            if i % 2 == 0:
                if i == 2: print(i)
            else:
                d = 3
                while d * d <= i and i % d != 0:
                    d += 2
                if d * d > i: print(i)
    else:
        i = 0

        while True:
            i += 1
            if i % 2 == 0:
                if i == 2: print(i)
            else:
                d = 3
                while d * d <= i and i % d != 0:
                    d += 2
                if d * d > i: print(i)


if __name__ == '__main__':
    n = str(input("Enter a number: "))

    if n.isdigit():
        generate(int(n))
    else:
        generate()

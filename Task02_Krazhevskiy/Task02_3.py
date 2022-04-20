

def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


def generate(n = -1):
    if n != -1:
        for i in range(1, n + 1):
            print(fact(i))
    else:
        i = 0
        while True:
            i += 1
            print(fact(i))


if __name__ == '__main__':
    n = str(input("Enter a number: "))

    if n.isdigit():
        generate(int(n))
    else:
        generate()

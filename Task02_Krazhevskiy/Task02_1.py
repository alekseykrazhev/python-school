

def generate(n = -1):
    if n != -1:

        for i in range(1, n + 1):
            if i % 2:
                print(f"{i} is odd")
            else:
                print(f"{i} is even")
    else:
        i = 0

        while True:
            i += 1
            if i % 2:
                print(f"{i} is odd")
            else:
                print(f"{i} is even")


if __name__ == '__main__':
    n = str(input("Enter a number: "))

    if n.isdigit():
        generate(int(n))
    else:
        generate()

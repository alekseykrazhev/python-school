

def isPalindrome(n):
    if n < 10:
        return True

    last = n % 10
    count = 0

    while n != 0:
        count += 1
        first = n % 10
        n = n // 10
        
    if first == last:
        return isPalindrome((n - (first * 10 ** (count - 1)) - last))

    return False


def generate(n = -1):
    if n != -1:
        for i in range(11, n + 1):
            if isPalindrome(i):
                print(i)
    else:
        i = 10
        while True:
            i += 1
            if isPalindrome(i):
                print(i)


if __name__ == '__main__':
    n = str(input("Enter a number: "))

    if n.isdigit():
        generate(int(n))
    else:
        generate()

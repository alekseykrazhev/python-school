

def any_to_decimal(n, used_base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = abs(n)
    b = alpha[num % used_base] 
    while num >= used_base :
        num //= used_base
        b += alpha[num % used_base] 
    return ('' if n >= 0 else '-') + b[::-1]


if __name__ == '__main__':
    used_base = int(input("Enter CS(number):"))
    n = input("Enter a number:")
    to_base = int(input("Enter to which CS(number)"))

    print(any_to_decimal(n, used_base))
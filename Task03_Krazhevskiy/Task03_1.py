

def decimal_to_any(number : float, base : int):
    sign = ''
    if number[0] == '-':
        sign = '-'
        #del number[0]

    if number == '0':
        return '0'

    before, after = number.split('.')
    ans = ''

    before = int(before)
    while before >= base:
        if before % base < 10:
            ans += str(before % base)
        else:
            ans += chr(before % base + 55)
        before //= base
    
    ans += str(before)
    ans = ans[::-1]
    ans += '.'

    count = 0
    after = float('0.' + after)
    while str(after).split('.')[1] != '0' and count < 20:
        count += 1
        after = '0.' + str(after).split('.')[1]
        after = float(after)
        after *= base
        int_part = str(after).split('.')[0]

        if after < 10:
            ans += str(int_part)
        else:
            ans += chr(int(int_part) + 55)

    if count < 1:
        ans += '0'

    return ans

    
def any_to_decimal(number, base : int):
    if '.' not in number:
        number += '.0'

    if base == 10:
        return number

    sign = ''
    if number[0] == '-':
        sign = '-'
        del number[0]

    if number == '0':
        return '0'

    before, after = number.split('.')
    ans = 0
    count = 1

    for char in before:
        if not char.isdigit():
            char = ord(char) - ord('A') + 10
        ans += int(char) * base ** (len(before) - count)
        count += 1
        
    count = 1
    for char in after:
        if not char.isdigit():
            char = ord(char) - ord('A') + 10
        ans += int(char) * base ** (-count)
        count += 1

    return sign + str(ans)


if __name__ == '__main__':
    used_base = int(input("Enter CS(number):"))
    n = (input("Enter a number:"))
    to_base = int(input("Enter to which CS(number)"))

    dec = any_to_decimal(n, used_base)
    print(f"{n} in decimal CS is {dec}")
    res = decimal_to_any(dec, to_base)
    print(f"{dec} in {to_base} CS is {res}")

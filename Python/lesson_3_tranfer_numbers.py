def convert_to_decimals(str_num, base):
    length = len(str_num)
    base = int(base)
    sum = 0
    for i in range(length):
        if base == 16 and str_num[i].isalpha():
            digit = ord(str_num[i].lower()) - 87
            sum += digit * base ** (length - i - 1)
        else:
            sum += int(str_num[i]) * base ** (length - i - 1)
    return sum


def conver_from_decimals(num, base):
    string = ""
    while num > 0:
        if num % base <= 9:
            string += str(num % base)
        else:
            string += chr(num % base + 55)
        num //= base
    return string[::-1]


print(conver_from_decimals(1000, 16))

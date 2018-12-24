"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


def reverse(x):
    if checkRange(x):
        num = abs(x)
        result = 0
        reverse_list = []
        while num > 0:
            reverse_list.append(num % 10)
            num = int(num / 10)
        for i in range(0, len(reverse_list)):
            result += reverse_list[i] * (10 ** (len(reverse_list) - 1 - i))

        if checkRange(result):
            if x < 0:
                return -1 * result
            else:
                return result
        else:
            return 0
    else:
        return 0


def checkRange(x):
    if 2147483647 > x > - 2147483648 and x != 0:
        return True
    else:
        return False


def online_solution(x):
    sign = [1, -1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0


def main():
    result = reverse(123)
    print(result)


main()


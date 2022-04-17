# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def binary_to_dec(binary):
    ret = 0
    binary = str(binary)[::-1]

    for n in range(0, len(binary)):

        if binary[n] != "0":
            ret += 2 ** n

    return ret


def dec_to_binary(some_integer):
    some_integer = int(some_integer)
    ret = ""
    h = 0

    while some_integer > 2 ** h:
        h += 1

    for n in range(h - 1, -1, -1):
        if some_integer >= 2 ** n:
            ret += "1"
            some_integer -= 2 ** n
        else:
            ret += "0"

    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        binary_to_dec(
            input("Input a binary number (note: all non zero characters are read as 1's)\n")))

    print(
        dec_to_binary(
            input("Input dec number\n")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

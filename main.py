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

    # Edgecase 1 or 0.
    if some_integer == 1:
        ret += "1"
    elif some_integer == 0:
        ret += "0"

    while some_integer > 2 ** h:
        h += 1

    for n in range(h - 1, -1, -1):
        if some_integer >= 2 ** n:
            ret += "1"
            some_integer -= 2 ** n
        else:
            ret += "0"
    return ret


def ip_address_dec_to_binary(ip_addresss_dec):
    ret = ""
    octet = ""

    for c in ip_addresss_dec:
        if c != ".":
            octet += c
        else:
            octet = dec_to_binary(octet)
            oct_len = len(octet)
            for n in range(0, 8 - oct_len):
                octet = "0" + octet
            ret += octet + c
            octet = ""
    octet = dec_to_binary(octet)
    oct_len = len(octet)
    for n in range(0, 8 - oct_len):
        octet = "0" + octet

    ret += octet
    return ret


def ip_address_binary_to_dec(ip_address_binary):
    dot = "."
    return str(binary_to_dec(ip_address_binary[0:8])) + dot + \
        str(binary_to_dec(ip_address_binary[9:17])) + dot + \
        str(binary_to_dec(ip_address_binary[18:26])) + dot + \
        str(binary_to_dec(ip_address_binary[27:35]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        binary_to_dec("1"))

    print(
        dec_to_binary("1"))

    print(ip_address_dec_to_binary("192.168.1.34"))
    print(ip_address_binary_to_dec("11000000.10101000.00000001.00100010"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

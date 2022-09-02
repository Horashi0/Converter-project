import builtins
import decimal

input = int(input("What would you like to convert? \n 1) Decimal to Binary \n 2) Decimal to Hexadecimal \n 3) Decimal to Octal \n 4) Hexadecimal to Decimal \n 5) Hexadecimal to Binary \n 6) Hexadecimal to Octal \n 7) Binary to Decimal \n 8) Binary to Hexadecimal \n 9) Binary to Octal \n 10) Octal to Decimal \n 11) Octal to Hexadecimal \n 12) Octal to Binary \n Please enter number: "))

# Decimal to Binary


def decimal_binary():
    a = int(builtins.input("What is your decimal number? "))
    bin_b = bin(a)
    print(int(bin_b.replace("0b", "")))
# Decimal to Hexadecimal


def decimal_hexadecimal():
    b = int(builtins.input("What is your Decimal number? "))
    hex_a = hex(b)
    print(hex_a)
    print(int(hex_a, 16))
# Decimal to Octal


def decimal_octal():
    c = int(builtins.input("What is your Decimal number? "))
    oct_c = oct(c)
    print(oct_c)
# Hexadecimal to Decimal


def hexadecimal_decimal():
    d = builtins.input("What is your Hexadecimal number? ")
    print(int(d, 16))
# Hexadecimal to Binary


def hexadecimal_binary():
    e = builtins.input("What is your Hexadecimal number? ")
    bin_e = int(e, 16)
    print((bin(bin_e)))
# Hexadecimal to Octal


def hexadecimal_octal():
    f = builtins.input("What is your Hexadecimal number? ")
    oct_f = int(f, 16)
    print((oct(oct_f)))
# Binary to Decimal


def binary_decimal():
    g = builtins.input("What is your Binary number? ")
    dec_g = int(g, 2)
    print(dec_g)
# Binary to Hexadecimal


def binary_hexadecimal():
    h = builtins.input("What is your Binary number? ")
    dec_h = int(h, 2)
    hex_h = hex(dec_h)
    print(hex_h)
# Binary to Octal


def binary_octal():
    i = builtins.input("What is your Binary number? ")
    dec_i = int(i, 2)
    oct_i = oct(dec_i)
    print(oct_i)
# Octal to Decimal


def octal_decimal():
    j = builtins.input("What is your Octal number? ")
    dec_j = int(str(j), 8)
    print(dec_j)
# Octal to Hexadecimal


def octal_hexadecimal():
    k = builtins.input("What is your Octal number? ")
    hex_k = int((k), 8)
    print(hex(hex_k))
# Octal to Binary


def octal_binary():
    l = builtins.input("What is your Octal number? ")
    bin_l = int(l, 8)
    print((bin(bin_l)))


# Decimal to Binary
if input == int("1"):
    decimal_binary()
# Decimal to Hexadecimal
if input == int("2"):
    decimal_hexadecimal()
# Decimal to Octal
if input == int("3"):
    decimal_octal()
# Hexadecimal to Decimal
if input == int("4"):
    hexadecimal_decimal()
# Hexadecimal to Binary
if input == int("5"):
    hexadecimal_binary()
# Hexadecimal to Octal
if input == int("6"):
    hexadecimal_octal()
# Binary to Decimal
if input == int("7"):
    binary_decimal()
# Binary to Hexadecimal
if input == int("8"):
    binary_hexadecimal()
# Binary to Octal
if input == int("9"):
    binary_octal()
# Octal to Decimal
if input == int("10"):
    octal_decimal()
# Octal to Hexadecimal
if input == int("11"):
    octal_hexadecimal()
# Octal to Binary
if input == int("12"):
    octal_binary()

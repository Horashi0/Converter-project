import builtins
import decimal

input = int(input("What would you like to convert? \n 1) Decimal to Binary \n 2) Decimal to Hexadecimal \n 3) Decimal to Octol \n 4) Hexadecimal to Decimal \n 5) Hexadecimal to Binary \n 6) Hexadecimal to Octol \n 7) Binary to Decimal \n 8) Binary to Hexadecimal \n 9) Binary to Octol \n 10) Octol to Decimal \n 11) Octol to Hexadecimal \n 12) Octol to Hexadecimal \n Please enter number: "))

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
# Decimal to Octol


def decimal_octol():
    c = int(builtins.input("What is your Decimal number? "))
    oct_c = oct(c)
    print(oct_c)
# Hexadecimal to Decimal


def hexadecimal_decimal():
    d = int(builtins.input("What is your Hexadecimal number? "))
    hex_d = int(d)
    print(hex_d, 16)


# Decimal to Binary
if input == int("1"):
    decimal_binary()
# Decimal to Hexadecimal
if input == int("2"):
    decimal_hexadecimal()
# Decimal to Octol
if input == int("3"):
    decimal_octol()
# Hexadecimal to Decimal
if input == int("4"):
    hexadecimal_decimal()

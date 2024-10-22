# x = int(input("Whats x? ").strip())
# y = int(input("whats y? ").strip())

x = float(input("Whats x? ").strip())
y = float(input("whats y? ").strip())
# without the int at the begining it thinks they are strings and it concatenate which means it just chains together.
# z = x + y
# z = int(x) + int(y) works the same
# z = round(x + y)
# round function rounds up to the nearest whole number
# print(f"{z:,}")
# :, adds the comma for the larger 1000 numbers

z = x / y
print(f"{z:.2f}")
# the :.2f makes it go to the second decimal point



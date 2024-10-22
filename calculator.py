x = int(input("Whats x? ").strip())
y = int(input("whats y? ").strip())
# without the int at the begining it thinks they are strings and it concatenate which means it just chains together.
# z = x + y
# z = int(x) + int(y) works the same
print(x + y)
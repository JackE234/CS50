#def = define
# inside the brackets (parameter)
# def hello(to="world"):
#     print("hello,", to)


# hello()
# name = input("What's your name? ").capitalize()
# hello(name)

def main():
    name = input("What's your name? ").capitalize()
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()
name = input("What's your name? ")
#The match statement in Python lets you check a value against multiple patterns to see which one fits.
#It’s like a more organized way of using multiple if statements.
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        # the _ is the equivelent of a else: statement
        print("Who?")
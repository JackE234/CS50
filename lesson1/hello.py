# going over methods and f string

# string(str) is a sequnce of text
# Ask user for their name
name = input("Whats your name? ").strip().title()
# task of code is to say hello to user input of their name

# Ways to solve this problem

#  print("Hello,", name)

# print('Hello, ', end="") 
## end removes the new line that is added to individual print functions.
# print(name)

first, last = name.split(" ")

# name  = name.capitalize() #used to capitalize the very first letter of input

# name = name.strip() #removes whitespace of the left and right of input
# name = name.title() #capitalizes the start of every word

# name = name.strip().title() #more cleaned up version compressing into one line of code
# whats this doing get
# get the value of the string name then strip off the white space from the left to the right
# the python is going through and title casing it going word to word capitalizing it

print(f"hello, {first}")#most commonly way users solve this problem
# F-string is a way to format strings(data types)

# sep="" part of the python docs for print file its used to
# change the space inbetween inputs


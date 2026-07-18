'''
# Ask the user for their name and print a greeting
name = input("What is your name? ")

# Remove whitespace from the start and end of the name and capitalize the first letter of the name
name = name.strip().title()

# Say hello to the user
print (f"Hello, {name}")
'''
def ask_name():
    name = input("What is your name? ")
    name = name.strip().title()
    greet(name) 
    return name

def greet(name):
    print(f"Hello, {name}")

name = ask_name()

def ask_age(name):
    age = int(input("What is your age? "))
    greet_age(age)
    return age

def greet_age(age):
    print(f"You are {age} years old")
    
age = ask_age(name)

def end_greet(name, age):
    print(f"Your name is {name} and you are {age} years old")

end_greet(name, age)
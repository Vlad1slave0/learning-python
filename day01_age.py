import time

def ask_name():
    name = input("Как тебя зовут? ")
    return name

name = ask_name()

def ask_age(name):
    age = int(input("Сколько тебе лет? "))
    return age
age = ask_age(name)

def calc(age):
    if age < 18:
        return 18 - age
    else:
        return 0
age_result = calc(age)

def calc2030(age):
    age2030_result = age + 4
    return age2030_result
age2030_result = calc2030(age)

def main_function(name, age, age_result, age2023_result):
    time.sleep(1.5)
    if age_result == 1:
        print(f"Привет, {name}! Тебе {age}, до совершеннолетия остался {age_result} год! А в 2030 году тебе будет {age2030_result}!")
    elif age_result in (2, 3, 4): 
        print(f"Привет, {name}! Тебе {age}, до совершеннолетия осталось {age_result} года! А в 2030 году тебе будет {age2030_result}!")
    elif age_result > 4:
        print(f"Привет, {name}! Тебе {age}, до совершеннолетия осталось {age_result} лет! А в 2030 году тебе будет {age2030_result}!")
    else:
        print(f"Привет, {name}! Тебе {age}. А в 2030 году тебе будет {age2030_result}!")

main_function(name, age, age_result, age2030_result)
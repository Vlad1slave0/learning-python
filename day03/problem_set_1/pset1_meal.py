import time

def converter(calc_input):
    hours, minutes  = calc_input.split(":")
    return float(hours) + float(minutes) / 60

def main():
    user_input = input("What time is it? ")
    result_of_math = converter(user_input)
    time.sleep(0.5)

    if 7 <= result_of_math <=8:
        print("Breakfast time")
    elif 19 < result_of_math <= 24:
        print("Wait your breakfast time")
    elif 0 <= result_of_math < 8:
        print("Wait your breakfast time")
    elif 8 < result_of_math < 12:
        print("Wait your lunch time")
    elif 12 <= result_of_math <= 13:
        print("Lunch time")
    elif 13 < result_of_math < 18:
        print("Wait your breakfast time")
    elif 18 <= result_of_math <= 19:
        print("Dinner time")
    else:
        print("Your time is in incorrect form")

main()
        

    


    




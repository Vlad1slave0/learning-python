import time

GREEN = "\033[32m"
RESET = "\033[0m"

inputPerson = input(f"Напишите что-то: ")
LowLetters = inputPerson.lower()
time.sleep(1)
print(GREEN + LowLetters + RESET)

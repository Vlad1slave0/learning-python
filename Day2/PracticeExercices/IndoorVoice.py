import time

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

for letter in inputPerson:
    if letter.isupper():
       RED + letter + RESET
    else:
        GREEN + letter + RESET

inputPerson = input(f"Напишите что-то: ")
LowLetters = inputPerson.lower()
time.sleep(1)
print(GREEN + LowLetters + RESET)

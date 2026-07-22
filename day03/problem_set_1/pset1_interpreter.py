
math_input = input("Напишите свою задачу: ").strip()
x, y, z, = math_input.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")
else:
    print("Исправьте предложение!")

    

def einstein_calculator(mass):
    final_mass = mass * 300000000 ** 2
    return final_mass 
    
def main():
    user_input = int(input("Пожалуйста введите целое число, чтобы узнать сколько энергии в джоулях в ней заключено: "))
    final_input = einstein_calculator(user_input)
    print(final_input)

main()

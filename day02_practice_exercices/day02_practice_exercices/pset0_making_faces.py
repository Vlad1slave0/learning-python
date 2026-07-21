def convert(text):
    result = text.replace(":)", "🙂")
    result = result.replace(":(", "🙁")
    return result


def main():
    user_text = input("Напиши что-то: ")
    final_text = convert(user_text)
    print(final_text)


main()
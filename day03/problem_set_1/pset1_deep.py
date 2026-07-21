
def main():
    answer_person = input("What is the Answer to the Great Question of Life, the Universe, and Everything ").strip().lower()
    match answer_person:
        case "42":
            print("Yes")
        case "forty-two" | "forty two":
            print("Yes")
        case _:
            print("Nahh mate")



main()

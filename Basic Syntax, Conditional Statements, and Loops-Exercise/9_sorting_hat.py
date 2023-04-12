while True:
    lines = input()

    if lines == 'Welcome!':
        print("Welcome to Hogwarts.")
        break
    elif lines == 'Voldemort':
        print("You must not speak of that name!")
        break

    word_lent = len(lines)

    if word_lent < 5:
        print(f"{lines} goes to Gryffindor.")

    elif word_lent == 5:
        print(f"{lines} goes to Slytherin.")

    elif word_lent == 6:
        print(f"{lines} goes to Ravenclaw.")

    elif word_lent > 6:
        print(f"{lines} goes to Hufflepuff.")


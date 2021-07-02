with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
with open("./Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.readlines()
    for name in name_list:
        name = name.strip('\n')
        new_letter = letter.replace('[name]', name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as output_letter:
            output_letter.write(new_letter)
    print("Task done!")

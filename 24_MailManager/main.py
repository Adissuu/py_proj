PLACEHOLDER = "[Name]"

with open("invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("blank_letter.txt") as text_file:
    content = text_file.read()
    for name in names:
        stripped_name = name.strip()
        new_content = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_content)

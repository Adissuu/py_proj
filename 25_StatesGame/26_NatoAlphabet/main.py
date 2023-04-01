import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet ={row.letter:row.code for (index, row) in data.iterrows()}

word = input("Please input a word: ").upper()
nato_word = []
nato_word = [nato_alphabet[letter] for letter in word]
print(nato_word)


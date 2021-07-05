import pandas

user_word = input("Type a word: ").upper()
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
word_dict = {row.letter: row.code for (index, row) in data.iterrows() if row.letter in user_word}
print(word_dict)

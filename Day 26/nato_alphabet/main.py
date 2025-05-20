import pandas

nato_alphabet_data_frame = pandas.read_csv("nato_alphabet\\nato_phonetic_alphabet.csv")
# print(nato_alphabet_data_frame)

nato_alphabet_dict = {
    row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()
}
print(nato_alphabet_dict)

word = input("Enter a word: ").upper()
try:
    phonetic_list = [nato_alphabet_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(phonetic_list)

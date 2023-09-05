

import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter :row.code for (index,row) in nato_alphabet.iterrows()}


user_input = input("Enter your name: ").upper()

name_spelled = [code for (letter,code) in nato_dict.items() if letter in user_input]

print(name_spelled)

import pandas


# TODO 1. create a dict from the CSV
df = pandas.read_csv('nato_phonetic_alphabet.csv')
index_phonetic_alphabet = df.set_index('letter')['code'].to_dict()
# name = input("Enter the name you need in your alphabet: ")
#name ='didiy'

def word():
    name = input("Enter the name you need in your alphabet: ")

# TODO 2. The user writes text and each letter is translated into a phonetic alphabet:
new_phonetic_name = []
for letter in name.upper():
    for code_letter, code_names in index_phonetic_alphabet.items():
        if letter == code_letter:
            new_phonetic_name.append(code_names)
        else:
            "Use only letters, Try again"

print(new_phonetic_name)



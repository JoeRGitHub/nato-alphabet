import pandas


# TODO 1. create a dict from the CSV
df = pandas.read_csv('nato_phonetic_alphabet.csv')
index_phonetic_alphabet = df.set_index('letter')['code'].to_dict()


# TODO 2. check user types only alphabet
def word():
    name = input("Enter the name you need in your alphabet: ")
    if name.isalpha():
        return name
    else:
        print("Use only alphabet and not space. Try again")
        return word()


# TODO 3. The user writes text and each letter is translated into a phonetic alphabet:
new_phonetic_name = []
x = word()
for letter in x.upper():
    for code_letter, code_names in index_phonetic_alphabet.items():
        if letter == code_letter:
            new_phonetic_name.append(code_names)


print(new_phonetic_name)



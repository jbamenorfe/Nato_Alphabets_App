"""This program takes an input from the user and displays its NATO phonetic codes. By JBAmenorfe on 24/01/2025"""
import pandas

#TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}
####    (a) Read csv file and assign it to alphabets_df (alphabets dataframe)
alphabets_df = pandas.read_csv("nato_phonetic_alphabet.csv")

####    (b) Create the dictionary called alphabets_dict
alphabets_dict = {row.letter:row.code for (index, row) in alphabets_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
####    (a) Receive an input from the user and assign it to a variable called word_to_spell
####    ##### Use exception handling to check the entry made by the user

def generate_phonetic():
    word_to_spell = input("Enter a word to spell: ").upper()
    ####    (b) Create a list of the phonetic code words from the variable word_to_spell
    try:
        phonetic_word_list = [alphabets_dict[letter] for letter in word_to_spell]
    except KeyError:
        print("Sorry, numbers are not valid entries. Enter only letters!")
        generate_phonetic()
    else:
        print(phonetic_word_list)

# Call the function generate_phonetic()
generate_phonetic()





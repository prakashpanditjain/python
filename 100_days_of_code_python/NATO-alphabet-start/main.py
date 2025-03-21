student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key,value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(row.score)
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
alpha_dict = {row.letter:row.code for index,row in df.iterrows()}
print(alpha_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("what is your word?\n").upper()
    try:
        phonetic_word_list = [alpha_dict[letter] for letter in user_input]
    except Exception as e:
        print(f"An error occurred: {e}")
        generate_phonetic()
    else:
        print(phonetic_word_list)

generate_phonetic()
import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word:").upper()
#user_nato = [code for (letter, code) in nato_dict.items() if letter in user_input]
#or 
user_nato = [nato_dict[letter] for letter in user_input]
print(user_nato)



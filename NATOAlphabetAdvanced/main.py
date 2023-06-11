import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
is_string = False

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while not is_string:
	word = input("Enter a word: ").upper()
	try:
		output_list = [phonetic_dict[letter] for letter in word]		
	except KeyError:
		print("Please enter only alphabet charcter")
	else:
		print(output_list)
		is_string = True


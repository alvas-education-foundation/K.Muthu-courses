# Program for  Dictionary which prints the meaning of the user input
#Program runs untill user press enter

import json
from difflib import get_close_matches
data=json.load(open("original.json"))

def meaning(word):
	word=word.lower()
	match=get_close_matches(word,data.keys())
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(match)>0:
		print("Did you mean", match[0])
		choice=input("Press 'y' for yes and 'n' for no : ")
		if choice == 'y':
			return data[match[0]]
		elif choice =='n':
			return "Sorry, Try other words"
		else:
			return "Press either 'y' or 'n' "
	else:
		return "Sorry, Try other words "

while True:
	word=input("Enter the search word : ")
	if word:
		output=meaning(word)
		if type(output) is list:
			for item in output:
				print("* ",item)
			print("     -----***-----        ")
		else:
			print(output)
			print("     -----***-----        ")
	else:
		break
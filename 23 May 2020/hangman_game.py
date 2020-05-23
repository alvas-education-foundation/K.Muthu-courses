#Python program to play Hangman game...

import random

def hangman():
	#Random word is choosen from the list
	word=random.choice(['doctor','home','avenger','fool','school','thor','ball','wild','lion','tiger','apple'])
	guessmade=''
	attempt=10
	while True:
		main=''
		for letter in word:
			if letter in guessmade:
				main=main+letter
			else:
				main=main+'_'+' '
		if main == word:
			print("The word is ",main)
			print("You won !!!")
			break
		print("Guess the word : ",main)
		guess=input()
		if guess.isalpha():
			guessmade=guessmade+guess
		else:
			print("Enter a valid character")
			guess=input()
		if guess not in word:
			attempt-=1
			if attempt == 9:
				print("9 attempts are left ")
				print(" --------  ")
			if attempt == 8:
				print("8 attempts are left ")
				print(" --------  ")
				print("    O    ")
			if attempt == 7:
				print("7 attempts are left ")
				print(" --------  ")
				print("    O    ")
				print("    |      ")
			if attempt == 6:
				print("6 attempts are left ")
				print(" --------  ")
				print("    O    ")
				print("    |      ")
				print("   /       ")
			if attempt == 5:
				print("5 attempts are left ")
				print(" --------  ")
				print("    O    ")
				print("    |      ")
				print("   / \    ")
			if attempt == 4:
				print("4 attempts are left ")
				print(" --------  ")
				print("  \ O    ")
				print("    |      ")
				print("   / \    ")
			if attempt == 3:
				print("3 attempts are left ")
				print(" --------  ")
				print("  \ O /   ")
				print("    |     ")
				print("   / \    ")
			if attempt == 2:
				print("2 attempts are left ")
				print(" --------  ")
				print("  \ O /|  ")
				print("    |     ")
				print("   / \    ")
			if attempt == 1:
				print("1 attempt is left ")
				print(" --------  ")
				print("  \ O_/|  ")
				print("    |     ")
				print("   / \    ")
			if attempt == 0:
				print("You lost ")
				print("You let a kind man die ")
				print(" --------  ")
				print("    O_| ")
				print("   /|\    ")
				print("   / \    ")
				break
		
#Greeting the user
name=input("Enter your name : ")
print("Welcome",name)
print("-----------------------")
print("Find the word in less than 10 attempts ")
hangman()
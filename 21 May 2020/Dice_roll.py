#Python program for virtual Dice rolling simulator

import random
print("Dice rolling simulator ")
while True:
	roll=input("Press 'y' to roll the dice : ")
	if roll =='y':
		number=random.randint(1,6)
		if number == 1:
			print("----------")
			print("|        |")
			print("|    O   |")
			print("|        |")
			print("----------")
		if number == 2:
			print("----------")
			print("|        |")
			print("|  O  0  |")
			print("|        |")
			print("----------")
		if number == 3:
			print("----------")
			print("|        |")
			print("|  O O O |")
			print("|        |")
			print("----------")
		if number == 4:
			print(" ----------")
			print("|  O    O  |")
			print("|          |")
			print("|  O    O  |")
			print(" ----------")
		if number == 5:
			print(" ----------")
			print("|  O     O |")
			print("|     O    |")
			print("|  O     O |")
			print(" ----------")
		if number == 6:
			print(" ----------")
			print("|  O O O  |")
			print("|         |")
			print("|  O O O  |")
			print(" ----------")
			
	else:
		break
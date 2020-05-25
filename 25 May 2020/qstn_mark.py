"""Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. If so, return true, otherwise return false """

import pandas as pd

#This function checks the two condition 
def count(a,dig):
	# value_counts provides the frequency of each characters
	# Also the result is stored in dictionary for ease access
	a=dict(pd.Series(a).value_counts())
	if '?' in a.keys():
		# Checking both condition
		if a['?'] == 3 and dig == 10:
			print("True")
			return 1
		else:
			return 0


# This function adds the two pair digits and stores the character between them
def check(n,dig):
	a=[]
	for x in s[n:]:
		if x.isdigit() is False:
			a.append(x)
			# a contains all the character between a pair of digits
		else:
			dig+=int(x)
			return count(a,dig)

#This is the first function called
#This function check the presence of digit in the string
def find(s):
	flag=0
	# n variable points the index of element in string 
	n=0
	for i in s:
		n+=1
		dig=0
		# Checks for digit in the string
		if i.isdigit():
			dig=dig+int(i)
			flag=check(n,dig)
			if flag == 1:
				break
			else:
				continue
	if flag != 1:
		print("False")


s=input("Enter the string : ")
find(s)
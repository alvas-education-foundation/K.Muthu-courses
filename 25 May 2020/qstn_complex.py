"""
Problem Statement:
    Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. 
    If so, return true, otherwise return false. Some examples test cases are below:

    "arrb6???4xxbl5???eee5" => true
    "acc?7??sss?3rr1??????5" => true
    "5??aaaaaaaaaaaaaaaaaaa?5?5" => false
    "9???1???9???1???9" => true
    "aa6?9" => false
"""

#importing numpy module
import numpy as np

#Function checks the sum of pair numbers
#Also finds the frequency of element '?' in the list
def check(n1 , n2 , li):
    n = 0
    for l in li:
        if l == '?':
            n += 1
    num = n1 + n2
    if num == 10:
        buf.append(n)

#This function finds the pair numbers (num1 , num2)
#Also groups the elements between the pair of numbers
def group(input_string , x):
    list = []
    num1 = int(input_string[x])
    num2 = 0
    x += 1
    while x < len(input_string):
        if input_string[x].isdigit():
            num2 = int(input_string[x])
            break
        else:
            list.append(input_string[x])
        x += 1
    check(num1 , num2 , list)

if __name__ == '__main__':
    input_string = input("Enter the string : ")
    global buf
    buf = []
    #Finding digits in the input string
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            group(input_string , i)  

    #Comparing the conditions and printing final result
    val = np.unique(buf)
    if len(val) == 1 and val[0] == 3:
        print('True')
    else:
        print('False') 
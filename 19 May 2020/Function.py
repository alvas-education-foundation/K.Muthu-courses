# Convert the temperature into Fahrenheit, given celsuis as inpit using function.

#Function definition
def temp(c):
	f=(c*9/5)+32
	return f

c=int(input("Enter the temperature in celsius : "))
#Function call
f=temp(c)
#Output
print("Temperature in Fahrenheit : ",f)
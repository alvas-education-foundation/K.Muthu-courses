# Read a file and then print the data in it

#Open the file in read mode
file=open('colour.txt','r')
#Storing the contents from the file
data=file.read()
#Output
print(data)
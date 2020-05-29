#Creating database using sqlite3 library

#importing sqlite3 module
import sqlite3

#Creating table in the database
def create_table():
	conn = sqlite3.connect("work.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE data(rollno 		INTEGER , name TEXT , marks REAL )")
	conn.commit()
	conn.close()
	
#Creating table 
create_table()

#Inserting values into the table
def insert(rollno,name,marks):
	conn = sqlite3.connect("work.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO data VALUES(?,?,?)",(rollno,name,marks))
	conn.commit()
	conn.close()

#Inserting values
insert(1,'Ashwin',80)
insert(2,'Dhoni',90)
insert(3,'Kohli',99)

#Function to view the data in the database table
def view():
	conn = sqlite3.connect("work.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM data")
	row=cur.fetchall()
	conn.commit()
	conn.close()
	return row
	
#Viewing the data in table
print("The data inserted into the table are : ")
print(view())
print()
	
#Deleting records in the table with rollno as base value
def delete(rollno):
	conn = sqlite3.connect("work.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM data WHERE rollno=?",(rollno,))
	conn.commit()
	conn.close()
	
#Deleting the records of rollno = 3
delete(3)
print("viewing the data after deleting records of rollno = 3 ")
print(view())
print()
	
#Update the records of data in table with rollno as base value
#Provide updated name or marks value as a parameter
def update(rollno,name,marks):
	conn = sqlite3.connect("work.db")
	cur = conn.cursor()
	cur.execute("UPDATE data SET name=? , marks = ? WHERE rollno=?",(name,marks,rollno))
	conn.commit()
	conn.close()
	
#update the name & marks of rollno = 2 as 'M S Dhoni' & 100
update(2,"M S Dhoni",100)

#Viewing the data after updating the records of rollno = 2
print("Viewing the data after updating records of rollno = 3 ")
print(view())
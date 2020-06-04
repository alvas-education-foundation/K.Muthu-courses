import sqlite3

def connect():
	conn=sqlite3.connect('routine.db')
	cur=conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS routine(Id INTEGER PRIMARY KEY , date text,savings integer ,exercise text,study text,diet text,python text)')
	conn.commit()
	conn.close()
	
def insert(date,savings,exercise,study,diet,python):
	conn=sqlite3.connect('routine.db')
	cur=conn.cursor()
	cur.execute('INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)',(date,savings,exercise,study,diet,python))
	conn.commit()
	conn.close()
	
	
def view():
	conn=sqlite3.connect('routine.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM routine')
	rows=cur.fetchall()
	conn.commit()
	conn.close()
	return rows
	
def delete(id):
	conn=sqlite3.connect('routine.db')
	cur=conn.cursor()
	cur.execute('DELETE FROM routine WHERE id=? ',(id,))
	conn.commit()
	conn.close()

def search(date=' ',savings=' ',exercise=' ',study=' ',diet=' ',python=' '):
	conn=sqlite3.connect('routine.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM routine where date=? or savings=? or exercise=? or study=? or diet=? or python =? ',(date,savings,exercise,study,diet,python))
	rows=cur.fetchall()
	conn.commit()
	conn.close()
	return rows
	
	
connect()
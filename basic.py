import sqlite3

def connection_demo():
	''' Creat a db connection
	'''
	# conn = sqlite3.connect(':memory:') # Creat in memory
	conn = sqlite3.connect('customer.db') # Creat a .db file


def table_demo():
	''' Crear a DataBase Table
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute(
		"""CREATE TABLE customers(
			first_name TEXT,
			last_name TEXT,
			age INTEGER,
			email TEXT
		)""")
	conn.commit()
	conn.close()


def insert_demo():
	''' Insert Records into Table
	'''
	# Insert one Record into Table
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute(
		"""INSERT INTO customers VALUES(
			'Jone',
			'Elder',
			20,
			'jone@example.com')
		""")
	conn.commit()
	conn.close()

	# Insert Many Records  into Table at a time
	many_customers = [
					('Wes', 'Brown', 18,'wes@brown.com'),
					('Steph', 'Kuewa', 19,'steph@codemy.com'),
					('Dan', 'Pas', 22,'dan@codemy.com')
				]
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.executemany("""INSERT INTO customers VALUES (?,?,?,?)""",many_customers)
	conn.commit()
	conn.close()


def query_demo():
	''' Quert and fetchall
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute("SELECT * FROM customers")
	#c.fetchone()
	#c.fetchmany(3)
	print("""c.execute("SELECT * FROM customers")""")
	for item in c.fetchall():
		print(item)

	c.execute("SELECT rowid,* FROM customers")
	print("""\nSELECT rowid,* FROM customers""")
	for item in c.fetchall():
		print(item)

	c.execute("SELECT * FROM customers WHERE age >= 19")
	print("""\nc.execute("SELECT * FROM customers WHERE age >= 19")""")
	for item in c.fetchall():
		print(item)
	c.execute("SELECT * FROM customers WHERE age >= 19 LIMIT 2")
	print("""\nc.execute("SELECT * FROM customers WHERE age >= 19 LIMIT 2")""")
	for item in c.fetchall():
		print(item)
	c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
	print("""\nc.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")""")
	for item in c.fetchall():
		print(item)
	c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
	print("""\nc.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")""")
	for item in c.fetchall():
		print(item)

	conn.commit()
	conn.close()


def udpate_demo():
	''' update record ID 
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute ("""UPDATE customers SET first_name = 'Bob'
					WHERE rowid = 1
				""")
	c.execute("SELECT rowid,* FROM customers")
	print('\nAfter change rowid=1 -> first_name = Bob:\n',c.fetchone())

	conn.commit()
	conn.close()


def delete_demo():
	''' delete record
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute(
		"""INSERT INTO customers VALUES(
			'Good',
			'Bye',
			30,
			'BoodBye@example.com')
		""")
	c.execute("DELETE from customers WHERE first_name='Good' AND last_name='Bye'")
	c.execute("SELECT rowid,* FROM customers")
	print('\nAfter inser and delete \'Good Bye\':')
	for item in c.fetchall():
		print(item)

	conn.commit()
	conn.close()


def order_result_demo():
	''' order result by ...
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute("SELECT rowid,* FROM customers ORDER BY age")
	print('\nSELECT rowid,* FROM customers ORDER BY age')
	for item in c.fetchall():
		print(item)
	c.execute("SELECT rowid,* FROM customers ORDER BY age DESC")
	print('\nSELECT rowid,* FROM customers ORDER BY age DESC')
	for item in c.fetchall():
		print(item)

	conn.commit()
	conn.close()


def drop_table_demo():
	''' drop table
	'''
	conn = sqlite3.connect('customer.db') # Creat a .db file
	c = conn.cursor()
	c.execute(
		"""CREATE TABLE to_be_drop(
			first_name TEXT,
			last_name TEXT,
			age INTEGER,
			email TEXT
		)""")
	c.execute("SELECT rowid,* FROM sqlite_master")
	print("""\nCreat a new table""")
	for item in c.fetchall():
		print(item)
	c.execute("DROP TABLE to_be_drop")
	c.execute("SELECT rowid,* FROM sqlite_master")
	print("""\nAfter drop a table""")
	for item in c.fetchall():
		print(item)
	conn.commit()
	conn.close()



if __name__ == '__main__':
	#connection_demo()
	#table_demo()
	#insert_demo()
	#query_demo()
	#udpate_demo()
	#delete_demo()
	#order_result_demo()
	drop_table_demo()


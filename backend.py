import sqlite3

class Database:

	# constructor
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
		self.conn.commit()

	def insert(self, title, author, year, isbn):
		# The id is an autoincrement value so we will pass in null
		self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
		self.conn.commit()

	def view(self):
		# The id is an autoincrement value so we will pass in null
		self.cur.execute("SELECT * FROM book")
		rows = self.cur.fetchall()
		return rows

	# All search. The user will enter in a title or auther or isbn or year
	def search(self, title = "", author = "", year = "", isbn = ""):
		self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
		rows = self.cur.fetchall()
		return rows

	# Delete a record by selecting a record from the listbox
	def delete(self, id):
		self.cur.execute("DELETE FROM book WHERE id = ?", (id,)) # Note enter comma after id
		self.conn.commit()

	# Update a record by selecting a record from the listbox and display the record in the widget
	def update(self, id, title, author, year, isbn):
		self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
		self.conn.commit()

	# destructor
	def __del__(self):
		self.conn.close()


	#insert("The Earth", "John Doe", 1997, 225555852)
	#delete(3)
	# update(4, "The moon", "John Smith", 1917, 985557)
	# print(view())
	# print(search(author="Aron Payle"))
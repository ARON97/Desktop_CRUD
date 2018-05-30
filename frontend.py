from tkinter import *
from backend import Database # import database

# create an object out of the blue print(Database class from database)
database = Database("books.db")

# getting the selected record for deletion
def get_selected_row(event):
	try:
		# global variable
		global selected_tuple
		# getting the index from the list
		index = list1.curselection()[0]
		# get the tuple(All the values of the row)
		selected_tuple = list1.get(index)
		# fill the entries with a selected record
		# delete if there is something in the entries
		e1.delete(0, END)
		e1.insert(END, selected_tuple[1])
		e2.delete(0, END)
		e2.insert(END, selected_tuple[2])
		e3.delete(0, END)
		e3.insert(END, selected_tuple[3])
		e4.delete(0, END)
		e4.insert(END, selected_tuple[4])
	except IndexError:
		pass

def view_command():
	# ensure that when the for loop is executed the listbox is already empty
	list1.delete(0, END)
	# iterate through records
	for row in database.view():
		list1.insert(END, row) # END ensures that every new row is inserted at the end of the listbox


# Search Entry button
def search_command():
	# ensure that when the for loop is executed the listbox is already empty
	list1.delete(0, END)
	for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
		list1.insert(END, row)
		
# Add Entry button
def add_command():
	database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	# ensure the list is empty
	list1.delete(0, END)
	# insert new values at the end of the list
	list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# Update button
def update_command():
	database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

# Delete button
def delete_command():
	database.delete(selected_tuple[0])


# from window = Tk() to window.mainloop() all the widgets are entered here
window = Tk()

# Window title
window.wm_title("BookStore")

# Title label
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

# Author label
l1 = Label(window, text = "Author")
l1.grid(row = 0, column = 2)

# Year label
l1 = Label(window, text = "Year")
l1.grid(row = 1, column = 0)

# ISBN label
l1 = Label(window, text = "ISBN")
l1.grid(row = 1, column = 2)

# Title entry
# Datatype
title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

# Author entry
author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

# Year entry
year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

# ISBN entry
isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

# listbox
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

# attach scrollbar to list
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

# Bind is used to bind a function to a widget
# Bind a method to the listbox. This is for the deletion method in the database
list1.bind('<<ListboxSelect>>', get_selected_row)

# BUTTONS
# View allbutton
b1 = Button(window, text = "View all", width = 12, command = view_command)
# Command is called a wrapper function
b1.grid(row = 2, column = 3)

# Search Entry button
b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
# Command is called a wrapper function
b2.grid(row = 3, column = 3)

# Add Entry button
b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
# Command is called a wrapper function
b3.grid(row = 4, column = 3)

# Update button
b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

# Delete button
b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

# Close button
b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
"""
GUI program that stores book info

Title, Author
Year, ISBN

User can: Create, Read, Update, Delete entries
"""

from tkinter import *

#create window object
window = Tk()

#FUNCTION TO  GET TEXT FROM ENTRY WIDGETS
def return_entry(en):
    """Gets and prints the content of the entry"""
    content = en.get()
    print(content) 

#label widgets
l1=Label(window,text="Title")
l1.grid(row=0,column=0)


l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)


#entry widgets
e1=Entry(window)
e1.grid(row=0,column=1)


#wrap up all widgets
window.mainloop()

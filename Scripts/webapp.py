from tkinter import *
import tkinter as tk
# Create object
root = Tk()
  
# Adjust size
root.geometry( "600x200" )
  
# Change the label text
def show():
    Label.config( text = clicked.get() )
    
def save_text():
   text_file = open("test.txt", "w")
   text_file.write(inputtxt.get(1.0, END))
   text_file.close()
def open_text():
   text_file = open("test.txt", "r")
   content = text_file.read()
   inputtxt.insert(END, content)
   text_file.close()
      
# Dropdown menu options
options = ["Option 1", "Option 2", "Option 3",]  
# datatype of menu text
clicked = StringVar() 
# initial menu text
clicked.set( "Select an Option" )

# Create Dropdown menu
labelDropMenu = Label(root,text = "Select Option: ").place(x = 40, y = 20)
dropMenu = OptionMenu( root , clicked , *options ).place(x = 240, y= 20)
buttonDrop = Button( root , text = "confirm selection" , command = show ).place(x=440, y = 20)

#Create textbox
labelText = Label(root, text = "Enter text: ").place(x=40, y = 120)
inputtxt = tk.Text(root, height = 5, width = 20,padx = 10, pady = 10).place(x=240,y=120)
buttonText = Button(root, text =  "confirm input" , command = save_text).place(x=440, y=120)

  
# Execute tkinter
root.mainloop()

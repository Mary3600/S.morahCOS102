import tkinter as tk
from tkinter import messagebox as msgbox

#handling button click event
def button_click():
    #show information message box
    msgbox.showinfo("Info", "Welcome to COS102 GUI app!\n")

    #ask for user confirmation
    result = msgbox.askyesno("Confirmation","Do you want to continue?")

#create main wondow
root = tk.Tk()
root.title("Home Page")
root.geometry = ("300x100")

#add a label widget
label = tk.Label(root, text="Hello Friend\n")
label.pack()

#Add a button widget 
button = tk.Button(root, text="click me!", command=button_click)
button.pack()

#styling the button widget
button.config(fg="red", bg="yellow")

#start event loop
root.mainloop()
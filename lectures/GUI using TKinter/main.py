from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)#helps to add padding

#Label

my_label = Label(text="I Am a Label", font=("Arial", 12, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="New_button")
new_button.grid(column=2,row=0)

#Entry
input = Entry()
input.grid(column=3,row=2)
# input.pack()


# button.pack()

window.mainloop()
from tkinter import *
import tkinter.messagebox

def save_data():
    fileD = open("orders.txt", "a")
    fileD.write("Category:\n")
    fileD.write("%s\n" % Category.get())
    fileD.write("Size:\n")
    fileD.write("%s\n" % Size.get())
    fileD.write("Color:\n")
    fileD.write("%s\n" % Color.get())
    fileD.write("Quantity:\n")
    fileD.write("%s\n" % Quantity.get())
    fileD.write("Name:\n")
    fileD.write("%s\n" % name.get())
    fileD.write("Address:\n")
    fileD.write("% s\n" % address.get("1.0", END))
    Category.set('')
    Size.set('')
    Color.set('')
    Quantity.set('')
    name.delete(0, END)
    address.delete("1.0", END)
    tkinter.messagebox.showinfo('Order Confirmation', 'Thank you for your order. '
                                                      'You will be notified when your order has been shipped.')
def read_Categories(file):
    Categories = []
    Size = []
    Color = []
    Quantity = []
    Categories_f = open(file)
    for line in Categories_f:
        as_list = line.split("|")
        Categories.append(as_list[0])
    return Categories

def read_Size(file):
    Categories = []
    Size = []
    Color = []
    Quantity = []
    Size_f = open(file)
    for line in Size_f:
        as_list = line.split("|")
        Size.append(as_list[1])
    return Size

def read_Color(file):
    Categories = []
    Size = []
    Color = []
    Quantity = []
    Color_f = open(file)
    for line in Color_f:
        as_list = line.split("|")
        Color.append(as_list[2])
    return Color

def read_Quantity(file):
    Categories = []
    Size = []
    Color = []
    Quantity = []
    Quantity_f = open(file)
    for line in Quantity_f:
        as_list = line.split("|")
        Quantity.append(as_list[3])
    return Quantity

app = Tk()
app.title('NOZOMU Apparel Shop On-line')
Label(app, text="Category:").pack()
Category = StringVar()
Category.set(None)
options = read_Categories("size.txt")
OptionMenu(app, Category, *options).pack()
Label(app, text="Size:").pack()
Size = StringVar()
Size.set(None)
options = read_Size("size.txt")
OptionMenu(app, Size, *options).pack()
Label(app, text="Color:").pack()
Color = StringVar()
Color.set(None)
options = read_Color("size.txt")
OptionMenu(app, Color, *options).pack()
Label(app, text="Quantity:").pack()
Quantity = StringVar()
Quantity.set(None)
options = read_Quantity("size.txt")
OptionMenu(app, Quantity, *options).pack()
Label(app, text = "Name:").pack()
name = Entry(app)
name.pack()
Label(app, text="Address:").pack()
address =Text(app)
address.pack()

Button(app, text="Order", command=save_data).pack()
app.mainloop()



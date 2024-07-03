# TKINTER
# - Needs to be imported but does not need to be installed because it is
# part of the core python stack
# - Library that is used to build GUIs in python
import tkinter as tk

# Create window
root = tk.Tk()

root.geometry("500x500")  # x-value, y-value
root.title("My First GUI")

# Pass the parent window
# Font is specified as a tuple
# LABEL = label for the window
label = tk.Label(root, text="Hello World!", font=('Arial, 18'))
label.pack(padx=20, pady=20)

# TEXTBOX = text entry, can be multiple lines
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

# ENTRY = text box of height 1 line
myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

# BUTTON
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()

###############################################################################
# TKINTER WINDOWS
#
# Tkinter = module for GUI toolkit, included with Python
#
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


from tkinter import *


window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

# Convert to photo image
icon = PhotoImage(file='logo.png')  # placeholder filepath
window.iconphoto(True, icon)
# Can be text or hexidecimal
window.config(background="black")
window.config(background="#5cfcff")

window.mainloop()   # place window on computer screen, listen for events

###############################################################################
# TKINTER NEW WINDOWS
#
# Toplevel() = new window 'on top' of other windows
# - Linked to a 'bottom' window so when bottom window closes, so does top level
# Tik() = new independent window

from tkinter import *


def create_window():
    new_window = Toplevel()
    old_window.destroy()    # closes out of old window


old_window = Tk()

Button(old_window, text="Create New Window", command=create_window).pack()

old_window.mainloop()

###############################################################################
# TKINTER WINDOW TABS


from tkinter import *
from tkinter import ttk  # contains other widgets


window = Tk()

# Widget that manages a collection of windows/displays
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)  # new frame for tab 1
tab2 = Frame(notebook)  # new frame for tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
# expand = expand to fill any space not otherwise used
# fill = fill space on x and y axis
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab #1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab #2", width=50, height=25).pack()

window.mainloop()

###############################################################################
# TKINTER GRIDS
#
# grid() = geometry manager that organizes widgets in a table-like structure
# in a parent
# - Column expands to largest widget


from tkinter import *

window = Tk()

titleLabel = Label(window,
                   text="Enter your info",
                   font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window,
                       text="First name: ",
                       width=20,
                       bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window,
                      text="Last name: ",
                      bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window,
                   text="Email: ",
                   width=30,
                   bg="blue").grid(row=3, column=0)
emailEntry = Entry(window).grid(row=4, column=1)

# column span = place widget in between two columns
submitButton = Button(window,
                      text="Submit").grid(row=3, column=0, columnspan=2)

window.mainloop()

###############################################################################
# TKINTER LABELS
#
# label = an area widget that holds text and/or an image within a window
# - Will expand based on widgets


from tkinter import *


window = Tk()

photo = PhotoImage(file='person.png')  # placeholder filepath
label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',     # foreground
              bg='black',       # background
              relief=RAISED,
              bd=10,
              padx=20,          # padding x
              pady=20,          # padding y
              image=photo,
              compound='bottom')  # displays both text and an image
label.pack()    # add label to window
# label.place(x=0, y=0)   # place label at designated x and y coordinates

window.mainloop()   # place window on computer screen, listen for events

###############################################################################
# TKINTER BUTTONS
#
# buttons = click it and it does stuff


from tkinter import *


count = 0


def click():
    global count
    count += 1
    print(count)

window = Tk()  # instantiate an instance of a window

photo = PhotoImage(file='like.png') # placeholder filepath

button = Button(window,
                text="click me!",
                command=click,  # list function name without parentheses
                font=("Comic Sans", 30),
                fg="00FF00",
                bg="black",
                activeforeground="00FF00",
                activebackground="black",
                state=ACTIVE, # can put active/disabled
                image=photo,
                compound='bottom')  # displays both text and image

button.pack()       # display button

window.mainloop()   # place window on computer screen, listen for events

###############################################################################
# TKINTER ENTRY BOX
#
# entry widget = textbox that accepts a single line of user input


from tkinter import *


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)  # deletes all characters within entry box


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")     # character to show when typing
entry.insert(0, 'Spongebob')  # default text
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()

###############################################################################
# TKINTER CHECKBOX


from tkinter import *


def display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("You don't agree :( ")

window = Tk()

x = IntVar()    # this is because we are storing a 1 or a 0 for on/off value

python_photo = PhotoImage(file='python.png')    # placeholder filepath

# Stores a 1 or 0 as a result
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,   # value when checked
                           offvalue=0,  # value when unchecked
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,  # add image to checkbox
                           # where you are adding the photo in relation to text
                           compound='left')
check_button.pack()

window.mainloop()

###############################################################################
# TKINTER RADIO BUTTONS
#
# radio button = can only select one from a group


from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if(x.get() == 0):
        print("You ordered a pizza!")
    elif(x.get() == 1):
        print("You ordered a hamburger!")
    elif(x.get() == 2):
        print("You ordered a hotdog!")
    else:
        print("Huh?")

window = Tk()

# Images need to be created after window instantiation
pizzaImage = PhotoImage(file='pizza.png')           # placeholder filepath
hamburgerImage = PhotoImage(file='hamburger.png')   # placeholder filepath
hotdogImage = PhotoImage(file='hotdog.png')         # placeholder filepath
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

# Iterate through each item in list
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              # adds text to radio buttons
                              text=food[index],
                              # groups radiobuttons together if they share the
                              # same variable
                              variable=x,
                              # assigns each radiobutton a different value
                              value=index,
                              # adds padding on x-axis
                              padx=25,
                              font=("Impact", 50),
                              # adds image to radiobutton
                              image=foodImages[index],
                              # adds image and text (left side)
                              compound='left',
                              # eliminate circle indicators
                              indicatoron=0,
                              # sets width of radio buttons
                              width=375,
                              # set command of radiobutton to function
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()

###############################################################################
# TKINTER LISTBOX
#
# listbox = a listing of selectable text items within its own container


def submit():
    food = []

    # Iterates through each selected item and gets the index and the item at
    # that index
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())

    # Adjust the listbox size once new item is added
    listbox.config(height=listbox.size())


def delete():
    # Start with last index because deleting from front will change the indices
    # of the items
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    # Adjust the listbox size once new item is deleted
    listbox.config(height=listbox.size())


from tkinter import *


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)  # Select multiple items from listbox
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()


window.mainloop()

###############################################################################
# TKINTER MESSAGEBOX


from tkinter import messagebox  # import messagebox library


# Different types of message boxes
def click():
    # messagebox.showinfo(title='This is an info message box',
    #                     message='You are a person')
    # messagebox.showwarning(title='WARNING!', message='You have A VIRUS!!')
    # messagebox.showerror(title='ERROR!!', message='Something went wrong')

    # # Returns T/F
    # if messagebox.askokcancel(title='ask ok cancel',
    #                     message='Do you want to do the thing?'):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing! :(")

    # # Returns T/F
    # if messagebox.askretrycancel(title='ask retry cancel',
    #                     message='Do you want to retry the thing?'):
    #     print("You retried a thing!")
    # else:
    #     print("You canceled a thing! :(")

    # # Returns T/F
    # if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
    #     print("I like cake too :)")
    # else:
    #     print("Why do you not like cake? :(")

    # # Returns 'yes' or 'no' string
    # answer = messagebox.askquestion(title='ask question',
    #                                 message='Do you like pie?')
    # if (answer == 'yes'):
    #     print('I like pie too :) ')
    # else:
    #     print('Why do you not like pie? :(')

    # Returns True, False, or None
    answer = messagebox.askyesnocancel(title='yes no cancel',
                                       message='Do you like to code?',
                                       icon='warning')
    if (answer == True):
        print("You like to code :)")
    elif (answer == False):
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window, command=click, text='Click Me')
button.pack()

window.mainloop()

###############################################################################
# TKINTER COLOR CHOOSER


from tkinter import *
from tkinter import colorchooser  # submodule


def click():
    color = colorchooser.askcolor()     # provides tuple of RGB and Hex
    colorRGB = color[0]
    colorHex = color[1]
    window.config(bg=colorHex)          # change background color


window = Tk()
window.geometry("420x420")

button = Button(text='Click Me', command=click)
button.pack()

window.mainloop()

###############################################################################
# TKINTER TEXT AREA
#
# text widget = enter multiple lines of text, functions like a text area


from tkinter import *


def submit():
    input = text.get("1.0", END)    # get first line to end
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8,   # number of characters high
            width=20,   # number of characters long
            padx=20,
            pady=20,
            fg="purple")    # font color
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()

###############################################################################
# TKINTER FILE DIALOG


from tkinter import *
from tkinter import filedialog


def openFile():
    # Returns string of filepath to selected file
    filepath = filedialog.askopenfilename(initialdir="",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()

###############################################################################
# TKINTER SAVE FILE


from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                        ])
    if file is None:
        return
    # filetext = str(text.get(1.0, END))    # enter text via text area
    filetext = input("Enter some text: ")   # enter text via console
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='Save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()

###############################################################################
# TKINTER MENUBAR


from tkinter import *


def openFile():
    print("File has been opened")


def saveFile():
    print("File has been saved")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You pasted some text!")


window = Tk()

openImage = PhotoImage(file="file.png") # sample file
saveImage = PhotoImage(file="save.png") # sample file
exitImage = PhotoImage(file="exit.png") # sample file

menubar = Menu(window)
window.config(menu=menubar)

# For each menubar tab, create separate menu and add each menu to menubar
# Menubar added to window

fileMenu = Menu(menubar,
                tearoff=0,
                font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)    # dropdown under filemenu
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar,
                tearoff=0,
                font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()

###############################################################################
# TKINTER FRAMES
#
# frame = a rectangular container to group and hold widgets


from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.place(x=100, y=100)

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()

###############################################################################
# TKINTER PROGRESS BAR


from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%")
        text.set(str(x + "/" + GB) + " GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = ProgressBar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()

###############################################################################
# TKINTER CANVAS
#
# canvas = widget that is used to draw graphs, plots, images in a window


from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# Pass start and end coordinates
canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
canvas.create_line(0, 500, 500, 0, fill="red", width=5)

canvas.create_rectangle(50, 50, 250, 250, fill="purple")

points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill="yellow",
                      outline="black", width=5)

# Style options: PIESLICE, CHORD, ARC
canvas.create_arc(0, 0, 500, 500,
                  fill="green",
                  style=PIESLICE,
                  start=270,
                  extent=180)

# Create pokeball
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)

canvas.pack()

window.mainloop()

###############################################################################
# TKINTER KEY EVENTS
#
# window.bind(event, function)

from tkinter import *


def doSomething(event):
    # print("You pressed: " + event.keysym)
    # Label will display the key that was pressed
    label.config(text=event.keysym)

window = Tk()

# window.bind("<Key>", doSomething)  # any key
window.bind("<Return>", doSomething)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()

###############################################################################
# TKINTER MOUSE EVENTS
#
# window.bind(event, function)


from tkinter import *


def doSomething(event):
    print("Mouse coordinates: " + str(event.x) + ", " + str(event.y))


window = Tk()

window.bind("<Button-1>", doSomething)  # Left mouse click
window.bind("<Button-2>", doSomething)  # Scroll wheel
window.bind("<Button-3>", doSomething)  # Right mouse click
window.bind("<ButtonRelease>", doSomething)
window.bind("<Enter>", doSomething)     # Enter the window
window.bind("<Leave>", doSomething)     # Leave the window
window.bind("<Motion>", doSomething)    # Where the mouse moved

window.mainloop()

###############################################################################
# DRAG AND DROP WIDGETS
#
# label.bind(event, function)


from tkinter import *


def drag_start(event):
    widget = event.widget   # Gets widget of event we're dealing with
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget   # Gets widget of event we're dealing with

    # winfo_x() = Gets top left x-coordinate of label relative to window
    x = widget.winfo_x() - widget.startX + event.x
    # winfo_y() = Gets top left y-coordinate of label relative to window
    x = widget.winfo_y() - widget.startY + event.y
    # New coordinates for widget
    widget.place(x=x, y=y)


window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=0, y=0)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)


window.mainloop()

###############################################################################
# MOVE WIDGET WITHIN WINDOW

from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


myimage = PhotoImage(file="racecar.png")  # placeholder file

label = Label(window, image=myimage, bg="red")
label.place(x=0, y=0)

window.mainloop()

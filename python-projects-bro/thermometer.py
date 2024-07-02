from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

hotImage = PhotoImage(file='hot.png')   # placeholder filepath
hotLabel = Label(image=hotImage)
hotLabel.pack()

coldImage = PhotoImage(file='cold.png')   # placeholder filepath
coldLabel = Label(image=coldImage)
coldLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # orientation of scale
              font=('Consolas', 20),
              tickinterval=10,  # add numeric indicators for value
              showvalue=0,      # hide current value
              resolution=5,     # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.pack()
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
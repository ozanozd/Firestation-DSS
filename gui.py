from tkinter import *
import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
canvas = Canvas(top , height = 400 , width = 400)
label_left = Label(top , text = "Model Extension" ,  underline = 0)
label_right = Label(top , text = "Model Type" ,   underline = 1)
button1 = Button(top , text = "Load" )
button2 = Button(top , text = "Select" )
button3 = Button(top , text = "Run Map" , bg = "blue" )
user_entry = Entry(top , font = 16)
checkbutton1 = Checkbutton(top , text = "Capacity" )
checkbutton2 = Checkbutton(top , text = "Traffic" )
radiobutton1 = Radiobutton(top , text = "Single Coverage" )
radiobutton2 = Radiobutton(top , text = "Multi Coverage")
checkbutton1.select

user_entry.place(x = 25 , y = 10 , width = 260 , height = 30)
button1.place(x = 350 , y = 10 , height = 30)
button2.place(x = 300 , y = 10 , height = 30)

label_left.place(x = 50 , y = 60 )
checkbutton1.place(x = 50 , y = 90 )
checkbutton2.place(x = 50 , y = 110 )

label_right.place(x = 250 , y = 60)
radiobutton1.place(x = 250 , y = 90 )
radiobutton2.place(x = 250 , y = 110 )

button3.place(x = 150 ,  y = 300 )

canvas.pack()
top.mainloop()

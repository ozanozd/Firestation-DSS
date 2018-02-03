"""
This program creates necessary gui for the decision support system.It based on the native library of python tkinter
"""

from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename

def load_file(user_entry_box):
    """
    When the load button is pressed this function is invoked.It is responsible of two things:
        i)  Call the file chooser function
        ii) Load the excel file
    """
    filename = askopenfilename()
    user_entry_box.insert(0 , filename)

def select_file():
    """
    When the select button is pressed this function is invoked.It is responsible for finalizing the file to load the file.
    """
    pass

def check_capacity():
    """
    When the capacity button is checked this function is invoked.
    """
    pass

def check_traffic():
    """
    When the traffic button is checked this function is invoked.
    """
    pass

def check_single_coverage():
    """
    When the single coverage button is selected this function is invoked.
    """
    pass

def check_multi_coverage():
    """
    When the multi coverage button is selected this function is invoked.
    """
    pass

def run_map():
    """
    When the run map button is selected this function is invoked.
    """
    pass

def prepare_gui():
    """
    This function creating gui items and initialize them
    """
    top = tkinter.Tk()
    # Code to add widgets will go here...
    canvas = Canvas(top , height = 400 , width = 400)
    label_left = Label(top , text = "Model Extension" ,  underline = 0)
    label_right = Label(top , text = "Model Type" ,   underline = 1)
    user_entry_box = Entry(top , font=("Calibri",12))
    load_button = Button(top , text = "Load"  , command = lambda: load_file(user_entry_box))
    select_button = Button(top , text = "Select" )
    runmap_button = Button(top , text = "Run Map"  )
    capacity_checkbutton = Checkbutton(top , text = "Capacity")
    traffic_checkbutton = Checkbutton(top , text = "Traffic")
    single_coverage_radiobutton = Radiobutton(top , text = "Single Coverage")
    multi_coverage_radiobutton = Radiobutton(top , text = "Multi Coverage")


    user_entry_box.place(x = 25 , y = 10 , width = 260 , height = 30)
    load_button.place(x = 350 , y = 10 , height = 30)
    select_button.place(x = 300 , y = 10 , height = 30)

    label_left.place(x = 50 , y = 60)
    capacity_checkbutton.place(x = 50 , y = 90)
    traffic_checkbutton.place(x = 50 , y = 110)

    label_right.place(x = 250 , y = 60)
    single_coverage_radiobutton.place(x = 250 , y = 90)
    multi_coverage_radiobutton.place(x = 250 , y = 110)

    runmap_button.place(x = 150 ,  y = 300)

    canvas.pack()
    top.mainloop()

prepare_gui()

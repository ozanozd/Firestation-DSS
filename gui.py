"""
This program creates necessary gui for the decision support system.It based on the native library of python tkinter
"""

from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
import os.path

def load_file(user_entry_box):
    """
    When the load button is pressed this function is invoked.It is responsible of two things:
        i)  Call the file chooser function
        ii) Load the excel file
    """
    filename = askopenfilename()
    user_entry_box.insert(0 , filename)

def check_validity_threshold(user_threshold_entry):
    """
    This function checks validity of the user's threshold
    """
    if type(user_threshold_entry.get()) != type(5) :
        return False

    return True

def select_threshold(user_threshold_entry):
    """
    This function selects a threshold and check whether corresponding availability_matrix exists or not.
       i)  If it exists then , use this excel filename
       ii) If not , create the corresponding excel file and use it.
    """

    #Check whether the entry is integer or Note
    if check_validity_threshold(user_threshold_entry) == False:
        pass

    file_path =  os.path()

    if os.path.exists(file_path)


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
    canvas = Canvas(top , height = 450 , width = 450)
    label_left = Label(top , text = "Model Extension" ,  underline = 0)
    label_right = Label(top , text = "Model Type" ,   underline = 0)
    label_threshold = Label(top , text = "Threshold(m)")
    user_entry_box = Entry(top , font = ("Calibri" , 12))
    user_threshold_entry = Entry(top , text = "Threshold" ,  font = ("Calibri" , 12) , command = lambda: check_validity_threshold(user_threshold_entry) )
    load_button = Button(top , text = "Load"  , command = lambda: load_file(user_entry_box))
    select_button = Button(top , text = "Select" )
    threshold_select_button = Button(top , text = "Select" , command = lambda: select_threshold(user_threshold_entry))
    runmap_button = Button(top , text = "Run Map"  )
    capacity_checkbutton = Checkbutton(top , text = "Capacity")
    traffic_checkbutton = Checkbutton(top , text = "Traffic")
    risk_checkbutton = Checkbutton(top , text = "Risk Factors")
    single_coverage_radiobutton = Radiobutton(top , text = "Single Coverage")
    multi_coverage_radiobutton = Radiobutton(top , text = "Multi Coverage")


    user_entry_box.place(x = 25 , y = 10 , width = 260 , height = 30)
    user_threshold_entry.place(x = 300 , y = 250 , width = 50 , height = 25)
    label_threshold.place(x = 220 , y = 255)
    threshold_select_button.place(x = 360 , y = 250 )
    load_button.place(x = 350 , y = 10 , height = 30)
    select_button.place(x = 300 , y = 10 , height = 30)

    label_left.place(x = 50 , y = 60)
    capacity_checkbutton.place(x = 50 , y = 90)
    traffic_checkbutton.place(x = 50 , y = 110)
    risk_checkbutton.place(x = 50 , y = 130)

    label_right.place(x = 250 , y = 60)
    single_coverage_radiobutton.place(x = 250 , y = 90)
    multi_coverage_radiobutton.place(x = 250 , y = 110)

    runmap_button.place(x = 150 ,  y = 300)

    canvas.pack()
    top.mainloop()

prepare_gui()

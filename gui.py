"""
This program creates necessary gui for the decision support system.It based on the native library of python tkinter
"""
#Works to be done:
# i) Add threshold as an user entry to gui
# ii) Edit radiobutton in a way that only one of them can be selected


import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import write_excel_availability_matrix as writer
import os.path

#Define height and width as constants
HEIGHT = 400
WIDTH = 415

class MainApplication:
    def __init__(self , master):
        self.master = master
        self.canvas = tk.Canvas(master , height = HEIGHT , width = WIDTH)

        # Define labels for Radiobuttons and Checkbuttons , threshold
        self.label_left = tk.Label(self.canvas , text = "Model Extension")
        self.label_right = tk.Label(self.canvas , text = "Model Type")
        self.label_threshold = tk.Label(self.canvas , text = "Threshold(m)")

        # Define user entries
        self.user_entry_box = tk.Entry(self.canvas , font = ("Calibri" , 12))
        self.user_threshold_entry = tk.Entry(self.canvas , text = "Threshold" ,  font = ("Calibri" , 12))

        # Define buttons
        self.load_button = tk.Button(self.canvas , text = "Load"  , command = lambda: load_file(user_entry_box))
        self.select_button = tk.Button(self.canvas , text = "Select")
        self.runmap_button = tk.Button(self.canvas , text = "Run Map" , command =  self.run_map)

        # Define checkbuttons
        self.capacity_checkbutton = tk.Checkbutton(self.canvas , text = "Capacity")
        self.traffic_checkbutton = tk.Checkbutton(self.canvas , text = "Traffic")
        self.risk_checkbutton = tk.Checkbutton(self.canvas , text = "Risk Factors")

        # Initialize radiobuttons as all of them are unselected
        self.radio_button_var = tk.IntVar()
        self.radio_button_var.set(2356)

        # Define radio_buttons
        self.single_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Single Coverage" , value = 1 , variable = self.radio_button_var)
        self.multi_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Multi Coverage" , value = 2 , variable = self.radio_button_var)


        # Place them
        self.user_entry_box.place(x = 25 , y = 10 , width = 260 , height = 30)
        self.user_threshold_entry.place(x = 340 , y = 275 , width = 50 , height = 25)
        self.label_threshold.place(x = 250 , y = 275)
        self.load_button.place(x = 350 , y = 10 , height = 30)
        self.select_button.place(x = 300 , y = 10 , height = 30)

        self.label_left.place(x = 50 , y = 60)
        self.capacity_checkbutton.place(x = 50 , y = 90)
        self.traffic_checkbutton.place(x = 50 , y = 110)
        self.risk_checkbutton.place(x = 50 , y = 130)

        self.label_right.place(x = 250 , y = 60)
        self.single_coverage_radiobutton.place(x = 250 , y = 90)
        self.multi_coverage_radiobutton.place(x = 250 , y = 110)

        self.runmap_button.place(x = 180 ,  y = 350)
        self.canvas.pack()

    def check_validity_threshold(self):
        """
        This function checks validity of the user's threshold
        """
        try :
            int(self.user_threshold_entry.get())
            return True
        except ValueError :
            return False

        return True
    def run_map(self):
        if self.check_validity_threshold() == False :
            messagebox.showerror("Wrong type!" , "Please enter an integer value.")
            self.user_threshold_entry.delete(0 , len(self.user_threshold_entry.get()))

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()





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

    filename = "availability_matrix_" + user_threshold_entry.get() + "xlsx"
    file_path =  os.path(filename)

    # If the file is already exists use it.Otherwise , create it
    if os.path.exists(file_path) == True :
        pass
    else :
        writer.run()
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

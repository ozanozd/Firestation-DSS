"""
This program creates necessary gui for the decision support system.It based on the native library of python tkinter
Gui is designed in object oriented style.
"""
#Works to be done:
# i) Add threshold as an user entry to gui
# ii) Edit radiobutton in a way that only one of them can be selected

#General library imports
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path

#Inside project imports
import cplex_imp as solver
import map

#Define height and width as constants
HEIGHT = 400
WIDTH = 415

def check_availability_matrix(from_district , to_district , distance , threshold):
    """
    This function check whether a Availability_Matrix_threshold.xlsx exists or not.
    If it does not exists it creates it  and write it to excel and returns it.
    Otherwise it read it and returns it
    """
    current_directory = solver.writer.reader.util.get_current_directory()
    file_name = "availability_matrix_" + str(threshold) + ".xlsx"
    full_path = current_directory + "/Availability_Matrix/" + file_name
    if os.path.isfile(full_path) == True:
        print(file_name , "is already exists.")
        availability_matrix = solver.writer.reader.read_availability_matrix(file_name)
        print(file_name , "is read.")
        return availability_matrix
    else:
        print(file_name , "does not exist.")
        availability_matrix = solver.writer.reader.util.generate_availability_matrix(from_district , to_district , distance , threshold)
        print("Availability_Matrix is created")
        solver.writer.write_availability_matrix_excel(availability_matrix , threshold)
        print("Availability_Matrix is written")
        return availability_matrix


def check_dat_file(file_name):
    """
    This function checks whether filename.dat file exist or not.
    If it exists then use it , otherwise write it then use it
    """

    current_directory = solver.writer.reader.util.get_current_directory()
    full_path = current_directory + "/Mod_Files/" + file_name

    if os.path.isfile(full_path) == True:
        return True
    else :
        return False


def check_solver(file_name):
    """
    This function checks whether there exists a file_name.txt or not
    """

    current_directory = solver.writer.reader.util.get_current_directory()
    full_path = current_directory + "/Solutions/" + file_name

    if os.path.isfile(full_path) == True:
        return True
    else :
        return False

class MainApplication:
    def __init__(self , master):
        self.master = master
        self.canvas = tk.Canvas(master , height = HEIGHT , width = WIDTH)

        # Define labels for Radiobuttons and Checkbuttons , threshold
        self.label_model= tk.Label(self.canvas , text = "Models")
        self.label_threshold = tk.Label(self.canvas , text = "Threshold(m)")

        # Define user entries
        self.user_entry_box = tk.Entry(self.canvas , font = ("Calibri" , 12))
        self.user_threshold_entry = tk.Entry(self.canvas , text = "Threshold" ,  font = ("Calibri" , 12) , state = tk.DISABLED)

        # Define buttons
        self.load_button = tk.Button(self.canvas , text = "Load"  , command = lambda: load_file(user_entry_box))
        self.select_button = tk.Button(self.canvas , text = "Select")
        self.runmap_button = tk.Button(self.canvas , text = "Run Map" , command =  self.run_map)

        # Initialize radiobuttons as all of them are unselected
        self.radio_button_var = tk.IntVar()
        self.radio_button_var.set(2356)

        # Define radio_buttons
        self.single_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Base Model" , value = 1 , variable = self.radio_button_var , command = self.select_base_model)
        self.multi_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Multicoverage Model" , value = 2 , variable = self.radio_button_var , command = self.select_multi_coverage)
        self.maximum_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Maximum Coverage Model" , value = 3 , variable = self.radio_button_var , command = self.select_maximum_coverage)
        self.base_model_diff_cost_radiobutton = tk.Radiobutton(self.canvas , text = "Base Model with different cost" , value = 4 , variable = self.radio_button_var , command = self.select_base_model_diff_cost)
        self.stochastic_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Stochastic Coverage Model" , value = 5 , variable = self.radio_button_var , command = self.select_stochastic_coverage)
        self.stochastic_maximum_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Stochastic Maximum Coverage Model" , value = 6 , variable = self.radio_button_var , command = self.select_stochastic_maximum_coverage)


        # Place them
        self.user_entry_box.place(x = 25 , y = 10 , width = 260 , height = 30)
        self.user_threshold_entry.place(x = 340 , y = 275 , width = 50 , height = 25)
        self.label_threshold.place(x = 250 , y = 275)
        self.load_button.place(x = 350 , y = 10 , height = 30)
        self.select_button.place(x = 300 , y = 10 , height = 30)

        self.label_model.place(x = 50 , y = 60)
        self.single_coverage_radiobutton.place(x = 50 , y = 85)
        self.multi_coverage_radiobutton.place(x = 50 , y = 110)
        self.maximum_coverage_radiobutton.place(x = 50 , y = 135)
        self.base_model_diff_cost_radiobutton.place(x = 50 , y = 160)
        self.stochastic_coverage_radiobutton.place(x = 50 , y = 185)
        self.stochastic_maximum_coverage_radiobutton.place(x = 50 , y = 210)

        self.runmap_button.place(x = 180 ,  y = 350)
        self.canvas.pack()

        self.dat_file_name = ""

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

    def active_user_threshold_entry(self):
        """
        This function activates user_threshold_entry
        """
        print("User threshold entry activated.")
        self.user_threshold_entry.configure(state = tk.NORMAL)

    def deactive_user_threshold_entry(self):
        """
        This function activates user_threshold_entry
        """
        print("User threshold entry deactivated.")
        self.user_threshold_entry.configure(state = tk.DISABLED)

    def select_base_model(self):
        """
        """
        print("We selected Base Model")
        print(self.radio_button_var.get())
        self.active_user_threshold_entry()
        self.dat_file_name = "BaseModel_"

    def select_multi_coverage(self):
        """
        """
        print("We selected Multi Coverage")
        self.active_user_threshold_entry()
        self.dat_file_name = "MultiCoverage_"

    def select_maximum_coverage(self):
        """
        """
        print("We selected Maximum Coverage")
        self.active_user_threshold_entry()
        self.dat_file_name = "MaximumCoverage_"

    def select_base_model_diff_cost(self):
        """
        """
        print("We selected Base Model Diff Cost")
        self.active_user_threshold_entry()
        self.dat_file_name = "BaseModel_Diff_Cost_"

    def select_stochastic_coverage(self):
        """
        """
        print("We selected Stochastic Coverage")
        self.deactive_user_threshold_entry()
        self.dat_file_name = "Stochastic_Coverage_"

    def select_stochastic_maximum_coverage(self):
        """
        """
        print("We selected Stochastic Maximum Coverage")
        self.deactive_user_threshold_entry()
        self.dat_file_name = "Stochastic_Maximum_Coverage_"

    def run_map(self):
        """
        Run the map with given user choices
        """

        #Get threshold and selected model number
        threshold = int(self.user_threshold_entry.get())
        choice = self.radio_button_var.get()

        #Prepare needed variables
        name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances = solver.writer.reader.read_district_file()
        risks = solver.writer.reader.read_risk()
        print("District file is read")

        #If the choice is not multicoverage use availability_matrix
        if choice != 2:
            availability_matrix = check_availability_matrix(from_districts , to_districts , distances , threshold)
        else :
            risk_availability_matrix = solver.writer.reader.util.generate_risk_availability_matrix(from_districts , to_districts , distances , risks , threshold)
            risk_indicator = solver.writer.reader.util.generate_risk_indicator(risks)
            risk_array = solver.writer.reader.util.generate_risk_array()

        #Create fixed_cost
        fixed_cost = solver.writer.reader.util.generate_fixed_cost_array()
        print("Fixed_cost is created")

        #Create or use dat file
        if check_dat_file(self.dat_file_name + str(threshold) + ".dat") == False:
            if choice == 1:
                solver.writer.write_dat(availability_matrix , fixed_cost , threshold)
                print(".dat file is created")
            elif choice == 2:
                solver.writer.write_multi_dat(risk_availability_matrix , risk_indicator , risk_array ,  fixed_cost , threshold)
            elif choice == 3:
                solver.writer.write_max_coverage_dat()
            elif choice == 4:
                solver.writer.write_base_mod_diff_cost_dat()
            elif choice == 5:
                solver.writer.write_stochastic_coverage_dat()
            elif choice == 6:
                solver.writer.write_stochastic_max_covarage_dat()

        else:
            print("We have already .dat file.")

        if check_solver(self.dat_file_name + "Sol" + str(threshold) + ".txt") == False:
            file_name = solver.run(choice , threshold)
            print("Solver solved and txt is created.")
        else:
            print("We have already a solution array.")
        solution_array = solver.writer.reader.read_cloud_solution(file_name)
        print("Solution array is read")
        map.run(solution_array , name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances)


        ## TODO: Input chech
        #map.run()

        #if self.check_validity_threshold() == False :
        #    messagebox.showerror("Wrong type!" , "Please enter an integer value.")
        #       self.user_threshold_entry.delete(0 , len(self.user_threshold_entry.get()))

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

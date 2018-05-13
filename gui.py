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
        self.label_threshold = tk.Label(self.canvas , text = "Threshold (m)")
        self.label_min_threshold = tk.Label(self.canvas , text = "Threshold (min)")
        self.label_facility = tk.Label(self.canvas , text = "Facility Number")
        self.label_confidence = tk.Label(self.canvas , text = "Conf Int (0-100)")

        # Define user entries
        self.user_entry_box = tk.Entry(self.canvas , font = ("Calibri" , 12))
        self.user_threshold_entry = tk.Entry(self.canvas , text = "Threshold" ,  font = ("Calibri" , 12) , state = tk.DISABLED)
        self.user_min_threshold_entry = tk.Entry(self.canvas , text = "Min_Threshold" ,  font = ("Calibri" , 12) , state = tk.DISABLED)
        self.user_facility_entry = tk.Entry(self.canvas , text = "Facility" ,  font = ("Calibri" , 12) , state = tk.DISABLED)
        self.user_confidence_entry = tk.Entry(self.canvas , text = "Confidence" ,  font = ("Calibri" , 12) , state = tk.DISABLED)

        # Define buttons
        self.load_button = tk.Button(self.canvas , text = "Load"  , command = self.load_file)
        self.select_button = tk.Button(self.canvas , text = "Select" , command = self.run_selected_solution)
        self.runmap_button = tk.Button(self.canvas , text = "Run Map" , command =  self.run_map)

        # Initialize radiobuttons as all of them are unselected
        self.radio_button_var = tk.IntVar()
        self.radio_button_var.set(2356)

        # Define radio_buttons
        self.single_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Base Model" , value = 1 , variable = self.radio_button_var , command = self.select_base_model)
        self.multi_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Multicoverage Model" , value = 2 , variable = self.radio_button_var , command = self.select_multi_coverage)
        self.maximum_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Maximum Coverage Model" , value = 3 , variable = self.radio_button_var , command = self.select_maximum_coverage)
        self.stochastic_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Stochastic Coverage Model" , value = 4 , variable = self.radio_button_var , command = self.select_stochastic_coverage)
        self.stochastic_maximum_coverage_radiobutton = tk.Radiobutton(self.canvas , text = "Stochastic Maximum Coverage Model" , value = 5 , variable = self.radio_button_var , command = self.select_stochastic_maximum_coverage)


        # Place them
        self.user_entry_box.place(x = 25 , y = 10 , width = 260 , height = 30)
        self.user_threshold_entry.place(x = 340 , y = 255 , width = 50 , height = 25)
        self.user_min_threshold_entry.place(x = 340 , y = 295 , width = 50 , height = 25)
        self.user_facility_entry.place(x = 140 , y = 255 , width = 50 , height = 25)
        self.user_confidence_entry.place(x = 140 , y = 295 , width = 50 , height = 25)
        self.label_threshold.place(x = 250 , y = 255)
        self.label_min_threshold.place(x = 250 , y = 295)
        self.label_facility.place(x = 50 , y = 255)
        self.label_confidence.place(x = 50 , y = 295)
        self.load_button.place(x = 350 , y = 10 , height = 30)
        self.select_button.place(x = 300 , y = 10 , height = 30)

        self.label_model.place(x = 50 , y = 60)
        self.single_coverage_radiobutton.place(x = 50 , y = 85)
        self.multi_coverage_radiobutton.place(x = 50 , y = 110)
        self.maximum_coverage_radiobutton.place(x = 50 , y = 135)
        self.stochastic_coverage_radiobutton.place(x = 50 , y = 160)
        self.stochastic_maximum_coverage_radiobutton.place(x = 50 , y = 185)

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
        This function deactivates user_threshold_entry
        """
        print("User threshold entry deactivated.")
        self.user_threshold_entry.configure(state = tk.DISABLED)

    def active_user_min_threshold_entry(self):
        """
        This function activates user_min_threshold_entry
        """
        print("User min_threshold entry activated.")
        self.user_min_threshold_entry.configure(state = tk.NORMAL)

    def deactive_user_min_threshold_entry(self):
        """
        This function deactivates user_min_threshold_entry
        """
        print("User min_threshold entry deactivated.")
        self.user_min_threshold_entry.configure(state = tk.DISABLED)

    def active_user_facility_entry(self):
        """
        This function activates user_facility_entry
        """
        print("User facility entry activated.")
        self.user_facility_entry.configure(state = tk.NORMAL)

    def deactive_user_facility_entry(self):
        """
        This function activates user_threshold_entry
        """
        print("User facility entry deactivated.")
        self.user_facility_entry.configure(state = tk.DISABLED)

    def active_user_confidence_entry(self):
        """
        This function activates user_confidence_entry
        """
        print("User onfidence entry activated.")
        self.user_confidence_entry.configure(state = tk.NORMAL)

    def deactive_user_confidence_entry(self):
        """
        This function deactivates user_confidence_entry
        """
        print("User confidence entry deactivated.")
        self.user_confidence_entry.configure(state = tk.DISABLED)

    def select_base_model(self):
        """
        """
        print("We selected Base Model")
        print(self.radio_button_var.get())
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.deactive_user_facility_entry()
        self.dat_file_name = "BaseModel_"

    def select_multi_coverage(self):
        """
        """
        print("We selected Multi Coverage")
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.deactive_user_facility_entry()
        self.dat_file_name = "MultiCoverage_"

    def select_maximum_coverage(self):
        """
        """
        print("We selected Maximum Coverage")
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.active_user_facility_entry()
        self.dat_file_name = "MaximumCoverage_"

    def select_stochastic_coverage(self):
        """
        """
        print("We selected Stochastic Coverage")
        self.deactive_user_threshold_entry()
        self.active_user_min_threshold_entry()
        self.deactive_user_facility_entry()
        self.active_user_confidence_entry()
        self.dat_file_name = "Stochastic_Coverage_"

    def select_stochastic_maximum_coverage(self):
        """
        """
        print("We selected Stochastic Maximum Coverage")
        self.deactive_user_threshold_entry()
        self.active_user_min_threshold_entry()
        self.active_user_facility_entry()
        self.active_user_confidence_entry()
        self.dat_file_name = "Stochastic_Maximum_Coverage_"

    def load_file(self):
        """
        When the load button is pressed this function is invoked.It is responsible of two things:
            i)  Call the file chooser function
            ii) Load the excel file
        """
        filename = askopenfilename()
        self.user_entry_box.insert(0 , filename)


    def run_selected_solution(self):
        """
        """
        file_name = self.user_entry_box.get()
        solution_array = solver.writer.reader.read_selected_solution(file_name)
        print("Solution array is read")
        name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances = solver.writer.reader.read_district_file()
        map.run(solution_array , name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances)

    def run_map(self):
        """
        Run the map with given user choices
        """

        #Get threshold and selected model number
        choice = self.radio_button_var.get()
        if choice <= 3:
            confidence_interval = 0
            is_stochastis = False
            threshold = int(self.user_threshold_entry.get())
            min_threshold = 0
            if choice == 3 :
                facility_number = int(self.user_facility_entry.get())
            else:
                facility_number = 0
        else:
            is_stochastis = True
            min_threshold = int(self.user_min_threshold_entry.get())
            threshold = 0
            confidence_interval = int(self.user_confidence_entry.get())
            if choice == 4 :
                facility_number = 0
            else :
                facility_number = int(self.user_facility_entry.get())


        #Prepare needed variables
        name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances = solver.writer.reader.read_district_file()
        risks = solver.writer.reader.read_risk()
        print("District file is read")

        if choice == 1 or choice == 2 or choice == 3 :
            availability_matrix = solver.writer.reader.util.generate_availability_matrix(from_districts , to_districts , distances , threshold)
            print("Availability_Matrix is created")

        elif choice == 4 or choice == 5:
            random_numbers = solver.writer.reader.read_generated_numbers()
            stochastic_availability_matrix = solver.writer.reader.util.generate_stochastic_availability_matrix(from_districts , to_districts , random_numbers , min_threshold , distances , confidence_interval)
            print("Stochastic matrix is created")
        #Create fixed_cost
        fixed_cost = solver.writer.reader.util.generate_fixed_cost_array()
        print("Fixed_cost is created")

        #Create or use dat file
        if choice == 1 or choice == 2  :
                if choice != 2:
                    solver.writer.write_dat(availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval)
                    print(".dat file is created")
                elif choice == 2:
                    risk_indicator = solver.writer.reader.util.generate_risk_indicator(risks)
                    risk_array = solver.writer.reader.util.generate_risk_array()
                    solver.writer.write_multi_dat(availability_matrix , risk_indicator , risk_array ,  fixed_cost , threshold)

                if check_solver(self.dat_file_name + "Sol" + str(threshold) + ".txt") == False:
                    file_name = solver.run(choice , threshold , confidence_interval , facility_number , min_threshold)
                    print("Solver solved and txt is created.")
                else:
                    print("We have already a solution array.")
        elif choice == 3 :

            solver.writer.write_dat(availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
            if check_solver(self.dat_file_name + "Sol" + str(threshold) + "_" + str(facility_number) + ".txt") == False:
                file_name = solver.run(choice , threshold , confidence_interval , facility_number , min_threshold)
                print("Solver solved and txt is created.")
            else:
                print("We have already a solution array.")

        elif choice == 4 :
            check_dat_file(self.dat_file_name + str(min_threshold) + "_" + str(confidence_interval) +  ".dat") == False
            solver.writer.write_dat(stochastic_availability_matrix , fixed_cost , min_threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
            if check_solver(self.dat_file_name + "Sol" + str(min_threshold) + "_" + str(confidence_interval) +  ".txt") == False:
                file_name = solver.run(choice , threshold , confidence_interval , facility_number , min_threshold)
                print("Solver solved and txt is created.")
            else:
                print("We have already a solution array.")

        elif choice == 5:
            check_dat_file(self.dat_file_name + str(threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".dat") == False
            solver.writer.write_dat(stochastic_availability_matrix , fixed_cost , min_threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
            if check_solver(self.dat_file_name + "Sol" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) +  ".txt") == False:
                file_name = solver.run(choice , threshold , confidence_interval , facility_number , min_threshold)
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

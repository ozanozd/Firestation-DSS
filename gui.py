"""
This program creates necessary gui for the decision support system.It based on the native library of python tkinter
Gui is designed in object oriented style.
"""
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
        self.runmap_button = tk.Button(self.canvas , text = "Run Map" , command =  self.run_map , state= tk.DISABLED)

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

        self.solution_file_name = ""
        self.map_file_name = ""


    def clear_all_inputs(self):
        """
        This function clears all input fields
        It takes no arguments.
        It returns nothing.
        """
        self.user_threshold_entry.delete(0, 'end')
        self.user_min_threshold_entry.delete(0, 'end')
        self.user_facility_entry.delete(0, 'end')
        self.user_confidence_entry.delete(0, 'end')

    def activate_run_map(self):
        """
        This function activates run_map button
        """
        self.runmap_button.configure(state = tk.NORMAL)

    def active_user_threshold_entry(self):
        """
        This function activates user_threshold_entry
        """
        self.user_threshold_entry.configure(state = tk.NORMAL)

    def deactive_user_threshold_entry(self):
        """
        This function deactivates user_threshold_entry
        """
        self.user_threshold_entry.configure(state = tk.DISABLED)

    def active_user_min_threshold_entry(self):
        """
        This function activates user_min_threshold_entry
        """
        self.user_min_threshold_entry.configure(state = tk.NORMAL)

    def deactive_user_min_threshold_entry(self):
        """
        This function deactivates user_min_threshold_entry
        """
        self.user_min_threshold_entry.configure(state = tk.DISABLED)

    def active_user_facility_entry(self):
        """
        This function activates user_facility_entry
        """
        self.user_facility_entry.configure(state = tk.NORMAL)

    def deactive_user_facility_entry(self):
        """
        This function activates user_threshold_entry
        """
        self.user_facility_entry.configure(state = tk.DISABLED)

    def active_user_confidence_entry(self):
        """
        This function activates user_confidence_entry
        """
        self.user_confidence_entry.configure(state = tk.NORMAL)

    def deactive_user_confidence_entry(self):
        """
        This function deactivates user_confidence_entry
        """
        self.user_confidence_entry.configure(state = tk.DISABLED)

    def select_base_model(self):
        """
        """
        self.clear_all_inputs()
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.deactive_user_facility_entry()
        self.solution_file_name = "BaseModel_"
        self.activate_run_map()

    def select_multi_coverage(self):
        """
        """
        self.clear_all_inputs()
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.deactive_user_facility_entry()
        self.solution_file_name = "MultiCoverage_"
        self.activate_run_map()

    def select_maximum_coverage(self):
        """
        """
        self.clear_all_inputs()
        self.active_user_threshold_entry()
        self.deactive_user_min_threshold_entry()
        self.deactive_user_confidence_entry()
        self.active_user_facility_entry()
        self.solution_file_name = "MaxCoverage_"
        self.activate_run_map()

    def select_stochastic_coverage(self):
        """
        """
        self.clear_all_inputs()
        self.deactive_user_threshold_entry()
        self.active_user_min_threshold_entry()
        self.deactive_user_facility_entry()
        self.active_user_confidence_entry()
        self.solution_file_name = "Stochastic_Coverage_"
        self.activate_run_map()

    def select_stochastic_maximum_coverage(self):
        """
        """
        self.clear_all_inputs()
        self.deactive_user_threshold_entry()
        self.active_user_min_threshold_entry()
        self.active_user_facility_entry()
        self.active_user_confidence_entry()
        self.solution_file_name = "Stochastic_MaxCoverage_"
        self.activate_run_map()
    def load_file(self):
        """
        When the load button is pressed this function is invoked.It is responsible of two things:
            i)  Call the file chooser function
            ii) Load the excel file
        """
        filename = askopenfilename()
        self.user_entry_box.insert(0 , filename)
        self.solution_file_name = self.user_entry_box.get()

    def run_selected_solution(self):
        """
        This function shows given solution , file_name.txt on the map.
        It takes 1 argument :
            i) file_name : A string, which represents name of the txt file that contains the solution
        It returns nothing.
        """
        solution_array = solver.writer.reader.read_selected_solution(self.user_entry_box.get())
        print("Solution array is read")
        name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances = solver.writer.reader.read_district_file()
        map.run(solution_array , name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances , int(self.user_threshold_entry.get()))


    def get_user_entries(self , choice):
        """
        This function get user entries.
        It takes 1 argument:
            i) choice              : An integer , which represents the model choice of the user
        It returns 5 variables:
            i) threshold           : An integer , which represents the max possible distance(m) between two district
            ii) is_stochastis      : A boolean  , which represents whether the chosen model is stochastic or not.
            iii) min_threshold     : An integer , which represents the max possible travel time(min) between two districts
            iv) facility_number    : An integer , which represents possible maximum facilities user allowed to open
            v) confidence_interval : An integer , which represents confidence_interval of stochastic model

        NOTE : For more details about these variable appropriate ranges check out input_check function
        """
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
            threshold = 7000
            confidence_interval = int(self.user_confidence_entry.get())
            if choice == 4 :
                facility_number = 0
            else :
                facility_number = int(self.user_facility_entry.get())

        return threshold , is_stochastis , min_threshold , facility_number , confidence_interval

    def get_appropriate_available_matrix(self,choice , from_districts , to_districts , distances , threshold , random_numbers , min_threshold , confidence_interval):
        """
        This function creates appropriate availability_matrix according to user's choice.
        It takes 1 argument :
            i) choice              : An integer     , which represents user's model choice
        It returns 1 argument :
            i) availability_matrix : A list of list , which consists of binary values that represents whether a particular district covers another particular district or not
        """
        if choice == 1 or choice == 2 or choice == 3 :
            availability_matrix = solver.writer.reader.util.generate_availability_matrix(from_districts , to_districts , distances , threshold)
            print("Availability_Matrix is created")

        elif choice == 4 or choice == 5:
            random_numbers = solver.writer.reader.read_generated_numbers()
            availability_matrix = solver.writer.reader.util.generate_stochastic_availability_matrix(from_districts , to_districts , random_numbers , min_threshold , distances , confidence_interval)
            print("Stochastic matrix is created")

        return availability_matrix

    def write_appropriate_dat_file(self , choice , availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval , risk_indicator , risk_array , min_threshold):
        """
        This function writes appropriate_dat file according to user's choice.
        It takes 1 argument :
            i) choice : An integer , which represents user's model choice
        It returns nothing.
        """
        if choice == 1:
            solver.writer.write_dat(availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
        elif choice == 2:
            solver.writer.write_multi_dat(availability_matrix , risk_indicator , risk_array ,  fixed_cost , threshold)
            print(".dat file is created")
        elif choice == 3 :
            solver.writer.write_dat(availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
        elif choice == 4 :
            solver.writer.write_dat(availability_matrix , fixed_cost , min_threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")
        elif choice == 5:
            solver.writer.write_dat(availability_matrix , fixed_cost , min_threshold , facility_number , is_stochastis , confidence_interval)
            print(".dat file is created")

    def generate_solution_filename(self , choice , threshold , is_stochastis , min_threshold , facility_number , confidence_interval):
        """
        This function generate appropriate solution file_name and returns it.
        It takes 6 arguments:
            i)  choice              : An integer , which represents user's model choice
            ii) threshold           : An integer , which represents the max possible distance(m) between two district
            iii) is_stochastis      : A boolean  , which represents whether the chosen model is stochastic or not.
            iv) min_threshold       : An integer , which represents the max possible travel time(min) between two districts
            v) facility_number      : An integer , which represents possible maximum facilities user allowed to open
            vi) confidence_interval : An integer , which represents confidence_interval of stochastic model
        It returns 1 variable:
            i) file_name            : A string   , which represents the name of the file that contains solutions according to user's choice.
        """
        if choice == 1:
            self.map_file_name = self.solution_file_name + "Sol_" + str(threshold) + ".html"
            self.solution_file_name += "Sol_" + str(threshold) + ".txt"
        elif choice == 2:
            self.map_file_name = self.solution_file_name + "Sol_" + str(threshold) + ".html"
            self.solution_file_name += "Sol_" + str(threshold) + ".txt"
        elif choice == 3:
            self.map_file_name = self.solution_file_name + "Sol_" + str(threshold) + "_" + str(facility_number) + ".html"
            self.solution_file_name += "Sol_" + str(threshold) + "_" + str(facility_number) + ".txt"
        elif choice == 4:
            self.map_file_name = self.solution_file_name + "Sol_" + str(min_threshold) + "_" + str(confidence_interval) +  ".html"
            self.solution_file_name += "Sol_" + str(min_threshold) + "_" + str(confidence_interval) +  ".txt"
        elif choice == 5:
            self.map_file_name = self.solution_file_name + "Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) +  ".html"
            self.solution_file_name += "Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) +  ".txt"

    def check_map(self):
        """
        This function checks whether there exists a file_name.txt or not
        It takes no arguments:
        It returns a boolean which represents whether there file_name.txt exists or not
        """
        current_directory = solver.writer.reader.util.get_current_directory()
        full_path = current_directory + "/Maps/" + self.map_file_name

        if os.path.isfile(full_path) == True:
            return True
        else :
            return False

    def threshold_check(self):
        """
        This function checks whether threshold is valid or not.
        It takes no arguments.
        It returns True if threshold is valid , otherwise it returns False.
        """
        threshold = self.user_threshold_entry.get()
        try :
            threshold = int(threshold)
            if threshold < 0 :
                messagebox.showerror("Error", "Please enter a nonnegative value for threshold")
                return False
            return True
        except:
            messagebox.showerror("Error", "Please enter an integer for threshold")
            return False

    def facility_number_check(self):
        """
        This function checks whether facility_number is valid or not.
        It takes no arguments.
        It returns True if facility_number is valid , otherwise it returns False.
        """
        facility_number = self.user_facility_entry.get()
        try :
            facility_number = int(facility_number)
            if facility_number < 0 or facility_number > 867 :
                messagebox.showerror("Error", "Please enter a value in [0,867] for facility_number")
                return False
            return True
        except:
            messagebox.showerror("Error", "Please enter an integer for facility_number")
            return False

    def threshold_min_check(self):
        """
        This function checks whether min_threshold is valid or not.
        It takes no arguments.
        It returns True if min_threshold is valid , otherwise it returns False.
        """
        min_threshold = self.user_min_threshold_entry.get()
        try :
            min_threshold = int(min_threshold)
            if min_threshold < 0 :
                messagebox.showerror("Error", "Please enter a nonnegative value for min_threshold")
                return False
            return True
        except:
            messagebox.showerror("Error", "Please enter an integer for min_threshold")
            return False

    def confidence_interval_check(self):
        """
        This function checks whether confidence_interval is valid or not.
        It takes no arguments.
        It returns True if confidence_interval is valid , otherwise it returns False.
        """
        confidence_interval = self.user_confidence_entry.get()
        try :
            confidence_interval = int(confidence_interval)
            if confidence_interval < 0 or confidence_interval > 100 :
                messagebox.showerror("Error", "Please enter a value in [0,100] interval for confidence_interval")
                return False
            return True
        except:
            messagebox.showerror("Error", "Please enter an integer for confidence_interval")
            return False

    def input_check(self , choice):
        """
        This function makes an input check according to user's choice
        It takes 1 arguments:
            i)  choice : An integer , which represents user's model choice
        It returns a boolean which represents whether inputs are valid or not
        """
        if choice == 1 or choice == 2:
            return self.threshold_check()
        elif choice == 3:
            if self.threshold_check() == True:
                return self.facility_number_check()
            else:
                return False
        elif choice == 4:
            if self.threshold_min_check() == True:
                return self.confidence_interval_check()
            else:
                return False
        elif choice == 5:
            if self.threshold_min_check() == True:
                if self.confidence_interval_check() == True:
                    return self.facility_number_check()
                else:
                    return False
            else:
                return False

    def run_map(self):
        """
        Run the map with given user choices.
        It takes no arguments.
        It returns nothing.
        """
        choice = self.radio_button_var.get()
        #Make an input check before running map
        if self.input_check(choice) == True:
            #Prepare thresholds , facility_number , confidence_interval etc.
            threshold , is_stochastis , min_threshold , facility_number , confidence_interval = self.get_user_entries(choice)

            #Generate file name of the solution file
            self.generate_solution_filename(choice , threshold , is_stochastis , min_threshold , facility_number , confidence_interval)

            if self.check_map() == True:
                map.draw_map(self.map_file_name)
            else:
                #Prepare District data
                name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances = solver.writer.reader.read_district_file()
                risks = solver.writer.reader.read_risk()
                risk_indicator = solver.writer.reader.util.generate_risk_indicator(risks)
                risk_array = solver.writer.reader.util.generate_risk_array()
                random_numbers = solver.writer.reader.read_generated_numbers()
                print("District file is read")

                #Get availability_matrix , it can be stochastic as well
                availability_matrix = self.get_appropriate_available_matrix(choice , from_districts , to_districts , distances , threshold , random_numbers , min_threshold , confidence_interval)

                #Create fixed_cost
                fixed_cost = solver.writer.reader.util.generate_fixed_cost_array()
                print("Fixed_cost is created")

                #Get .dat file
                self.write_appropriate_dat_file(choice , availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval , risk_indicator , risk_array , min_threshold)
                solver.run(choice , threshold , confidence_interval , facility_number , min_threshold)
                solution_array = solver.writer.reader.read_cloud_solution(self.solution_file_name)
                print("Solution array is read")
                count = 0
                for element in solution_array :
                    if element == 1:
                        count += 1
                print(count)
                map.run(solution_array , name_of_districts , x_coordinates , y_coordinates , from_districts , to_districts , distances , threshold , self.map_file_name)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

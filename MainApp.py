# Sumbitted by  : Syed Muhammad Mudasir
# Rollno        : F21BSEEN1E02007
# Semester      : 5th
# Section       : E1
# Project       : Institute Configuration In Tkinter
# Sumbitted To  : Sir Nauman

# To install All The packages just type 

# "pip install -r requirements.txt"  in the terminal of vscode or whichever IDE you are Using



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

class InfoTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_item = None
        self.init_welcome_tab()

    def init_welcome_tab(self):

        # Frame 1
        Label_frame_0 = ttk.LabelFrame(self.parent, text="")
        Label_frame_0.grid(row=0, column=0, padx=30, pady=10, sticky=tk.W)

        self.Lable_1 = ttk.Label(Label_frame_0 ,text="Welcome" , font=("Arial" , 20))
        self.Lable_1.grid(row=0, column=0, padx=30, pady=5 ,sticky=tk.W)

        self.Lable_2 = ttk.Label(Label_frame_0 ,text="To" , font=("Arial" , 15))
        self.Lable_2.grid(row=1, column=0, padx=30, pady=5 ,sticky=tk.W)

        self.Lable_3 = ttk.Label(Label_frame_0 ,text="Institute Configration System" , font=("Arial" , 20))
        self.Lable_3.grid(row=2, column=0, padx=30, pady=5 ,sticky=tk.W)
     
        
        # Frame 2
        Label_frame_1 = ttk.LabelFrame(self.parent, text="")
        Label_frame_1.grid(row=1, column=0, padx=30, pady=10, sticky=tk.W)

        self.Lable_1 = ttk.Label(Label_frame_1 ,text="Discription :-" , font=("Arial" , 13))
        self.Lable_1.grid(row=1, column=0, padx=10, pady=4 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- This appliction is made by using Tkinter ." , font=("Arial" , 10))
        self.Lable_1.grid(row=2, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- It uses a Rest API to store the data to the DataBase ." , font=("Arial" , 10))
        self.Lable_1.grid(row=3, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="  The API is made via using Flask ." , font=("Arial" , 10))
        self.Lable_1.grid(row=4, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- It uses the MONGO-DB as a DataBase to store all the data of this application." , font=("Arial" , 10))
        self.Lable_1.grid(row=5, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- There are 3 major components of this Configration System :" , font=("Arial" , 10))
        self.Lable_1.grid(row=6, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="    .. Campus" , font=("Arial" , 10))
        self.Lable_1.grid(row=7, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="    .. Faculty" , font=("Arial" , 10))
        self.Lable_1.grid(row=8, column=0, padx=15 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="    .. Department" , font=("Arial" , 10))
        self.Lable_1.grid(row=9, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- Each component have ability perform the CRUD operations like ;" , font=("Arial" , 10))
        self.Lable_1.grid(row=10, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="     Creating or Adding the data, Showing the Data , Updating the existing Data and Deleting the exsisting data." , font=("Arial" , 10))
        self.Lable_1.grid(row=11, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="- [Important to Know] :" , font=("Arial" , 10))
        self.Lable_1.grid(row=12, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="    Make sure to run the API seperately (In the seperate console or run it seperately) other-wise you may run into problems." , font=("Arial" , 10))
        self.Lable_1.grid(row=13, column=0, padx=15, pady=1 ,sticky=tk.W)
        self.Lable_1 = ttk.Label(Label_frame_1 ,text="    You can Update and Delete the data via clicking on the Rows of Preview Window." , font=("Arial" , 10))
        self.Lable_1.grid(row=14, column=0, padx=15, pady=1 ,sticky=tk.W)


        # Frame 3
        Label_frame_2 = ttk.LabelFrame(self.parent, text="")
        Label_frame_2.grid(row=2, column=0, padx=30, pady=10, sticky=tk.W)

        self.Lable_1 = ttk.Label(Label_frame_2 ,text="Made by Syed Muhammad Mudasir (F21BSEEN1E02007) ." , font=("Arial" , 10))
        self.Lable_1.grid(row=1, column=0, padx=10, pady=10 ,sticky=tk.W)       

class CampusTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_item = None
        self.init_campus_tab()

    def init_campus_tab(self):
        campus_frame = ttk.LabelFrame(self.parent, text="Campus Information")
        campus_frame.grid(row=0, column=0, padx=30, pady=10, sticky=tk.W)

        # Lables and Entries
        campus_id_label = ttk.Label(campus_frame, text="Campus ID :")
        campus_id_label.grid(row=0, column=1 , padx=15 , sticky=tk.W)
        self.campus_id_entry = ttk.Entry(campus_frame)
        self.campus_id_entry.grid(row=0, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        campus_name_label = ttk.Label(campus_frame, text="Campus Name :")
        campus_name_label.grid(row=1, column=1, padx=15 , sticky=tk.W)
        self.campus_name_entry = ttk.Entry(campus_frame)
        self.campus_name_entry.grid(row=1, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        contact_info_label = ttk.Label(campus_frame, text="Contact Info :-")
        contact_info_label.grid(row=3, column=1, padx=15 , pady=10 , sticky=tk.W)

        telephone_label = ttk.Label(campus_frame, text="Telephone Number :")
        telephone_label.grid(row=4, column=1, padx=25 ,sticky=tk.W)
        self.telephone_entry = ttk.Entry(campus_frame)
        self.telephone_entry.grid(row=4, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        email_label = ttk.Label(campus_frame, text="Email :")
        email_label.grid(row=5, column=1 ,padx=25 , sticky=tk.W)
        self.email_entry = ttk.Entry(campus_frame)
        self.email_entry.grid(row=5, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        address_label = ttk.Label(campus_frame, text="Address :")
        address_label.grid(row=6, column=1 ,padx=25 , sticky=tk.W)
        self.address_entry = ttk.Entry(campus_frame)
        self.address_entry.grid(row=6, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        departments_label = ttk.Label(campus_frame, text="List of Departments :")
        departments_label.grid(row=7, column=1 , padx=15 ,  sticky=tk.W)
        self.departments_text = tk.Text(campus_frame, height=4, width=30)
        self.departments_text.grid(row=7, column=2, padx=20 , pady=5 , sticky=tk.W+tk.E)

        # Buttons
        self.add_button = ttk.Button(campus_frame, text="Add Campus", command=self.add_campus)
        self.add_button.grid(row=8, column=1, pady=10)

        self.update_button = ttk.Button(campus_frame, text="Update Campus", state=tk.DISABLED, command=self.update_campus)
        self.update_button.grid(row=8, column=2, pady=10)

        self.show_data_button = ttk.Button(campus_frame, text="Show Data", command=self.show_campus_data)
        self.show_data_button.grid(row=9, column=1, pady=10)

        self.delete_button = ttk.Button(campus_frame, text="Delete Campus", state=tk.DISABLED, command=self.delete_campus)
        self.delete_button.grid(row=9, column=2, pady=10)

        self.clear_button = ttk.Button(campus_frame, text="Clear Entries" , command=self.clear_entries)
        self.clear_button.grid(row=10, column=1, pady=10)

        seprator = ttk.Label(self.parent , text="_______________________________________________________________________________________________________")
        seprator.grid(row=1, column=0 , padx=20, pady=5, sticky=tk.W)

        # Treeview for displaying data
        Show_Data_Label = ttk.Label(self.parent , text="Data Preview Area :" , font=("Arial" , 10))
        Show_Data_Label.grid(row=2, column=0 , padx=20, pady=5, sticky=tk.W)

        self.tree = ttk.Treeview(self.parent, columns=("Campus ID", "Campus Name", "Telephone", "Email", "Address", "Departments"), show="headings")
        self.tree.heading("Campus ID", text="Campus ID")
        self.tree.heading("Campus Name", text="Campus Name")
        self.tree.heading("Telephone", text="Telephone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Departments", text="Departments")
        self.tree.grid(row=3, column=0, rowspan=8, padx=20, pady=10, sticky=tk.W)



        # Bind the treeview's selection event to a callback method
        self.tree.bind("<ButtonRelease-1>", lambda event: self.display_selected_data())

    def add_campus(self):
        campus_id = self.campus_id_entry.get()
        campus_name = self.campus_name_entry.get()
        telephone = self.telephone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        departments = self.departments_text.get("1.0", tk.END)

        if not campus_id or not campus_name or not telephone or not email or not address:
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return

        # Construct the campus data as a dictionary
        campus_data = {
            "campus_id": campus_id,
            "campus_name": campus_name,
            "telephone": telephone,
            "email": email,
            "address": address,
            "departments": departments
        }

        # API endpoint for adding campus data
        api_endpoint = "http://localhost:5000/campus"

        try:
            response = requests.post(api_endpoint, json=campus_data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Campus added successfully.")
                # Update the treeview with the new data
                self.show_campus_data()
                # Clear the entries
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Failed to add campus: {response.text}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to add campus: {e}")

    def show_campus_data(self):
        # API endpoint for retrieving campus data
        api_endpoint = "http://localhost:5000/campus"

        try:
            response = requests.get(api_endpoint)
            data = response.json()

            # Clear existing data in the treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Display actual data retrieved from the API
            for row in data:
                self.tree.insert("", tk.END, values=(row["campus_id"], row["campus_name"], row["telephone"], row["email"],row["address"], row["departments"]))

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch campus data: {e}")

    def display_selected_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_data = self.tree.item(selected_item, "values")
            if selected_data and len(selected_data) == 6:
                # Enable update and delete buttons
                self.update_button["state"] = tk.NORMAL
                self.delete_button["state"] = tk.NORMAL

                # Populate entry fields with selected data
                self.campus_id_entry.delete(0, tk.END)
                self.campus_id_entry.insert(0, selected_data[0])

                self.campus_name_entry.delete(0, tk.END)
                self.campus_name_entry.insert(0, selected_data[1])

                self.telephone_entry.delete(0, tk.END)
                self.telephone_entry.insert(0, selected_data[2])

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, selected_data[3])

                self.address_entry.delete(0, tk.END)
                self.address_entry.insert(0, selected_data[4])

                # Update the Text widget with the selected departments
                self.departments_text.delete("1.0", tk.END)
                self.departments_text.insert("1.0", selected_data[5])
            else:
                messagebox.showerror("Error", "Selected data does not have the expected format.")
        else:
            messagebox.showinfo("Update", "Please select a row to update.")

    def update_campus(self):
        
        selected_item = self.tree.selection()
        if selected_item:
            campus_id = self.campus_id_entry.get()
            campus_name = self.campus_name_entry.get()
            telephone = self.telephone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            departments = self.departments_text.get("1.0", tk.END)

            
            if not campus_id or not campus_name or not telephone or not email or not address:
                messagebox.showerror("Error", "Please fill in all the required fields.")
                return

            # Construct the updated campus data as a dictionary
            updated_campus_data = {
                "campus_id": campus_id,
                "campus_name": campus_name,
                "telephone": telephone,
                "email": email,
                "address": address,
                "departments": departments
            }

            # API endpoint for updating campus data
            update_api_endpoint = f"http://localhost:5000/campus/{campus_id}"

            try:
                response = requests.put(update_api_endpoint, json=updated_campus_data)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Campus updated successfully.")
                    # Disable update and delete buttons after successful update
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                    # Clear the selected_item attribute
                    self.selected_item = None
                    # Clear the entries
                    self.clear_entries()
                    # Update the treeview with the new data
                    self.show_campus_data()
                else:
                    messagebox.showerror("Error", f"Failed to update campus: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to update campus: {e}")
        else:
            messagebox.showinfo("Update", "Please select a row to update.")

    def delete_campus(self):
        
        selected_item = self.tree.selection()
        if selected_item:
            campus_id = self.campus_id_entry.get()

            # API endpoint for deleting campus data
            delete_api_endpoint = f"http://localhost:5000/campus/{campus_id}"

            try:
                # Send DELETE request to delete the campus data
                response = requests.delete(delete_api_endpoint)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Campus deleted successfully.")
                    # Delete the selected row from the treeview
                    self.tree.delete(selected_item)
                    # Disable update and delete buttons after deletion
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                    # Enable add button again
                    self.add_button["state"] = tk.NORMAL
                else:
                    messagebox.showerror("Error", f"Failed to delete campus: {response.text}")

            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to delete campus: {e}")
        else:
            messagebox.showinfo("Delete", "Please select a row to delete.")

    def clear_entries(self):
        self.campus_id_entry.delete(0, tk.END)
        self.campus_name_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.departments_text.delete("1.0", tk.END)

class FacultyTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_item = None
        self.init_faculty_tab()

    def init_faculty_tab(self):
        faculty_frame = ttk.LabelFrame(self.parent, text="Faculty Information")
        faculty_frame.grid(row=0, column=0, padx=30, pady=10 , sticky=tk.W)

        # Labels and Entries
        ttk.Label(faculty_frame, text="Faculty ID :").grid(row=0, column=0, padx=15 ,sticky=tk.W)
        self.faculty_id = ttk.Entry(faculty_frame)
        self.faculty_id.grid(row=0, column=1 , padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Faculty Name :").grid(row=1, column=0,padx=15 , sticky=tk.W)
        self.faculty_name = ttk.Entry(faculty_frame)
        self.faculty_name.grid(row=1, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Faculty Dean :").grid(row=2, column=0, padx=15 ,sticky=tk.W)
        self.faculty_dean = ttk.Entry(faculty_frame)
        self.faculty_dean.grid(row=2, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        contact_info_label = ttk.Label(faculty_frame, text="Contact Info :-")
        contact_info_label.grid(row=3, column=0, padx=15 , pady=10 , sticky=tk.W)

        ttk.Label(faculty_frame, text="Telephone Number :").grid(row=4, column=0, padx=25 ,sticky=tk.W)
        self.phone = ttk.Entry(faculty_frame)
        self.phone.grid(row=4, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Email :").grid(row=5, column=0,padx=25 , sticky=tk.W)
        self.email = ttk.Entry(faculty_frame)
        self.email.grid(row=5, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Address :").grid(row=6, column=0, padx=25 ,sticky=tk.W)
        self.address = ttk.Entry(faculty_frame)
        self.address.grid(row=6, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Teaching Subjects :").grid(row=7, column=0, padx=15 ,sticky=tk.W)
        self.teaching_subjects_text = tk.Text(faculty_frame, height=4, width=30)
        self.teaching_subjects_text.grid(row=7, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)


        # Buttons
        add_button = ttk.Button(faculty_frame, text="Add Faculty", command=self.add_faculty)
        add_button.grid(row=8, column=0, pady=10)

        update_button = ttk.Button(faculty_frame, text="Update Faculty", state=tk.DISABLED, command=self.update_faculty)
        update_button.grid(row=8, column=1, pady=10)

        show_data_button = ttk.Button(faculty_frame, text="Show Data", command=self.show_faculty_data)
        show_data_button.grid(row=9, column=0, pady=10)

        delete_button = ttk.Button(faculty_frame, text="Delete Faculty", state=tk.DISABLED, command=self.delete_faculty)
        delete_button.grid(row=9, column=1, pady=10)

        self.clear_button = ttk.Button(faculty_frame, text="Clear Entries" , command=self.clear_entries)
        self.clear_button.grid(row=10, column=0, pady=10)

        seprator = ttk.Label(self.parent , text="_______________________________________________________________________________________________________")
        seprator.grid(row=1, column=0 , padx=20, pady=5, sticky=tk.W)

        # Treeview for displaying faculty data
        faculty_show_data_label = ttk.Label(self.parent, text="Faculty Data Preview Area:", font=("Arial", 10))
        faculty_show_data_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

        self.tree = ttk.Treeview(self.parent, columns=("Faculty ID", "Faculty Name", "Faculty Dean", "Telephone", "Email", "Address", "Teaching Subjects"), show="headings")
        self.tree.heading("Faculty ID", text="Faculty ID")
        self.tree.heading("Faculty Name", text="Faculty Name")
        self.tree.heading("Faculty Dean", text="Faculty Dean")
        self.tree.heading("Telephone", text="Telephone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Teaching Subjects", text="Teaching Subjects")
        self.tree.grid(row=3, column=0 , rowspan=8 , padx=20, pady=10, sticky=tk.W)

        # Bind the treeview's selection event to a callback method
        self.tree.bind("<ButtonRelease-1>", lambda event: self.display_selected_data())

        # Save buttons as attributes for easy access
        self.add_button = add_button
        self.show_data_button = show_data_button
        self.update_button = update_button
        self.delete_button = delete_button

    def add_faculty(self):
        faculty_id = self.faculty_id.get()
        faculty_name = self.faculty_name.get()
        faculty_dean = self.faculty_dean.get()
        telephone = self.phone.get()
        email = self.email.get()
        address = self.address.get()
        subjects = self.teaching_subjects_text.get("1.0", tk.END)

        if not faculty_id or not faculty_name or not faculty_dean or not telephone or not email or not address:
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return

        # Construct the faculty data as a dictionary
        faculty_data = {
            "faculty_id": faculty_id,
            "faculty_name": faculty_name,
            "faculty_dean": faculty_dean,
            "telephone": telephone,
            "email": email,
            "address": address,
            "subjects": subjects
        }

        
        api_endpoint = "http://localhost:5000/faculty"

        try:
            response = requests.post(api_endpoint, json=faculty_data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Faculty added successfully.")
               
                self.show_faculty_data()
               
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Failed to add faculty: {response.text}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to add faculty: {e}")

    def show_faculty_data(self):
       
        api_endpoint = "http://localhost:5000/faculty"

        try:
            response = requests.get(api_endpoint)
            data = response.json()

            # Clear existing data in the treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Display actual data retrieved from the API
            for row in data:
                self.tree.insert("", tk.END, values=(
                    row["faculty_id"], row["faculty_name"], row["faculty_dean"],
                    row["telephone"], row["email"], row["address"], row["subjects"]
                ))

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch faculty data: {e}")

    def display_selected_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_data = self.tree.item(selected_item, "values")
            if selected_data and len(selected_data) == 7:
                # Enable update and delete buttons
                self.update_button["state"] = tk.NORMAL
                self.delete_button["state"] = tk.NORMAL

                # Set the selected_item attribute
                self.selected_item = selected_item

                # Populate entry fields with selected data
                self.faculty_id.delete(0, tk.END)
                self.faculty_id.insert(0, selected_data[0])

                self.faculty_name.delete(0, tk.END)
                self.faculty_name.insert(0, selected_data[1])

                self.faculty_dean.delete(0, tk.END)
                self.faculty_dean.insert(0, selected_data[2])

                self.phone.delete(0, tk.END)
                self.phone.insert(0, selected_data[3])

                self.email.delete(0, tk.END)
                self.email.insert(0, selected_data[4])

                self.address.delete(0, tk.END)
                self.address.insert(0, selected_data[5])

                # Update the Text widget with the selected subjects
                self.teaching_subjects_text.delete("1.0", tk.END)
                self.teaching_subjects_text.insert("1.0", selected_data[6])
            else:
                messagebox.showerror("Error", "Selected data does not have the expected format.")
                # Disable update and delete buttons
                self.update_button["state"] = tk.DISABLED
                self.delete_button["state"] = tk.DISABLED
        else:
            # No row selected, disable update and delete buttons
            self.update_button["state"] = tk.DISABLED
            self.delete_button["state"] = tk.DISABLED

    def update_faculty(self):
        selected_item = self.tree.selection()
        if selected_item:
            faculty_id = self.faculty_id.get()
            faculty_name = self.faculty_name.get()
            faculty_dean = self.faculty_dean.get()
            telephone = self.phone.get()
            email = self.email.get()
            address = self.address.get()
            subjects = self.teaching_subjects_text.get("1.0", tk.END)

            
            if not faculty_id or not faculty_name or not faculty_dean or not telephone or not email or not address:
                messagebox.showerror("Error", "Please fill in all the required fields.")
                return

            # Construct the updated faculty data as a dictionary
            updated_faculty_data = {
                "faculty_id": faculty_id,
                "faculty_name": faculty_name,
                "faculty_dean": faculty_dean,
                "telephone": telephone,
                "email": email,
                "address": address,
                "subjects": subjects
            }

            
            update_api_endpoint = f"http://localhost:5000/faculty/{faculty_id}"

            try:
                response = requests.put(update_api_endpoint, json=updated_faculty_data)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Faculty updated successfully.")
                    # Disable update and delete buttons after successful update
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                    # Clear the selected_item attribute
                    self.selected_item = None
                    
                    self.clear_entries()
                    
                    self.show_faculty_data()
                else:
                    messagebox.showerror("Error", f"Failed to update faculty: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to update faculty: {e}")
        else:
            messagebox.showinfo("Update", "Please select a row to update.")

    def delete_faculty(self):
        selected_item = self.tree.selection()
        if selected_item:
            faculty_id = self.faculty_id.get()

            
            delete_api_endpoint = f"http://localhost:5000/faculty/{faculty_id}"

            try:
                # Send DELETE request to delete the faculty data
                response = requests.delete(delete_api_endpoint)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Faculty deleted successfully.")
                    # Delete the selected row from the treeview
                    self.tree.delete(selected_item)
                    # Disable update and delete buttons after deletion
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                else:
                    messagebox.showerror("Error", f"Failed to delete faculty: {response.text}")

            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to delete faculty: {e}")
        else:
            messagebox.showinfo("Delete", "Please select a row to delete.")

    def clear_entries(self):
        self.faculty_id.delete(0, tk.END)
        self.faculty_name.delete(0, tk.END)
        self.faculty_dean.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.teaching_subjects_text.delete("1.0", tk.END)

class DepartmentTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_item = None
        self.init_department_tab()

    def init_department_tab(self):
        
        department_frame = ttk.LabelFrame(self.parent, text="Department Information")
        department_frame.grid(row=0, column=0, padx=30, pady=10 , sticky=tk.W)

        # Labels and Entries

        ttk.Label(department_frame, text="Department ID :").grid(row=0, column=0, padx=15 ,sticky=tk.W)
        self.department_id = ttk.Entry(department_frame)
        self.department_id.grid(row=0, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(department_frame, text="Department Name :").grid(row=1, column=0, padx=15 , sticky=tk.W)
        self.department_name = ttk.Entry(department_frame)
        self.department_name.grid(row=1, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(department_frame, text="Department Head :").grid(row=2, column=0, padx=15 , sticky=tk.W)
        self.department_head = ttk.Entry(department_frame)
        self.department_head.grid(row=2, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        contact_info_label = ttk.Label(department_frame, text="Contact Info :-")
        contact_info_label.grid(row=3, column=0, padx=15 , pady=10 , sticky=tk.W)

        ttk.Label(department_frame, text="Telephone Number :").grid(row=4, column=0 ,padx=25 , sticky=tk.W)
        self.phone = ttk.Entry(department_frame)
        self.phone.grid(row=4, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(department_frame, text="Email :").grid(row=5, column=0 ,padx=25 , sticky=tk.W)
        self.email = ttk.Entry(department_frame)
        self.email.grid(row=5, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(department_frame, text="List of Courses :").grid(row=6, column=0 , padx=15 , sticky=tk.W)
        self.courses_text = tk.Text(department_frame, height=4, width=30)
        self.courses_text.grid(row=6, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)


        # Buttons
        self.add_button = ttk.Button(department_frame, text="Add Department", command=self.add_department)
        self.add_button.grid(row=7, column=0, pady=10)

        self.update_button = ttk.Button(department_frame, text="Update Department", state=tk.DISABLED, command=self.update_department)
        self.update_button.grid(row=7, column=1, pady=10)

        self.show_button = ttk.Button(department_frame, text="Show Data", command=self.show_department_data)
        self.show_button.grid(row=8, column=0, pady=10)

        self.delete_button = ttk.Button(department_frame, text="Delete Department", state=tk.DISABLED, command=self.delete_department)
        self.delete_button.grid(row=8, column=1, pady=10)

        self.clear_button = ttk.Button(department_frame, text="Clear Entries ", command=self.clear_entries)
        self.clear_button.grid(row=9, column=0, pady=10)

        seprator = ttk.Label(self.parent , text="_______________________________________________________________________________________________________")
        seprator.grid(row=1, column=0 , padx=20, pady=5, sticky=tk.W)

        # Treeview for displaying department data
        department_show_data_label = ttk.Label(self.parent, text="Department Data Preview Area:", font=("Arial", 10))
        department_show_data_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

        self.tree = ttk.Treeview(self.parent, columns=("Department ID", "Department Name", "Department Head", "Telephone", "Email", "List of Courses"), show="headings")
        self.tree.heading("Department ID", text="Department ID")
        self.tree.heading("Department Name", text="Department Name")
        self.tree.heading("Department Head", text="Department Head")
        self.tree.heading("Telephone", text="Telephone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("List of Courses", text="List of Courses")
        self.tree.grid(row=3, column=0 , rowspan=8 , padx=20, pady=10, sticky=tk.W)

        # Bind the treeview's selection event to a callback method
        self.tree.bind("<ButtonRelease-1>", lambda event: self.display_selected_data())

    def add_department(self):
        department_id = self.department_id.get()
        department_name = self.department_name.get()
        department_head = self.department_head.get()
        phone = self.phone.get()
        email = self.email.get()
        courses = self.courses_text.get("1.0", tk.END)


        if not department_id or not department_name or not department_head or not phone or not email:
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return

        # Construct the department data as a dictionary
        department_data = {
            "department_id": department_id,
            "department_name": department_name,
            "department_head": department_head,
            "phone": phone,
            "email": email,
            "courses": courses
        }

 
        api_endpoint = "http://localhost:5000/department/add"

        try:
            response = requests.post(api_endpoint, json=department_data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Department added successfully.")

                self.show_department_data()

                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Failed to add department: {response.text}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to add department: {e}")

    def show_department_data(self):
        
        api_endpoint = "http://localhost:5000/department"

        try:
            response = requests.get(api_endpoint)
            data = response.json()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in data:
                self.tree.insert("", tk.END, values=(
                    row["department_id"], row["department_name"], row["department_head"], row["phone"], row["email"], row["courses"]
                ))

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch department data: {e}")

    def display_selected_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_data = self.tree.item(selected_item, "values")
            if selected_data and len(selected_data) == 6:
                # Enable update and delete buttons
                self.update_button["state"] = tk.NORMAL
                self.delete_button["state"] = tk.NORMAL
    
                # Set the selected_item attribute
                self.selected_item = selected_item
    
                self.department_id.delete(0, tk.END)
                self.department_id.insert(0, selected_data[0])
    
                self.department_name.delete(0, tk.END)
                self.department_name.insert(0, selected_data[1])

                self.department_head.delete(0, tk.END)
                self.department_head.insert(0, selected_data[2])
    
                self.phone.delete(0, tk.END)
                self.phone.insert(0, selected_data[3])
    
                self.email.delete(0, tk.END)
                self.email.insert(0, selected_data[4])
    
                # Update the Text widget with the selected courses
                self.courses_text.delete("1.0", tk.END)
                self.courses_text.insert("1.0", selected_data[5])
            else:
                messagebox.showerror("Error", "Selected data does not have the expected format.")
        else:
            # No row selected, disable update and delete buttons
            self.update_button["state"] = tk.DISABLED
            self.delete_button["state"] = tk.DISABLED

    def update_department(self):
        selected_item = self.tree.selection()
        if selected_item:
            department_id = self.department_id.get()
            department_name = self.department_name.get()
            department_head = self.department_head.get()
            phone = self.phone.get()
            email = self.email.get()
            courses = self.courses_text.get("1.0", tk.END)

            
            if not department_id or not department_name or not department_head or not phone or not email:
                messagebox.showerror("Error", "Please fill in all the required fields.")
                return

            # Construct the updated department data as a dictionary
            updated_department_data = {
                "department_id": department_id,
                "department_name": department_name,
                "department_head": department_head,
                "phone": phone,
                "email": email,
                "courses": courses
            }

            
            api_endpoint = f"http://localhost:5000/department/{department_id}"

            try:
                response = requests.put(api_endpoint, json=updated_department_data)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Department updated successfully.")

                    self.show_department_data()

                    self.clear_entries()
                else:
                    messagebox.showerror("Error", f"Failed to update department: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to update department: {e}")
        else:
            messagebox.showinfo("Update", "Please select a row to update.")

    def delete_department(self):
        selected_item = self.tree.selection()
        if selected_item:
            department_id = self.department_id.get()

            
            api_endpoint = f"http://localhost:5000/department/{department_id}"

            try:
                response = requests.delete(api_endpoint)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Department deleted successfully.")
                    
                    self.show_department_data()
                   
                    self.clear_entries()
                else:
                    messagebox.showerror("Error", f"Failed to delete department: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to delete department: {e}")
        else:
            messagebox.showinfo("Delete", "Please select a row to delete.")

    def clear_entries(self):
        self.department_id.delete(0, tk.END)
        self.department_name.delete(0, tk.END)
        self.department_head.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.courses_text.delete("1.0", tk.END)


class InstituteConfigurationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Institute Configuration")
        self.notebook = ttk.Notebook(self.root)
        
        self.info_tab = ttk.Frame(self.notebook)
        self.campus_tab = ttk.Frame(self.notebook)
        self.faculty_tab = ttk.Frame(self.notebook)
        self.department_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.info_tab, text="Info")
        self.notebook.add(self.campus_tab, text="Campus")
        self.notebook.add(self.faculty_tab, text="Faculty")
        self.notebook.add(self.department_tab, text="Department")

        self.notebook.pack(expand=1, fill="both")

        # Initialize components
        self.campus_component = InfoTab(self.info_tab)
        self.campus_component = CampusTab(self.campus_tab)
        self.faculty_component = FacultyTab(self.faculty_tab)
        self.department_component = DepartmentTab(self.department_tab)


        # Center the window on the screen
        self.center_window()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 1450
        window_height = 800

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstituteConfigurationApp(root)
    root.mainloop()

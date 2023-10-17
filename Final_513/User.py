import tkinter as tk
from tkinter import ttk
import pandas as pd
import plots
from tkinter import messagebox
import json
import os
import numpy as np

#setting the accountfile.json as accountfile
accountfile = "accountfile.json"

#create a class
class CrimeApp(tk.Tk):
    #create a login frame
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("500x700")

        self.selected_graph = tk.StringVar()
        self.crime_types_var = []
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()

        # Load data from data.py
        from data import df
        self.user_credentials = {}
        self.df = df

        self.label_username = ttk.Label(self, text="Username:")
        self.label_password = ttk.Label(self, text="Password:")
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self)
        self.button_login = ttk.Button(self, text="Login", command=self.login)
        self.button_create_account = ttk.Button(self, text="Create Account", command=self.show_create_account)
        self.label_username.pack(pady=5)
        self.entry_username.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_login.pack(pady=5)
        self.button_create_account.pack(pady=5)

        self.data_text = tk.Text(self, wrap=tk.WORD, height=10)
        self.data_text.pack(pady=10, expand=True, fill='both')
        self.data_text.pack_forget()  
        
        self.load_account()
        self.protocol("WM_DELETE_WINDOW", self.exitApp)
    
    #create to read the account         
    def load_account(self):
            with open(accountfile, "r") as file:
                self.user_credentials = json.load(file)
    
    #create to save the account  
    def save_accounts(self):
        with open(accountfile, "w") as file:
            json.dump(self.user_credentials, file)

    #to show create account
    def show_create_account(self):
        self.label_username.destroy()
        self.label_password.destroy()
        self.entry_username.destroy()
        self.entry_password.destroy()
        self.button_login.destroy()
        self.button_create_account.destroy()

        self.create_account_widgets()

    # Create the create account widgets
    def create_account_widgets(self):
        self.label_new_username = ttk.Label(self, text="username:")
        self.label_new_password = ttk.Label(self, text="password:")
        self.entry_new_username = ttk.Entry(self)
        self.entry_new_password = ttk.Entry(self)
        self.button_create = ttk.Button(self, text="Create Account", command=self.create_account_action)

        # Place create account widgets
        self.label_new_username.pack()
        self.entry_new_username.pack(pady=5)
        self.label_new_password.pack(pady=5)
        self.entry_new_password.pack(pady=5)
        self.button_create.pack()
    
    #create account action
    def create_account_action(self):
        new_username = self.entry_new_username.get()
        new_password = self.entry_new_password.get()

        if not new_username or not new_password:
            messagebox.showerror("Failed", "Please enter username and password.")
            return

        if new_username and new_password:
            self.user_credentials[new_username] = new_password
            messagebox.showinfo("Account Created", "Account created successfully")
            self.create_login_widgets()

    #create login widgets
    def create_login_widgets(self):
        self.label_new_username.destroy()
        self.label_new_password.destroy()
        self.entry_new_username.destroy()
        self.entry_new_password.destroy()
        self.button_create.destroy()

        # Recreate the login widgets
        self.label_username = ttk.Label(self, text="Username:")
        self.label_password = ttk.Label(self, text="Password:")
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self)
        self.button_login = ttk.Button(self, text="Login", command=self.login)
        self.button_create_account = ttk.Button(self, text="Create Account", command=self.show_create_account)
        self.label_username.pack(pady=5)
        self.entry_username.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_login.pack(pady=5)
        self.button_create_account.pack(pady=5)

    #login page
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.user_credentials and self.user_credentials[username] == password:
            self.label_username.destroy()
            self.label_password.destroy()
            self.entry_username.destroy()
            self.entry_password.destroy()
            self.button_login.destroy()
            self.button_create_account.destroy()

            self.create_widgets()
        else:
            tk.messagebox.showerror("Login Failed", "Invalid username or password")

    #exit page
    def exitApp(self):
        if messagebox.askokcancel(title="Exit", message="Are you sure you want to exit?"):
            self.destroy()

    #crate the widgets page
    def create_widgets(self):
        # Create options for filtering data
        crime_types = self.df['primary_type'].unique()
        ttk.Label(self, text="Insert Start Date:").pack(pady=5)
        ttk.Entry(self, textvariable=self.start_date_var).pack()
        ttk.Label(self, text="Insert End Date:").pack(pady=5)
        ttk.Entry(self, textvariable=self.end_date_var).pack()

        ttk.Label(self, text="Crime Types").pack(pady=5)
        for crime_type in crime_types:
            var = tk.BooleanVar()
            ttk.Checkbutton(self, text=crime_type, variable=var, onvalue=True, offvalue=False).pack()
            self.crime_types_var.append((crime_type, var))

        graph_label = ttk.Label(self, text="Select Chart")
        graph_label.pack()

        graph_choices = ['Bar Chart', 'Line Chart', 'Violin Plot', 'Bar Chart by hour of Day',
                         'Locations for Crime Types']
        graph_dropdown = ttk.Combobox(self, textvariable=self.selected_graph, values=graph_choices)
        graph_dropdown.pack()

        plot_button = ttk.Button(self, text='show Graph', command=self.plot_selected_graph)
        plot_button.pack(pady=10)

    # setting the outcome of the graph
    def plot_selected_graph(self):
        selected_graph = self.selected_graph.get()
        selected_crime_types = [crime_type for crime_type, var in self.crime_types_var if var.get()]
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()

        filtered_df = self.df.copy()
        if selected_crime_types:
            filtered_df = filtered_df[filtered_df['primary_type'].isin(selected_crime_types)]

        if start_date and end_date:
            try:
                filtered_df['date'] = pd.to_datetime(filtered_df['date'])
                filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]
            except pd.errors.ParserError:
                tk.messagebox.showerror("Invalid Date Format", "Please enter dates in YYYY-MM-DD format")

        # Calculate crime_count and add it to filtered_df
        filtered_df['crime_count'] = filtered_df['primary_type'].groupby(filtered_df['date']).transform('count')
        
        self.show_data(filtered_df)

        if selected_graph == 'Bar Chart':
            plots.Crime_Type_by_Month(filtered_df)
        
        elif selected_graph == 'Line Chart':
            plots.plot_crime_trend(filtered_df)

        elif selected_graph == 'Bar Chart by hour of Day':
            plots.plot_crime_by_time(filtered_df)

        elif selected_graph == 'Locations for Crime Types':
            plots.plot_top_locations(filtered_df)

        elif selected_graph == 'Violin Plot':
            plots.plot_violin_plot(filtered_df)

    #create the outcome of the informataion, Calculation, and statistic
    def show_data(self, df):
        self.data_text.delete(1.0, tk.END)
        data_str = df.head().to_string(index=False)
        self.data_text.insert(tk.END, data_str)
        self.data_text.insert(tk.END, "\n\nStatistical Outcomes:\n")

        numerical_columns = df.select_dtypes(include='number')

        self.data_text.insert(tk.END, f"Means:{numerical_columns.mean()}\n")
        self.data_text.insert(tk.END, f"Standard Deviations:{numerical_columns.std()}\n")
        self.data_text.insert(tk.END, f"Variances:{numerical_columns.var()}\n")

        self.data_text.insert(tk.END, f"Counts:{df.count()}\n\n")
        self.data_text.insert(tk.END, f"Averages:{df.mean(axis=0)}\n")
        self.data_text.insert(tk.END, f"Correlations:{df.corr()}\n")

        self.data_text.pack(pady=10, expand=True, fill='both')

if __name__ == "__main__":
    app = CrimeApp()
    app.mainloop()

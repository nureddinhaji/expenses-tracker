import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

# To import tkcalendar we must beofre instal it with "pip install tkcalendar"
from tkcalendar import *

# Variables for total amount row
total_amount = 0
added_currencies = {}

# Create the app window frame
window = tk.Tk()
window.title("Expenses Tracker")
window.minsize(1000,700)
window.columnconfigure(0,weight=1)
window.rowconfigure(1,weight=1)

#Inputs Frame
inputs_frame = tk.Frame(window)
inputs_frame.grid(row=0, column=0, sticky="NSEW",pady=10)
inputs_frame.columnconfigure(0, weight=1)

#Results Frame
results_frame = tk.Frame(window)
results_frame.grid(row=1, column=0, sticky="NSEW")
results_frame.rowconfigure(0, weight=1)
results_frame.columnconfigure(0, weight=1)

#=========================
# Get currencies symbols from API
#=========================
# Api URL and Headers
url_symbols = "https://api.apilayer.com/fixer/symbols"
headers= {"apikey": "2jAnAahYHdQz3n773JCvcmhYVoRwvuuT"}

#Get all recurrencies symbols
response = requests.get(url_symbols, headers=headers)
result = response.json()
currencies = list(result["symbols"].keys())

#=========================
# Create inputs to the APP
#=========================
items_list = ["Amount", "Currency", "Category", "Payment Method", "Date"]
global amount_entry

for index, item in enumerate(items_list):
    frame = tk.Frame(inputs_frame)
    frame.grid(row=[index + 1], column=0, sticky="NSEW",pady=3)
    label = tk.Label(frame, text = item)
    label.grid(row = 0, column=0, sticky="NSEW")
    if item == "Amount":
        amount_entry = tk.Entry(frame, width="50")
        amount_entry.grid(row = 0, column=1)
    elif item == "Currency":
        currency_entry = ttk.Combobox(frame, state="readonly", width="47", values= currencies)
        currency_entry.grid(row = 0, column=1)
    elif item == "Category":
        category_entry = ttk.Combobox(frame, state="readonly", width="47", values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Charity"])
        category_entry.grid(row = 0, column=1)
    elif item == "Payment Method":
        payment_entry = ttk.Combobox(frame, state="readonly", width="47", values=["Cash", "Debit Card", "Paypal"])
        payment_entry.grid(row = 0, column=1)
    elif item == "Date":
        date_entry = tk.Entry(frame, width="50")
        date_entry.insert(0, "yyyy-mm-dd")
        date_entry.grid(row = 0, column=1)
    frame.columnconfigure(0, minsize=200)

# Function to get the selected date and add it to date entry and coles date picker
def get_selected_date(event):
    date_entry.delete(0, tk.END)
    date_entry.insert(0, calendar.get_date())
    calendar_frame.destroy()

# Function to open date picker
def get_date(evnt):
    global calendar_frame, calendar,submit_btn
    calendar_frame = tk.Tk()
    calendar_frame.title("Select Date")
    calendar = Calendar(calendar_frame,showweeknumbers = False, date_pattern = 'yyyy-mm-dd', showothermonthdays = False)
    calendar.grid(row=0,pady=10)

    submit_btn = tk.Button(calendar_frame, text="Submit Date", width=9, height=1, bg="blue", fg="yellow",)
    submit_btn.grid(row=1, sticky="NSEW")

    submit_btn.bind("<Button-1>", get_selected_date)

date_entry.bind("<Button-1>", get_date)

#=========================
# Add expense button
#=========================
# Add add_button frame
add_button_frame = tk.Frame(inputs_frame)
add_button_frame.grid(row=6, column=0, sticky="NSEW",pady=3)
# Add add_button label
add_button_label = tk.Label(add_button_frame, text = "")
add_button_label.grid(row = 0, column=0, sticky="NSEW")
# Add add_button entry
add_button_button = tk.Button(add_button_frame, text="Add An Expense", bg="blue", fg="yellow")
add_button_button.grid(row = 0, column=1)
# Make it to get all space
add_button_frame.columnconfigure(0, minsize=200)

#=========================
# Add the expenses table
#=========================
table_columns = ["amount", "currency", "category", "payment", "date"]
table = ttk.Treeview(results_frame, column=(table_columns), show='headings', height=5)
for column in table_columns:
    table.column(column, anchor="center")
    table.heading(column, text= column.capitalize())

# Add the expenses table to main window
table.grid(row=0, sticky="NSEW")

# Add a tag with special background color for total amount
table.tag_configure('TA', background='yellow')

# Function to add expenses to the table
def add_inputs(event):
    # Get all user inputs
    amount = amount_entry.get()
    currency = currency_entry.get()
    category = category_entry.get()
    payment = payment_entry.get()
    date = date_entry.get()
    
    # Get variables from global scope
    global total_amount, added_currencies

    #Check if user added all infos
    if(amount and currency and category and payment and date):
        
        # Check if total amount table has been added before, if it delete it
        if(table.exists("total_amount")):
            table.delete("total_amount")
        
        # Add the new expense row to the table
        table.insert('', tk.END, values=(amount, currency, category, payment, date))

        # Check if the new expense currency has been added before to added_currencies tuple
        # if it has ben added before use it to convert the amount to USD
        # if not convert it with API and add it to added_currencies tuple
        if currency not in added_currencies.keys():
            conv_url = f"https://api.apilayer.com/fixer/latest?symbols={currency}&base=USD"
            response = requests.get(conv_url, headers=headers)
            result = response.json()
            added_currencies[currency] = result["rates"][currency]

        # Add the new expense amount to the total_amount
        total_amount += float(amount) / added_currencies[currency]

        # Add the total amount row to the expenses table
        table.insert('', tk.END, values=('{:.2f}'.format(total_amount), "USD"), iid="total_amount", tags=("TA"))
    else:
        messagebox.showerror(message="Please fill all inputs.", title="Error")

# Bind add_button to add_inputs function
add_button_button.bind("<Button-1>", add_inputs)



# Run The Window
window.mainloop()
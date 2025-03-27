import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # For Combobox

def select_files():
    """Opens a file selection dialog and updates the file selection field."""
    file_paths = filedialog.askopenfiles()  # Allows multiple file selection
    global selected_files
    selected_files = [file.name for file in file_paths]  # Store file paths
    file_selection_label.config(text=", ".join(selected_files))  # Update label

def select_google_sheet():
    """Opens a file selection dialog for the Google Sheet and updates the sheet selection field."""
    file_path = filedialog.askopenfilename(filetypes=[("Google Sheets", "*.xlsx;*.csv")])  # Adjust file types as needed
    global selected_sheet_file
    selected_sheet_file = file_path
    sheet_selection_label.config(text=selected_sheet_file)

def extract_data():
    """
    This function will contain the logic to extract data from the selected files
    and load it into the selected Google Sheet.  For now, it's a placeholder.
    """
    if selected_files and selected_sheet_file and selected_sheet_tab.get():
        print("Extracting data from:", selected_files)
        print("To Google Sheet:", selected_sheet_file)
        print("To Tab:", selected_sheet_tab.get())
        #
        #  Add your data extraction and Google Sheets loading logic here
        #
        print("Data extraction and loading process started...")  # Placeholder message
    else:
        print("Please select files, a Google Sheet, and a tab.")

# Initialize Tkinter window
window = tk.Tk()
window.title("Data Extraction Tool")
window.geometry("600x400")  # Initial window size
window.resizable(True, True)  # Make the window resizable

# --- File Selection ---
file_selection_frame = tk.Frame(window)
file_selection_frame.pack(pady=10)

file_selection_button = tk.Button(file_selection_frame, text="Select Files", command=select_files)
file_selection_button.pack(side=tk.LEFT, padx=10)

file_selection_label = tk.Label(file_selection_frame, text="No files selected", width=40, wraplength=300)
file_selection_label.pack(side=tk.LEFT)

# --- Google Sheet Selection ---
sheet_selection_frame = tk.Frame(window)
sheet_selection_frame.pack(pady=10)

sheet_selection_button = tk.Button(sheet_selection_frame, text="Select Google Sheet", command=select_google_sheet)
sheet_selection_button.pack(side=tk.LEFT, padx=10)

sheet_selection_label = tk.Label(sheet_selection_frame, text="No sheet selected", width=40, wraplength=300)
sheet_selection_label.pack(side=tk.LEFT)

# --- Google Sheet Tab Selection ---
sheet_tab_frame = tk.Frame(window)
sheet_tab_frame.pack(pady=10)

sheet_tab_label = tk.Label(sheet_tab_frame, text="Select Tab:")
sheet_tab_label.pack(side=tk.LEFT, padx=10)

#  Use a Combobox for tab selection (you'll need to populate it dynamically
#  if you want it to reflect actual tabs in a sheet after selection)
selected_sheet_tab = ttk.Combobox(sheet_tab_frame, values=["Sheet1", "Sheet2", "Sheet3"]) # Example tabs
selected_sheet_tab.pack(side=tk.LEFT)
selected_sheet_tab.set("Sheet1")  # Default selection

# --- Extract Button ---
extract_button = tk.Button(window, text="Extract", command=extract_data, bg="green", fg="white", font=("Arial", 12, "bold"))
extract_button.pack(pady=20)

# --- Initialize variables to store selections ---
selected_files = []
selected_sheet_file = ""

# Run the Tkinter event loop
window.mainloop()
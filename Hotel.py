import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    """
    Function to handle form submission.
    """
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    address = entry_address.get()
    phone_number = entry_phone_number.get()
    check_in_date = entry_check_in_date.get()

    if first_name and last_name and address and phone_number and check_in_date:
        messagebox.showinfo("Submission Successful", "แบบฟอร์มถูกส่งเรียบร้อยแล้ว!")
        
        # You can add code here to save the data to a file, database, etc.
        # For example, printing the data to the console:
        print("--- ข้อมูลการเข้าพัก ---")
        print(f"ชื่อลูกค้า: {first_name}")
        print(f"นามสกุล: {last_name}")
        print(f"ที่อยู่: {address}")
        print(f"เบอร์โทร: {phone_number}")
        print(f"วันที่เข้าพัก: {check_in_date}")
        print("--------------------")

        # Clear the input fields after submission
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_phone_number.delete(0, tk.END)
        entry_check_in_date.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "กรุณากรอกข้อมูลให้ครบถ้วน")

# Create the main window
root = tk.Tk()
root.title("แบบฟอร์มเข้าพักโรงแรม")
root.geometry("450x350")
root.resizable(False, False)

# Set a style for better aesthetics
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"))

# Create a frame for the form
form_frame = ttk.Frame(root, padding="20")
form_frame.pack(fill="both", expand=True)

# Create and place widgets
## Row 1: First Name
label_first_name = ttk.Label(form_frame, text="ชื่อลูกค้า:")
label_first_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_first_name = ttk.Entry(form_frame, width=40)
entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

## Row 2: Last Name
label_last_name = ttk.Label(form_frame, text="นามสกุล:")
label_last_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_last_name = ttk.Entry(form_frame, width=40)
entry_last_name.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

## Row 3: Address
label_address = ttk.Label(form_frame, text="ที่อยู่:")
label_address.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_address = ttk.Entry(form_frame, width=40)
entry_address.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

## Row 4: Phone Number
label_phone_number = ttk.Label(form_frame, text="เบอร์โทร:")
label_phone_number.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_phone_number = ttk.Entry(form_frame, width=40)
entry_phone_number.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

## Row 5: Check-in Date
label_check_in_date = ttk.Label(form_frame, text="วันที่เข้าพัก:")
label_check_in_date.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_check_in_date = ttk.Entry(form_frame, width=40)
entry_check_in_date.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

# Submit button
submit_button = ttk.Button(form_frame, text="ส่งแบบฟอร์ม", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

# Configure column to expand
form_frame.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()

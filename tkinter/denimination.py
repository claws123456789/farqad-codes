import tkinter as tk
from tkinter import messagebox
def calculate_denominations():
        amount = int(entry_amount.get())
        if amount <= 0:
            messagebox.showerror("Error", "Please enter a positive amount")
            return
        
        denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        result = ""
        
        for i in denominations:
            count = amount // i
            if count > 0:
                result += f"{i} =  {count}\n"
                amount %= i
        
        label_result.config(text=result)



root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("300x400")

tk.Label(root, text="Enter Amount:", font=("Arial", 12)).pack(pady=10)
entry_amount = tk.Entry(root, font=("Arial", 12))
entry_amount.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_denominations, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()


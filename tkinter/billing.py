import tkinter as tk
def calculate_total():
    total = 0
    for item, var in zip(menu, quantity_vars):
        total += price[item] * int(var.get())
    total_var.set(f"Total: ${total:.2f}")

root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("400x400")

menu = ["Pizza", "Burger", "Pasta", "Salad","rice"]
price = {"Pizza": 100.99, "Burger": 90.49, "Pasta": 70.99, "Salad": 4.99,"rice":40.80}

quantity_vars = []

for i in menu:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    
    tk.Label(frame, text=f"{i} - ${price[i]:.2f}").pack(side=tk.LEFT)
    
    var = tk.StringVar(value="0")
    quantity_vars.append(var)
    
    tk.Entry(frame, textvariable=var, width=5).pack(side=tk.RIGHT)


total_var = tk.StringVar(value="Total: $0.00")
total_label = tk.Label(root, textvariable=total_var, font=("Arial", 12, "bold"))
total_label.pack(pady=10)

# Buttons
tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=5)


root.mainloop()
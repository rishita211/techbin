import tkinter as tk
from tkinter import messagebox

# Reward logic
def calculate_reward():
    name = name_entry.get()
    weight = weight_entry.get()

    try:
        weight = float(weight)
        if weight >= 5:
            reward = "🎁 Big Reward (₹100 Coupon / Gift Card)"
        else:
            reward = "🎉 Small Reward (₹20 Coupon)"
        result_label.config(text=f"{name}, your reward is: {reward}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for weight.")

# GUI setup
root = tk.Tk()
root.title("Tech Bin - Waste Reward System")
root.geometry("400x300")

tk.Label(root, text="👤 Enter Your Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="♻️ Enter Waste Weight (in KG):").pack(pady=5)
weight_entry = tk.Entry(root, width=30)
weight_entry.pack()

tk.Button(root, text="Submit", command=calculate_reward, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()

import tkinter as tk

from excess_energy import calculate_list, export_to_excel

def get_input():
    battery_capacity = entry.get()
    calculate_list(int(battery_capacity))

window = tk.Tk()
window.title("Menu")

entry = tk.Entry(window, width=30)

button = tk.Button(window, text="Get Input", command=get_input)

export_btn = tk.Button(window, text="Export To Excel", command=export_to_excel)

window.geometry("500x500")
entry.pack(pady=10)
button.pack(pady=5)
export_btn.pack(pady=10)

window.mainloop()
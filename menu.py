import tkinter as tk

from excess_energy import calculate_list, export_to_excel

def get_input():
    battery_capacity = entry.get()
    kwh_coefficient = entry_kwh_coefficient.get()
    calculate_list(float(battery_capacity),float(kwh_coefficient))
def export_to_excel_click():
      battery_capacity = entry.get() 
      kwh_coefficient = entry_kwh_coefficient.get()
      export_to_excel(float(kwh_coefficient),float(battery_capacity))

window = tk.Tk()
window.title("Menu")

label = tk.Label(window, text="Battery Capacity")
label.pack()

entry = tk.Entry(window, width=30)
entry_kwh_coefficient = tk.Entry(window,width=30)

button = tk.Button(window, text="Get Input", command=get_input)

export_btn = tk.Button(window, text="Export To Excel", command=export_to_excel_click)

window.geometry("400x250")
entry.pack(pady=15)
entry_kwh_coefficient.pack(pady=20)
button.pack(pady=10)
export_btn.pack(pady=15)

window.mainloop()
import pandas as pd

df = pd.read_excel(r"C:\\Users\\rahid\Documents\\projects\\Excess Energy\\Excess Energy.xlsx", 'Excess')

class Excess_VM:
    def __init__(self,Date,e_Grid_kWh,Consumption):  #,excess_energy,excess_1wh,discharge,charging_of_battery,additional_energy_from_excess_energy
        self.Date = Date
        self.e_Grid_kWh = e_Grid_kWh
        self.Consumption = Consumption
excess_vm_list = []
for index, row in df.iterrows():
    excess_vm_object = Excess_VM(
        Date=row['Date'],
        e_Grid_kWh=row['e_Grid_kWh'],
        Consumption=row['Consumption']
    )
    excess_vm_list.append(excess_vm_object)

print(excess_vm_list[0].Date)


import math
import pandas as pd
from Excess_VM import Excess_VM

df = pd.read_excel(
    r"C:\\Users\\rahid\Documents\\projects\\Excess Energy\\Excess Energy.xlsx", "Excess"
)

excess_vm_list = []
for index, row in df.iterrows():
    excess_vm_object = Excess_VM(
        Date=row["Date"],
        e_Grid_kWh=row["e_Grid_kWh"],
        Consumption=row["Consumption"],
        Excess_Energy_1MW=row["Excess_Energy_1MW"],
        Excess_1MW=row["Excess_1MW"],
        Discharge=row["Discharge"],
        Charging_of_battery=row["Charging_of_battery"],
        Additional_energy=row["Additional_energy"],
    )
    excess_vm_list.append(excess_vm_object)

sum = 0

for x in excess_vm_list:
    if x.e_Grid_kWh > x.Consumption:
        x.Excess_Energy_1MW = x.e_Grid_kWh - x.Consumption
    else:
        x.Excess_Energy_1MW = 0

previous_discharge = 0
first_iteration = True
for x in excess_vm_list:
    if not math.isnan(x.Discharge) and x.Excess_1MW == 0:
        if first_iteration:
            previous_discharge = x.Discharge
            first_iteration = False
            continue
        x.Discharge = previous_discharge - x.Consumption
        previous_discharge = x.Discharge
    else:
        x.Discharge = previous_discharge

print(excess_vm_list[45].Discharge)

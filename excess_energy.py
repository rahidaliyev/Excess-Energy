from datetime import datetime
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
global kwh_coefficient
def calculate_list(battery_capacity,kwh_coefficient):  
    for x in excess_vm_list:
        x.e_Grid_kWh = kwh_coefficient*x.e_Grid_kWh 
        if x.e_Grid_kWh > x.Consumption:
            x.Excess_Energy_1MW = x.e_Grid_kWh - x.Consumption
        else:
            x.Excess_Energy_1MW = 0
    
    previous_discharge = 0
    for x in excess_vm_list:
        if  x.Excess_Energy_1MW == 0 and previous_discharge+x.Excess_1MW>battery_capacity*0.2:
            if previous_discharge - x.Consumption>battery_capacity*0.2:
                x.Discharge = previous_discharge - x.Consumption
                previous_discharge = x.Discharge
            else:
                previous_discharge = battery_capacity * 0.2
        else:
            if previous_discharge + x.Excess_Energy_1MW < battery_capacity * 0.8:
                x.Discharge = previous_discharge + x.Excess_Energy_1MW
                previous_discharge = x.Discharge
            elif previous_discharge+x.Excess_Energy_1MW >= battery_capacity*0.8:
                x.Discharge = battery_capacity*0.8
                previous_discharge = battery_capacity*0.8
            else:
                x.Discharge = previous_discharge


def export_to_excel(kwh_coefficient,battery_capacity):
    excess_vm_df = pd.DataFrame([
        {
            "Date": x.Date,
            "e_Grid_kWh": x.e_Grid_kWh,
            "Consumption": x.Consumption,
            "Excess_Energy_1MW": x.Excess_Energy_1MW,
            "Excess_1MW": x.Excess_1MW,
            "Discharge": x.Discharge,
            "Charging_of_battery": x.Charging_of_battery,
            "Additional_energy": x.Additional_energy,
        }
        for x in excess_vm_list
    ])
    
    output_excel_path = f"C:\\Users\\rahid\\Documents\\projects\\Excess Energy\\Output_Excess_Energy_{kwh_coefficient}-MW_{battery_capacity}-kWh.xlsx"
    
    excess_vm_df.to_excel(output_excel_path, index=False)
    print("Export olundu!!!")
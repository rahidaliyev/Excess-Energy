# dictionary = {"brand": "Ford", "model": "Mustang", "year": "1964"}

# print(len(dictionary["brand"]) + 7)


# textDictionary = {"0": "12", "23": "43", "2": "76"}

# textDictionary.update({"4": "12"})
# print(textDictionary)


# Sorting Dictionary
# sorted_items = sorted(textDictionary.items())
# print(sorted_items)
# print(textDictionary)

# Concat dictionaries

# dict1 = {1: "a", 2: "d"}
# dict2 = {3: "a", 2: "d"}
# dict3 = {4: "45", 5: "c"}
# dict4 = {}

# for d in (dict1,dict2,dict3):
#     dict4.update(d)
# print(dict4)


# Write a Python script to check whether a given key already exists in a dictionary.

# sampleDict = {1: "r", 2: "a", 3: "h", 4: "i", 5: "d", 2: "as"}


# def is_key_present(x):
#     if x in sampleDict:
#         print("Bu achar dictionary-de movcuddur!")
#     else:
#         print("Bu achar dictionary-de deyil!")


# is_key_present(65)


# Write a Python program to iterate over dictionaries using for loops.

# sampleDict = {1: "r", 2: "a", 3: "h", 4: "i", 5: "d", 2: "as"}
# for key, value in sampleDict.items():
#     print(key,'-->',value)


#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# n = int(input("Input a number: "))
# d = dict()

# for x in range(1, n + 1):
#     d[x] = x * x
# print(d)


# Write a Python script to merge two Python dictionaries.
# dist1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# dist2 = {5: 7, 6: 4, 7: 9, 8: 16, 9: 25}

# def Merge(dist1,dist2):
#     return(dist2.update(dist1))

# Merge(dist1,dist2);

# print(sorted(dist2.items()));


# Write a Python program to iterate over dictionaries using for loops.

# dist1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# for key, value in dist1.items():
#     print(key, " ", dist1[key])

# dist1[key] equals to value


# Write a Python program to sum all the items in a dictionary.

# dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# valueSum = sum(dict.values())
# keySum = sum(dict.keys())
# result = valueSum + keySum
# print(result)


# Write a Python program to multiply all the items in a dictionary.
# dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# result = 1 
# for key in dict:
#     result = result * dict[key]
# print(result)

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


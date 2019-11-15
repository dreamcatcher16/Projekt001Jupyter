# Plivanje
import pandas as pd
import numpy as np

data = pd.read_csv('Zad 4 - Podaci.txt', sep=",", header=None)
data.columns = ["Takmicar", "Vreme1", "Vreme2"]

podaci = data.set_index("Takmicar")
print()

# Ubacivanje nove kolone i nalazenje proseka
podaci["Prosek"] = 0.0
for takmicar in podaci.index:
    podaci.loc[takmicar, "Prosek"] = podaci.loc[takmicar, "Vreme1":"Vreme2"].mean()

# Sortiranje tabele po najbojim vremenima
sortirano = podaci.sort_values(by=["Prosek"])
# print (sortirano)

# Tabela bez pojedinacnih vremena
finale = sortirano.drop("Vreme1", axis=1)
finale = finale.drop("Vreme2", axis=1)
print("Prva tri takmicara su:")
print(finale.head(3))
print()
#print(finale)

# Finale A
print("Takmicari finala A su:")
finaleA = finale[finale.Prosek <= 27]
print(finaleA)
print()
finaleAtxt = finaleA.drop("Prosek", axis=1)
print(finaleAtxt)

with open('FinaleA.txt', 'w') as file:
    finaleAtxt.to_string(file)
print()    

# Finale B
print("Takmicari finala B su:")
finaleB = finale[(finale.Prosek > 27) & (finale.Prosek <= 29)]
print(finaleB)
print()

finaleBtxt = finaleB.drop("Prosek", axis=1)
print(finaleBtxt)
with open('FinaleB.txt', 'w') as file:
    finaleBtxt.to_string(file)
print()   

# Nisu se plasirali
print("Takmicari koji se nisu plasirali su:")
finaleN = finale[(finale.Prosek > 29)]
print(finaleN)
#finaleNtxt = finaleN.drop("Prosek", axis=1)
#brojN = finaleNtxt.count()
brojN = len(finaleN.index)
print(finaleN)
print("Broj takmicara koji se nije kvalifikovao: ")
print(brojN)
print()


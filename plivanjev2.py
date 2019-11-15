# Plivanje
import pandas as pd
import numpy as np


# Formiranje tabele iz fajla
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


# Tabela bez pojedinacnih vremena
finale = sortirano.drop("Vreme1", axis=1)
finale = finale.drop("Vreme2", axis=1)
print("Prva tri takmicara su:")
print(finale.head(3))
print()

# Finale A

finaleA = finale[finale.Prosek <= 27]

#finaleAtxt = finaleA.drop("Prosek", axis=1)

# Snimanje u fajl FinaleA.txt
#with open('FinaleA.txt', 'w') as file:
#    finaleAtxt.to_string(file)
np.savetxt(r'FinaleA.txt', finaleA.index, fmt='%d')
# Finale B

finaleB = finale[(finale.Prosek > 27) & (finale.Prosek <= 29)]
print(finaleB)
#finaleBtxt = finaleB.drop("Prosek", axis=1)

# Snimanje u fajl FinaleB.txt
#with open('FinaleB.txt', 'w') as file:
#    finaleBtxt.to_string(file)
np.savetxt(r'FinaleB.txt', finaleB.index, fmt='%d')

# Nisu se plasirali

finaleN = finale[(finale.Prosek > 29)]
brojN = len(finaleN.index)
print("Broj takmicara koji se nije kvalifikovao: ")
print(brojN)
print()

# Tri najuspesnija takmicara B finala
print("Tri najuspesnija takmicara B finala su takmicari: ")
finaleB3 = finaleB.drop("Prosek", axis=1)
for i in range(3):
    print(i+1, ". ", finaleB3.index[i])
print()





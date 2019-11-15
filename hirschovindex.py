# Citiranost istrazivaca

#podaci = [12, 3, 4, 0, 1, 3, 0, 23, 4, 5, 10, 4, 2, 6, 9, 0, 2, 1, 1, 4, 2, 1]


print('Unesite brojeve citata naucnih radova razdvojene razmaknicom: ')
podaci = [int(x) for x in input().split()]

n = len(podaci)

print()
print('Hirsov h-indeks niza:', podaci)
podaci.sort()
for i in range(n):
    if podaci[i] <= n - i:
        hi = podaci[i]
print('je: ' , hi)

prosecnacitiranost = sum(podaci) / n
print()
print('Prosecna citiranost je: ', round(prosecnacitiranost,2))

podaci.sort()
if n % 2 == 0:
    medijana = (podaci[n // 2] + podaci[n // 2 - 1])/2
else:
    medijana = podaci[n // 2] 
print()
print('Medijana je: ', medijana)
print()



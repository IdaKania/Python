import numpy.matlib
import numpy as np  
from numpy import random


l1 = int(input("Podaj ilosc wierszy macierzy: "))
l2 = int(input("Podaj ilosc kolumn macierzy: "))

m1 = random.randint(15, size=(l1, l2))
m2 = random.randint(15, size=(l1, l2))

print("Macierz 1")
print(m1)
print(end='\n')
print("Macierz 2")
print(m2)
print(end='\n')

suma = m1 + m2
iloczyn = m1 * m2

print(end='\n')
print("Suma macierzy")
print(suma)

print(end='\n')
print("Iloczyn macierzy")
print(iloczyn)

"""Oppgave 2.2 Fysikkheftet"""

import numpy as np

m = 1200
c = 3*10**8


v_lst = np.linspace(0, 0.9, 10)
#print(v_lst)
v_lst = v_lst * c
#print(v_lst)

p_lst = v_lst * m
#print(p_lst)


print("v | p")
for i in range(len(v_lst)):
    print(f"{v_lst[i]:.2e} | {p_lst[i]:.2e}")

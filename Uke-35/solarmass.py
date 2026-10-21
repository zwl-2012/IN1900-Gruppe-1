# -*- coding: utf-8 -*-
"""@author: zliu2
Oppgave 1.1 Solar mass - Fysikkheftet"""


import numpy as np 


lysar = 9.5 * 10**(12) * 1000 # lysaar (m)
AU = 1.58 * 10**(-5) * lysar  # 1 AU 
G = 6.674 * 10**(-11) # G 
yr = 365 * 24 * 3600 # 1 yr (s)


M_sol = (4 * np.pi**2 * AU**3) / (G * yr**2) # Solar mass (kg)

#print(M_sol)

M_str = str(M_sol)
print(M_str)
#print(type(M_str))
#print(len(M_str))

base = ""
for i in range(0, 4):
    base += M_str[i]

exponent = ""
for j in range(len(M_str)-2, len(M_str)): # range(20, 22) = 20,21
    exponent += M_str[j]
#print(exponent)


print(f"M_sol = {base} * 10^{exponent} kg")




def is_standard_form(str_num):
    # check if num is on standard form (e+...) or not
    state = False
    for e in str_num:
        if e == "e":
            state = True
            break
    return state


def find_index(string, letter="e"):
    idx = 0
    for i in len(string):
        if string[i] == letter:
            idx = i
            break
    return idx


#8*10^(30)
#8*10(-30)
#-8*10^(30)
#800
# 0.8

def standard_form(num, decimals):
    if decimals < 0 or type(decimals) != int:
        raise ValueError("Decimal not specified")
    
    string_num = str(num)
    form = ""
    if is_standard_form(string_num):
        idx = find_index(string_num)
        base = string_num[:idx]
        base = round(float(base), decimals)
        sign = string_num[idx+1]
        exponent = string_num[idx+2:]
        if sign == "-": form = f"{base} * 10^({-exponent})"
        else: form = f"{base} * 10^({exponent})"
    else: 
        return
        
        












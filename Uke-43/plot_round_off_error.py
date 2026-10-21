########## 7.5 ##########
import numpy as np
import matplotlib.pyplot as plt

print("\n---------- 7.5 round_off_error.py ----------\n")

delta_x = []
abs_error = []
n = []

filename = "plot_round_off_error.txt"

with open(filename, "r") as f:
    f.readline()
    for line in f:
        round_lst = line.split(", ")


        curr_delta_x = round_lst[0].split(": ")
        delta_x.append(float(curr_delta_x[1]))

        curr_abs_error = round_lst[3].split(": ")
        abs_error.append(float(curr_abs_error[1]))


        curr_n = round_lst[-1].split("=")
        n.append(int(curr_n[1]))



        f.readline()




"""
#plt.plot(n, delta_x)
plt.semilogy(n, delta_x)
plt.title("delta_x")
plt.show()
"""

#plt.plot(n, abs_error)
plt.semilogy(n, abs_error)
plt.title("abs_error")
plt.show()


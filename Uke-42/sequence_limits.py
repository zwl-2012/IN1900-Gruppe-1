"""Oppgave A.1 Langtangen"""
import numpy as np
import matplotlib.pyplot as plt

##### a)
def a_n(n):
    an = (7 + 1/(n+1)) / (3 - 1/(n+1)**2)
    return an





##### b)
def D_n(n):
    Dn = np.sin(2**(-n)) / 2**(-n)
    return Dn




##### c)
def D(f, x, N):
    n_list = np.arange(0, N+1)
    h_list = np.zeros(len(n_list))
    for i in range(len(n_list)):
        h_list[i] = 2**(n_list[i])
    
    Dn = (f(x + h_list) - f(x))  / h_list
    
    return Dn, n_list



def plot_D(Dn, n_list):
    plt.plot(n_list, Dn)
    plt.show()
    return




if __name__ == "__main__":
    print("\n---------- sequence_limits.py ----------\n")
    
    #print(D_n(10000))
    
    
    Dn, n_list = D(lambda x: np.sin(x), np.pi, 40)
    plot_D(Dn, n_list)
    
    
    
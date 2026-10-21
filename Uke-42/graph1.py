"""Oppgave 6.14 Oppgaveheftet"""
import numpy as np
import matplotlib.pyplot as plt




##### a)
"""
def plot_line(p1, p2):
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    
    plt.plot(x, y)
    plt.show()
"""





##### b)


def plot_line(p1, p2):
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    
    plt.plot(x, y, color="blue", marker="o")
    #plt.show()



def complete_graph(points):
    L = len(points)
    
    for i in range(0, L-1):
        for j in range(i+1, L):
            print(points[i], points[j])
            plot_line(points[i], points[j])
    plt.show()
            
            
    
    
            
            
    
    






if __name__ == "__main__": 
    print("\n---------- graph1.py ----------\n")
    
    
    ########## a) 
    p1 = [0,0]
    p2 = [1,1]
    
    #plot_line(p1, p2)
    
    
    
    
    
    
    
    
    
    
    
    
    ########## b) 
    points_square = [[0,0], [1,0], [0,1], [1,1]]
    
    complete_graph(points_square)
    
    
    a = np.sqrt(2)/2
    points_eight = [[1,0], [a,a], [0,1], [-a,a],
                    [-1,0], [-a,-a], [0,-1], [a,-a]]
    
    complete_graph(points_eight)
    
    
    
    
    
    
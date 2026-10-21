
import sys

def F(m1, m2, r):
    G = 6.674 * 10**(-11)
    return (G*m1*m2)/r**2





try:
    M = sys.argv[1]
except: 
    raise IndexError("M not defined")
    






try: 
    M = float(M)
except:
    raise ValueError("M not a float")



try:
    filename = sys.argv[2]
except:
    raise IndexError("File not defined")
    


try: 
    file = open(filename, "r")
except: 
    raise IOError("File doesnt exist")

print("Success")


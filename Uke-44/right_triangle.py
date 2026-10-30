import numpy as np
import matplotlib.pyplot as plt



class RightTriangle:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Argument(s) is negative")
        self.a = a
        self.b = b
        self.c = np.sqrt(a**2 + b**2)

    
    def plot_triangle(self):
        plt.axis("equal")
        plt.plot([0, self.a], [0, 0])
        plt.plot([self.a, self.a], [0, self.b])
        plt.plot([0, self.a], [0, self.b])
        
        """Alternativ plot metode"""
        #plt.plot([0, self.a, self.a, 0], [0, 0, self.b, 0])
        
        plt.show()




def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success





print("\n---------- right_triangle.py ----------\n")

##### b)
#triangle1 = RightTriangle(1, 1)
#print(triangle1.c)


#triangle2 = RightTriangle(3, 4)
#print(triangle2.c)



##### c)
#test_RightTriangle()
#triangle4 = RightTriangle(1,-1)



##### d)
triangle5 = RightTriangle(3, 4)
triangle5.plot_triangle()




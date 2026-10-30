import numpy as np
import matplotlib.pyplot as plt


class Diff:
    def __init__(self, f):
        self.f = f
    
    def diff1(self, x, h):
        d1 = (self.f(x+h) - self.f(x))/h
        return d1
    
    def diff2(self, x, h):
        d2 = (self.f(x+h) - self.f(x-h))/(2*h)
        return d2
    
    def diff3(self, x, h):
        d3 = (-self.f(x+2*h) + 8*self.f(x+h) - 8*self.f(x-h) + self.f(x-2*h)) / (12*h)
        return d3




print("\n---------- class_diff.py ----------\n")

x = np.linspace(-1, 1, 101)
h_list = [0.9, 0.6, 0.3, 0.1]

f = lambda x: np.sin(2*np.pi*x)
df = lambda x: 2*np.pi * np.cos(2*np.pi*x)

df_exact = df(x)

diff = Diff(f)
for h in h_list:
    plt.plot(x, diff.diff1(x, h), label=f"d1")
    plt.plot(x, diff.diff2(x, h), label=f"d2")
    plt.plot(x, diff.diff3(x, h), label=f"d3")
    plt.plot(x, df_exact, label="exact", linestyle="dotted")
    plt.legend()                # for labels to appear
    plt.title(f"h={h}")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.show()



    
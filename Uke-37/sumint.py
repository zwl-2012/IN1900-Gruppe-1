#### Problem 4.2 Sum of integers 
#### Recap week 37


#### a) 
def sumint(n):
    s = 0 
    for i in range(1, n+1): 
        s += i 
    return s


### b)
def sumint_fast(n): 
    return int(n*(n+1)/2)



### c)
def test_sumint():
    n = 10
    expected = sumint(n)
    predicted = sumint_fast(n)
    tol = 1e-8 
    msg = "expected and predicted not aligned"
    diff = abs(expected - predicted)
    
    if diff > tol: 
        raise ValueError(msg)
    
    print("Test successful")
    
    




#### Results
if "__main__" == __name__:
    print("4.2 Sum integers")
    #print(sumint(10)) # 55
    #print(sumint_fast(10)) # 55
    #test_sumint()
    print(sumint_fast(10))
    
    
    
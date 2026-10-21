
import sys

### Old 
"""
status = True
try: 
    a = sys.argv[1]
except:
    raise IndexError("a is not defined")
"""


 
    
### check if a is defined

status = True

try: 
    a = sys.argv[1]
except:
    status = IndexError
    
if status is IndexError: 
    a = input("Define a: ")
    print(a)  
    



### check if b is defined
    
status = True

try: 
    b = sys.argv[2]
except:
    status = IndexError
    
if status is IndexError: 
    b = input("Define b: ")
    print(b)  





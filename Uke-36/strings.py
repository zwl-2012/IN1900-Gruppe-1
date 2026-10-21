
"""f strings, something to be very aware of"""


### Types of ways to generate a string object (str)

## Method 1 - convert number into strings
num = 5
string = str(5) # <class 'str'>
#print(type(string))


## Method 2 - using " "
string = "5"



## Method 3 - using ' '
string = '5'


## Method 4 - f-strings
string = f"{num}"




## Honourable mentions: '%e', '%g'
## ineffective, hard syntax, f-string is better!



## Be aware of this with f-strings
string = f"{num} is an 'integer'"
# 5 is an 'integer'
#print(string)
































string = f'{num} is an "integer"'
# 5 is an "integer"
#print(string)








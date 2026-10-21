"""While loops"""


##Example: Generate next even number for each use of keyboard, starting with number 2

even = 2
print("Even number is:", even, "\nTo quit: Q")
while True:
    state = input()
    if state == "Q":
        print("Ending sequence")
        break
    else: 
        even += 2 
        print(even)


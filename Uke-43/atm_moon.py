########## 7.4 ##########
print("\n---------- 7.4 atm_moon.py ----------\n")

moon_dict = {}
filename = "atm_moon.txt"



with open(filename, "r") as f:
    f.readline()
    for line in f:
        elements = line.split(" ; ")
        for element in elements:
            name_val = element.split(" - ")

            name = name_val[0].upper()

            value = int(name_val[1].replace(",", ""))

            moon_dict[name] = value



print(moon_dict)

    
    

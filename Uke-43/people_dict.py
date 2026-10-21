########## 7.6 ##########
print("\n---------- 7.6 people_dict.py ----------\n")

people = {}

filename = "people_file.txt"


with open(filename, "r") as f:
    for line in f:
        lst = line.split(", ")
        name = lst[0]
        age = int(lst[1])
        gender = lst[2]

        people[name] = {"Age": age, "Gender": gender[:-1]}

print(people)
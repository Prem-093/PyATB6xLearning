my_list = [1, 2, 3]
my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[1] = "Dutta"

for element in my_list:
    print(element)

for i in range(1,5):
    print(i)



my_list = [1, 2, 3]
print("index at zero location:", my_list[0])
print("index at zero location:", my_list[1])
print("index at zero location:", my_list[2])

##add single entry in list
my_list.append(4) ##add single entry in list

print(my_list)

##add multiple entry in list
#To add multiple records in list use extend
my_list.extend([4,5,6,"Prem"])
print(my_list)

#Insert use for new entry
my_list.insert(1,"tripathi")
print(my_list)

# Remove entry from list
my_list.remove("Prem")
print(my_list)

#Copy list
my_list_copy=my_list.copy()
print(my_list_copy)
my_dict={
        "name":"Prem",
        "Age":"32",
        "Address":"M.I.G 282",
        "Profession":"Software Engineer"
}

print(my_dict)
print(my_dict["name"])
del my_dict["Profession"]
print(my_dict)

for k,v in my_dict.items():
    print(k,v)
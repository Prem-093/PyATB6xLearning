person_info={
    "name":"Prem",
    "Age":"32",
    "address":{
        "off_address":"lkw",
        "home_address":"gkp",

    }
}

person_info1 = {
    "name": "Tripathi",
    "Age": "32",
    "address": {
        "off_address": "lkw",
        "home_address": "gkp"

    }
}

person_info3 = {
    "name": "mani",
    "Age": "32",
    "address": {
        "off_address": "lkw",
        "home_address": "gkp"

    }
}


person_list=[person_info,person_info1,person_info3]

print(person_list)
print(person_list[0])
print(person_list[1])
print(person_list[2])
print(person_list[0]["address"]["off_address"])

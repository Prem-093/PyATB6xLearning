shopping_list_wife=["bread","butter","paneer"]
shopping_list_wife[1]=["cheese"]
print(shopping_list_wife)


# Real of Tuples

my_tuple=("tta.com","sdet.live")
print(my_tuple)
#my_tuple[2]=("cfc.com")

my_api_list=list(my_tuple)
print(my_api_list)

my_api_list.append("abc.com")

print(my_api_list)

#convert again in tuple

my_api_list2=tuple(my_api_list)
print(my_api_list2)

# Real case, where we Tuples

API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[1])
print(API_URLSs[0])

t = tuple()
print(t)

l = list()
print(l)

# Conversion List to Tuple

listT1=["prem","butter","paneer"]
tup=tuple(["prem","butter","paneer"])
print(tup)

Weapon1=("AK47","AK56","Rifle")
Misiles=("Pinaka","Agni","Brahmos")

new_tuples=(Weapon1,Misiles)

print(new_tuples)
print(new_tuples[0])
print(new_tuples[1])
print(new_tuples[0][0])
print(new_tuples[0][1])
print(new_tuples[1][1])
print(new_tuples[1][0])
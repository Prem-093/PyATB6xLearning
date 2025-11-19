cities=("Pune","Delhi","Mumbai")
print(len(cities))
print("Pune" in cities)
print("Delhi" in cities)


new_url=tuple(["www.abc.com","www.sdet.com","www.testingacad.com"])
print(new_url)

for i in cities:
    print(i)

numbers="pramod" *3
print(numbers)

numbers=(1,2) * 3
print(numbers)

num=(1,2,3,4,5)
print(len(num))
print(num.count(3))
print(num.index(3))

new_list=list(num)
print(new_list)

#back to tuple
num_tuple=tuple(new_list)
print(num_tuple)

print(max(num_tuple))


my_list = [1, 2, 3]
print(my_list[0:2])
print(my_list[-1])



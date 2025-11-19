set1=set(["abc","test","xyz"])
print(set1)
print(len(set1))

for i in set1:
    print(i)

set1.add("pramod")
set1.add("pramod")
print(set1)


squares = {x ** 2 for x in range(5)}
print(squares)

my_list=[1,2,3,3]
new_set=frozenset(my_list)
print(new_set)
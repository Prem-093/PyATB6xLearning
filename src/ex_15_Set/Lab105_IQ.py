# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer

# print("swiss".count("s"))
# print("swiss".count("w"))
# print("swiss".count("i"))

s=set()

def firstNonRepetativeCharacter(string):
    for char in string:
        if string.count(char)==1:
            s.add(char)
            return char
    return None


print(firstNonRepetativeCharacter("swiss"))
print(s)
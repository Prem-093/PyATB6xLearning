squares = [1, 4, 9, 16, 25]
print(squares)
print(squares.pop())
print(squares.pop(1))
print(squares)
squares.clear()
print(squares)

# index(element, start, end)
# Returns the index of the first occurrence of the element.
numbers = [10, 20, 30, 20, 40]

print(numbers.index(30))

print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# reverse() Reverses the list in place.
numbers.reverse()
print(numbers)
# max() / min() / sum() Works for numerical lists.
print(max(numbers))

print(min(numbers))

print(sum(numbers))

# Slicing

print(numbers[2:4])

print(numbers[1:4])  # from index of 1 to 3
print(numbers[-1])  # # Last element

# List Creation and Comprehension

# range(1,5) -> list
l=list(range(1,5))
print(l)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

# del statement - Deletes an element by index or the whole list.
del numbers[0]
print(numbers)
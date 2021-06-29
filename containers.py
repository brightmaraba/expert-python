# Lists - Dynamic sequence of objects
# Tuples - Immutable sequence of objects
# Dictionaries - key: pair values
# Sets - Uniqueness is key
# List comprehension

evens = [i for i in range(100) if i % 2 == 0]
print(f'The even numbers between 1 and 100 are: {evens}')

# Enumerate
for i, element in enumerate(['One', 'Two', 'Tree']):
    print(f'{i} : {element}')

# Zip
for items in zip([1,2,3], [4,5,6]):
    print(items)

# Reverse Zip
for items in zip(*zip([1,2,3], [4,5,6])):
    print(items)

# Unpacking
x, y, z = 10, 20, 30
print(f'x = {x}, y = {y}, z = {z}')

first, second, *rest = 0, 1, 2, 3
print(f'{first}, {second}, {rest}')

first, *inner, last = 0, 1, 2, 3
print(first, inner, last)

# Nested Unpacking
(a, b), (c, d) = (1, 2),(3, 4)
print(a, b, c, d)

# Dictionaries
person = {
    'name': 'Brian',
    'age' : 75,
    'address': '25 A Sussex Street',
    'state': 'Western Australia',
    'zip_code': 6061
}
print(person)

# Iterating Dictionary
# Using key
for key in person:
    print(key)

# Trick to process both keys and values
for key in person:
    print(key, '->', person[key])

# Iterating using .items() ==> Produces Tuples of k.v pairs.
for key, value in person.items():
    print(key, '-->', value)

# Using comprehension and dicts
squares = {number: number**2 for number in range(100)}
print(squares)

# set() - This is a mutable, non-ordered, finite collection of unique, immutable(hashable) objects
# frozen()-Immutable sets

a = set([frozenset([1,2,3]), frozenset([1,2,3,4])])
print(a)
b = set({element for element in range(20)})
print(b)
substrings = ['These', 'are', 'strings', 'to', 'concatanate.']

s = ' '

# Highly inefficient
# for substring in substrings:
#     s += substring
# print(s)
s = ' '.join(substrings)
print(s)
# OR using an "unbound" method call
x = str.join(' ', substrings)
print(x)


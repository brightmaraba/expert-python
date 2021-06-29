# Iterators 
# - __next__ : Returns the next item of a container
# - __iter__ : Returns the iterator itself
# Generators
# Decorators
# Context Managers

i = iter('My Name is Brian')

class CountDown:
    def __init__(self, step):
        self.step =step

    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Return the iterator itself."""
        return self
count = 0
count_down = CountDown(4)
# for each_element in count_down:
#     print(f'Element {count} is {each_element}')
#     count+=1
# else:
#     print("Done!")

# Generators and yield statements
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for i in range(100)])
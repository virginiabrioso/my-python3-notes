# An iterator is an object that can be iterated (looped) upon, and it implements two methods:
#   __iter__(): Returns the iterator object itself.
#   __next__(): Returns the next item in the sequence.

# iterators.py

# A custom iterator class that iterates through a list
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # Raise StopIteration to signal the end of the iteration

# Creating an instance of MyIterator
numbers = [1, 2, 3, 4, 5]
iterator = MyIterator(numbers)

# Using the iterator with a for loop
print("Iterating over MyIterator:")
for number in iterator:
    print(number)


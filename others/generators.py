import sys

# problem
x = [i**2 for i in range(10000)] #take lot m/o

# for el in x:
#     print(el)

# partial soln w/o gen.


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv


# g = Gen(100)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

#  Using Generators


def gen(n):
    for i in range(n):
        yield i**2


g = gen(10000)

# for i in g:
#     print(i)

print("\nM/m list-", sys.getsizeof(x))
print("M/m generators-", sys.getsizeof(g))
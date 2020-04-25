from collections import Counter
import itertools

a = [1, 2, 3, 'a']
b = ['a', 3, 2, 5, 6, 'v']
print(set(a).intersection(b))

a = [[1, 2], [3, 4], [5, 6], [7, 8]]

a_ = list(itertools.chain.from_iterable(a))
print(a_)

# result = list(map(lambda x: int(x), input().split(" ")))
# print(result)

myList = [1, 2, 1, 25, 2, 3, 1, 9, 25, 2, 1, 3, 24]
print(Counter(myList))

a= [1,2,4,5,3]
b = [0,9,6,8,7]

for i , j in zip(a,b):
    print(i+j)

words = ['hi','set','Raman','def','hi', 'hi','set','Friends']
words_count = Counter(words)
print(type(words_count))
top_two = words_count.most_common(3)
print(top_two)


"""Task 1"""


def genarator(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_n = genarator(int(input()))
# вывидет в конце ошибку StopIteration при условии что число будет < 11
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
def fibon():
    n = 100
    for i in range(n):
        yield i
    print(i)

gen = fibon()
print(gen)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())




# def fibon(n):
#     a = b = 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
#
# for x  in fibon(10):
#     print(x)



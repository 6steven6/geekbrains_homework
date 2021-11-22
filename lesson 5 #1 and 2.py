# def numbers(num):
#     for i in range(1, num + 1, 2):
#         yield i
#
#
# gen = numbers(16)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

"""номер 2"""

num = 15
num_gen = (i for i in range(1, num + 1, 2))

print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

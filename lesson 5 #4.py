src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num = [num1 for i, num1 in zip(src, src[1:]) if num1 > i]
print(num)

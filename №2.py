numbers = []
for num in range(1, 1001, 2):
    numbers.append(num ** 3)

final_sum = 0
for num in numbers:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)


final_sum = 0
for num in numbers:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)
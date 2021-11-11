import math

goods = [16.04, 53.55, 4, 34.34, 89.3, 67.98, 45.77, 41.1, 90.43, 81.11, 19.22, 51.87, 99.99, 78.45, 79, 88.21, 36.63,
         48.89, 86.32, 98.5]

# for prices in goods:
#     cents = prices % 1 * 100
#     cents = math.ceil(cents)
#     cents = int(cents)
#     prices = f' цена: {int(prices // 1)} руб {cents:02d} копеек '
#     print(prices, end = '')  # задание a


# goods_sorted = sorted(goods)
# print(goods_sorted) # задание b

new_list = sorted(goods)
print(sorted(new_list)) # задание c

max_five = new_list[-5:len(new_list)]
print(max_five) # задание d




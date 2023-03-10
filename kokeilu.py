
# t = (1, 2, 3, [1, 2, 3], True)

# for x in t:
#     print(type(x))


# t = (1, 2, 3, [1, 2, 3], True, 'Bob', 35, 100000, [
#      '50', '60', '70'], 0, 23, 45, 1000, 12, [], 10)

# print('Length of the tuple is:', len(t))

# l = []
# counter = -1

# for x in t:
#     l.append(x)
#     counter += 1
#     if type(x) == list:
#         print(f'List found at index: ', counter,
#               '. ', 'Length: ', len(l[counter]), '.', sep='')

# print(l)


# y = 10

# m = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# row_1 = m[0]
# row_2 = m[1]
# row_3 = m[2]

# row_1_col_1 = row_1[0]


# from timeit import timeit
# l = []
# x = timeit('l.append(1)', globals=globals(), number=100_000)
# print(x)

# l = []
# y = timeit('l.insert(0, 1)', globals=globals(), number=100_000)
# print(y)

# print(y/x)


# t1 = 1, 2, 3, 4, 5, 6
# t2 = 7, 8, 9, 10
# t3 = 11, 12, 13, 14, 15, 16, 17

# list_of_zeroes = []

# list_one = list(t1+t2+t3)
# odd_count = len(list_one[::2])

# for i in range(0, odd_count):
#     list_of_zeroes.append(0)

# list_one[::2] = list_of_zeroes

# result = tuple(list_one)
# print(result)


# odd_numbers = [1, 3, 5, 7, 9]
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0

# for x in odd_numbers:
#     if x in number_list:
#         counter += 1
# print('Odd numbers found:', counter)


# a = 8.23489734789
# b = a // 1
# c = b % 2
# print(b)
# print(c)


# data = [
#     (100, 'USD', 'EUR', 0.83),
#     (100, 'USD', 'CAD', 1.27),
#     (100, 'CAD', 'EUR', 0.65)
# ]

# row = 0

# amount, currency, target_currency, exchange_rate = data[row]
# converted = amount * exchange_rate
# print(amount, currency, '=', converted, target_currency, sep=' ')

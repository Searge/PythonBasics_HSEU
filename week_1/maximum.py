# Напишите программу, которая считывает два целых числа A и B
# и выводит наибольшее значение из них. Числа — целые от 1 до 1000.
a, b = [int(input()) for i in range(2)]

diff_positive = (a - b) ** 2
diff_sqrt = diff_positive ** .5

result = sum([a, b, diff_sqrt]) / 2
print(int(result))

# Напишите программу, которая считывает два целых числа A и B
# и выводит наибольшее значение из них. Числа — целые от 1 до 1000.
a, b = [int(input()) for i in range(2)]

# підносимо різницю в ступінь, щоб позбутися мінусу:
diff_positive = (a - b) ** 2
diff_sqrt = diff_positive ** .5

# додаємо до меншого числа його різницю з більшим
# в результаті отримуємо суму двох більших чисел:
result = sum([a, diff_sqrt, b]) / 2
print(int(result))

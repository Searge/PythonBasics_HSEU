Рассмотрим несколько задач, решаемых с помощью арифметических операций, которые показывают некоторые идеи.

Пусть есть два товара, первый из них стоит A рублей B копеек, а второй - C рублей D копеек. Сколько рублей и копеек стоят эти товары вместе.

В задачах где есть несколько размерностей величин (например, рубли и копейки, километры и метры, часы и минуты) следует переводить все в наименьшую единицу измерения, осуществлять необходимые действия, а затем переводить обратно к нужным единицам.

В нашей задаче наименьшей единицей являются копейки, поэтому все цены следует перевести в них, затем сложить их, а затем перевести результат обратно в рубли и копейки. Код решения будет выглядеть так:

```python
a = int(input())
b = int(input())
c = int(input())
d = int(input())
cost1 = a * 100 + b
cost2 = c * 100 + d
totalCost = cost1 + cost2
print(totalCost // 100, totalCost % 100)
```

Для определения количества рублей нужно разделить цену в копейках на 100 нацело, а для определения оставшегося числа копеек - посчитать остаток от деления на 100.

Следующая задача: Вася играет в Super Mario Bros. очень хорошо и получил N дополнительных жизней. Известно, что переменная, в которой хранится количество жизней может принимать значения от 0 до 255. В случае, если было 255 жизней и игрок получил дополнительную жизнь, счетчик обнуляется. Сколько жизней на счетчике?

В этой задаче достаточно посчитать остаток от деления введенного числа на 256. Такие действия часто требуются, например, при работе со временем (при переходе через сутки счетчик времени обнуляется). Решение задачи выглядит так:

```python
n = int(input())
print(n % 256)
```
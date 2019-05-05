# https://habr.com/ru/post/311680/
# H — висота шеста
# A — поднимается за день
# B — спускается за ночь
H, A, B = [int(input()) for _ in range(3)]
top = 1

# День в который доползет до вершины
h_night = H - B - top
speed = A - B
finish = h_night // speed + top

print(finish)

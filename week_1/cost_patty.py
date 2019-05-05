a, b, n = [int(input()) for i in range(3)]

rur = a * 100
kop = b
patty = sum([rur, kop])

total = patty * n

rur = total // 100
kop = total % 100

print(rur, kop)

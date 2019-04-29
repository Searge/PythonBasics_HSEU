N = int(input())

cent = N // 100
dec = N % 100 // 10
ones = N % 10

print(cent + dec + ones)

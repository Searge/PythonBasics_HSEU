# Выведите число секунд между этими моментами времени.
h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]


hour = lambda x: x * 3600
minute = lambda x: x * 60


h1, h2 = map(hour, (h1, h2))
m1, m2 = map(minute, (m1, m2))

start = sum([h1, m1, s1])
end = sum([h2, m2, s2])

print(end - start)

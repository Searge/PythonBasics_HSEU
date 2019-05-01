# задача з нулями вирішується так:
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/qoori/vtoraia-sprava-tsifra
N = int(input())

hour = N // 3600 % 24
minute = N // 60 % 60
second = N % 60

print("{}:{:02d}:{:02d}".format(hour, minute, second))

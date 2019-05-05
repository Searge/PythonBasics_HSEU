# В этой задаче необходимо проверить, делится ли
# число A на число B нацело.

a, b = [int(input()) for i in range(2)]

# modulus returns the value of the
remainder = a % b
_true, _false = 1, 2

yes = _true - remainder
no = ((remainder + _false) // (remainder + _true)) % _false

print('YES' * yes + 'NO' * no)

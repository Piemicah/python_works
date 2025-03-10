x = [5, 6, 2, 8, 9, 2, 9, 0, 2, 8, 4, 5, 7]

y = list(filter(lambda a: a > 4, x))

z = list(map(lambda a: a**2, x))

print(y)
print(z)

import math
# ---------------
# square rooting numbers

print('-- square rooting numbers --')

x = math.sqrt(117)
print(x)

print(math.sqrt(81))
print(math.sqrt(25))
print(math.sqrt(73))

# ---------------
# flooring (rounding) numbers

print('-- rounding numbers --')

y = math.floor(math.sqrt(x))
print(y)

print(math.floor(8.3))
print(math.floor(9.5))
print(math.floor(4.8))

# ---------------
# ceil - weird thing that gives you the highest value (ex: the ceil of 5.3 = 6)

print('-- math.ceil --')

z = math.ceil(math.sqrt(823))
print(z)

print(math.ceil(5.3))
print(math.ceil(10.7))
print(math.ceil(1.2))

# ---------------
# squaring numbers

print('-- squaring numbers --')

a = 3 ** 2
print(a)

print(9 ** 8)
print(4 ** 3)
print(13 ** 4)

# another way to square numbers, or set them to a power of something

print('-- math.pow --')

b = math.pow(3,2)
print(b)

print(math.pow(9,8))
print(math.pow(4,3))
print(math.pow(13,4))

# ---------------
# some random math functions

print('-- some random math functions --')

print(math.pi)
print(math.e)
print(math.inf)
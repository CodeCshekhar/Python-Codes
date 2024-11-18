# Example demonstrating the use of assignment operators in Python

a = 10
b = 5

# Assignment Operators
a = b  # a is now 5
print("a = b:", a)

a += b  # a is now 10
print("a += b:", a)

a -= b  # a is now 5
print("a -= b:", a)

a *= b  # a is now 25
print("a *= b:", a)

a /= b  # a is now 5.0
print("a /= b:", a)

a %= b  # a is now 0.0
print("a %= b:", a)

a **= b  # a is now 0.0 to the power of 5 which is 0.0
print("a **= b:", a)

a = 25
a //= b  # a is now 5
print("a //= b:", a)
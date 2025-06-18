def add_one(number):
    number += 1
    return number
x = 42
print(f"Before: {x}")
x = add_one(x)
print(f"After: {x}")

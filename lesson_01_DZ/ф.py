def remainder(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзяd.")
    return a % b

print(remainder(-10, 0))
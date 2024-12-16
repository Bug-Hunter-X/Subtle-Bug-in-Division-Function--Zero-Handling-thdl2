def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return 0  # Or raise an exception: raise ZeroDivisionError("Both inputs are zero.")
    if a == 0:
        return b
    if b == 0:
        return a
    return a / b

result = function_with_uncommon_error(0, 0)
print(result)
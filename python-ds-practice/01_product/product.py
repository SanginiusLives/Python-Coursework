def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """

    prod = [a, b]
    result = 1
    for num in prod:
        result = result * num

    return result

print(product(2, 2))
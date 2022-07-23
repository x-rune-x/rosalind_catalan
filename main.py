def catalan_numbers(n):
    if n == 1 or n == 0:
        return 1

    output = 0
    for k in range(1, n + 1):
        output += catalan_numbers(k - 1) * catalan_numbers(n - k)

    return output


print(catalan_numbers(7))

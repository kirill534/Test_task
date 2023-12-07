def row_sum_odd_numbers(n):
    an = 1 + (n - 1) * n
    return sum([num for num in range(an, an+2*n, 2)])


assert row_sum_odd_numbers(13) == 2197
assert row_sum_odd_numbers(19) == 6859

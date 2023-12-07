def sum_of_sums(n):
    def S(N):
        return N * (N + 1) // 2

    def Z(N):
        return N * (N + 1) * (N + 2) // 6

    return S(Z(n))


assert sum_of_sums(3) == 55
assert sum_of_sums(5) == 630

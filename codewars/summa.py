def sum_of_sums(n):
    def S(N):
        return N * (N + 1) // 2

    def Z(N):
        return N * (N + 1) * (N + 2) // 6

    return S(Z(n))


assert sum_of_sums(3) == 55
assert sum_of_sums(5) == 630

from collections import Counter
def find_maximum(nums):
    return Counter(nums).most_common(1)[0][0]


list1 = [1, 3, 6, 2, 12, 7, 9, 4, 3, 1, 12, 4, 5, 2, 4, 4]
maximux = find_maximum(list1)
print('Maximum', maximux)
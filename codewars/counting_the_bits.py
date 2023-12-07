class Solution:
    @staticmethod
    def countBits(num):
        counter = [0]
        for i in range(1, num + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter


s = Solution
assert s.countBits(2) == [0, 1, 1]

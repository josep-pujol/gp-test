
class PSBTree:
    """
    Partial Sums Binary Tree
    """
    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.aux = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < len(self.nums) + 1:
            self.aux[i] += diff
            i += i & -i

    def _sum_all(self, i):
        res = 0
        while i > 0:
            res += self.aux[i]
            i -= i & -i
        return res

    def sum(self, i, j):
        if not self.nums: 
            return  0
        return self._sum_all(j + 1) - self._sum_all(i)

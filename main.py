class Solution:
    def two_sum(self, nums, target):
        num_indices = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], index]
            num_indices[num] = index
        return -1

def main():
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.two_sum(nums1, target1)
    print(f"Перший масив: {nums1}, target: {target1}, Результат: {result1}")

    nums2 = [1, 2, 3, 7]
    target2 = 10
    result2 = solution.two_sum(nums2, target2)
    print(f"Другий масив: {nums2}, Ціль: {target2}, Результат: {result2}")

    nums3 = [5, 3, 20, 30]
    target3 = 9
    result3 = solution.two_sum(nums3, target3)
    print(f"Третій масив: {nums3}, Ціль: {target3}, Результат: {result3}")

if __name__ == "__main__":
    main()
import unittest

def max_experience(levels, experience):
    if not experience or not experience[0]:
        return 0

    dp = [[0] * (i+1) for i in range(levels)]
    dp[0][0] = experience[0][0]
    
    for i in range(1, levels):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + experience[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + experience[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + experience[i][j]
    
    return max(dp[levels-1])


class TestMaxExperience(unittest.TestCase):
    def test_example_case(self):
        levels = 4
        experience = [[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 12)

    def test_single_level(self):
        levels = 1
        experience = [[4]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 4)

    def test_varied_experience(self):
        levels = 3
        experience = [[1], [2, 3], [4, 5, 6]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 10)

    def test_empty_experience(self):
        levels = 0
        experience = []
        result = max_experience(levels, experience)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
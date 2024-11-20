from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([1,5,4,2,9,9,9], 3, 15), 2: ([4,4,4], 3, 0),
                            3: ([1,5,4,2,9,9,9], 1, 9), 4: ([9,18,10,13,17,9,19,2,1,18], 5, 68),
                            5: ([1,1,1,7,8,9], 3, 24)}
        self.__obj = Solution()
        return super().setUp()

    @timeout(0.5)
    def test_case_1(self):
        nums, k, output = self.__testCases[1]
        results = self.__obj.maximumSubarraySum(nums = nums, k = k)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

    @timeout(0.5)
    def test_case_2(self):
        nums, k, output = self.__testCases[2]
        results = self.__obj.maximumSubarraySum(nums = nums, k = k)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

    @timeout(0.5)
    def test_case_3(self):
        nums, k, output = self.__testCases[3]
        results = self.__obj.maximumSubarraySum(nums = nums, k = k)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

    @timeout(0.5)
    def test_case_4(self):
        nums, k, output = self.__testCases[4]
        results = self.__obj.maximumSubarraySum(nums = nums, k = k)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

    @timeout(0.5)
    def test_case_5(self):
        nums, k, output = self.__testCases[5]
        results = self.__obj.maximumSubarraySum(nums = nums, k = k)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

if __name__ == '__main__': unittest.main()
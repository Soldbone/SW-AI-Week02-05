class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_num = -1
        for i in range(len(nums)):
            if i == 0:
                last_num = nums[i]
            elif last_num == nums[i]:
                nums[i] = "_"
            else:
                last_num = nums[i]

        last_location = 0
        for i in range(len(nums)):
            if nums[i] != "_":
                nums[last_location], nums[i] = nums[i], nums[last_location]
                last_location += 1

        return last_location


solution = Solution()
nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums2 = [1, 1, 2]
nums3 = []
print(solution.removeDuplicates(nums3))

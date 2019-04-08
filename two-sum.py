"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""

def twoSum(nums, target):
    nums_sorted = [i for i in sorted(enumerate(nums), key=lambda x:x[1])]

    for i in range(len(nums)):
        # break condition:
        # 2. nums_sorted[i] >= target / 2
        small_number = nums_sorted[i][1]
        if small_number > target / 2:
            return None
        for j in range(len(nums) - 1, i, -1):
            # 3. nums_sorted[j] < target / 2
            big_number = nums_sorted[j][1]
            if big_number < target / 2:
                continue
            if small_number + big_number == target:
                return [nums_sorted[i][0], nums_sorted[j][0]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
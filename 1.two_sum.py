def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums, target):
    for i in range(0, len(nums)):
        if (target - nums[i]) in nums:
            return i, nums.index((target - nums[i]))


def online_solution(nums, target):
    find_result = {}
    for i, num in enumerate(nums):
        if target - num in find_result:
            return [find_result[target - num], i]
        else:
            find_result[num] = i


def main():
    print(online_solution([2, 7, 11, 15], 9))


main()



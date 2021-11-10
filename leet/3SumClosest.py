"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""


def three_sum_closest(nums, target):
    nums = sorted(nums)
    delta = target + 10e4*3
    ans = sum(nums[:3])
    for i in range(len(nums)-2):
        p1 = i+1
        p2 = len(nums)-1
        while p1 < p2:
            currsum = nums[i] + nums[p1] + nums[p2]

            if currsum == target:
                return target

            # update ans if currsum closer to target
            if abs(currsum - target) < delta:
                ans = currsum
                delta = abs(currsum - target)

            if currsum < target:
                p1 += 1
            else:
                p2 -= 1
    return ans


three_sum_closest(
[0,-4,1,-5],0)

assert three_sum_closest([0, 0, 0],1), 0

assert three_sum_closest([1,1,1,0],100), 3


r=three_sum_closest([-1,2,1,-4],1)

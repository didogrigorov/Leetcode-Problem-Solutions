class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list2 = []
        for i in range(len(nums)):
            for y in range(i):
                if nums[i] == nums[y] and nums[i] + nums[y] == target:
                    list2.append(y)
                    list2.append(i)
                    break
                elif nums[i] == nums[y]:
                    continue
                else:
                    if nums[i] + nums[y] == target:
                        list2.append(y)
                        list2.append(i)
        return list2       

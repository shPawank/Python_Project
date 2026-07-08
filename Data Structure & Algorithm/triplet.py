nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
result = []
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = [nums[i], nums[j], nums[k]]
                if triplet not in result:
                    result.append(triplet)
print(result)
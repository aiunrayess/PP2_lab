def unique(nums):
    m = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                m.append(nums[i])
    while len(m) > 0:
        while m[0] in nums:
            nums.remove(m[0])
        m.pop(0)
    print(nums)

nums = []

while True:
    a = input()
    if a == "Stop":
        break
    nums.append(a)

unique(nums)
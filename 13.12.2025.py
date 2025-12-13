with open('907.txt') as f:
    cnt = 0
    for line in f:
        nums = list(map(int, line.split()))
        if len(set(nums)) != 5:
            continue
        nums.sort()
        if nums[3] + nums[4] <= nums[0] + nums[1] + nums[2]:
            cnt += 1

print(cnt)
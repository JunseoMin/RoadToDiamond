n = int(input())
dollors = [25,10,5,1]
for _ in range(n):
    nums = ['0','0','0','0']
    gusurum = int(input())
    i = 0
    while gusurum:
        nums[i] = str(gusurum // dollors[i])
        gusurum %= dollors[i]
        i += 1

    print(" ".join(nums))
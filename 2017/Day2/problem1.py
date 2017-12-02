with open("2017/Day2/input.txt") as f:
    # total = 0
    # for l in f:
    #     nums = [int(i) for i in l.split("\t")]
    #     total = total + (max(nums) - min(nums))
    # print total

    # As a one-liner
    print sum([max(nums) - min(nums) for nums in [[int(i) for i in l.split("\t")] for l in f]])
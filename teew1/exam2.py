def two_sum(nums, traget):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if i + j == traget:
                print(f"{i}, {j} = {traget}")
    else:
        return[]

two_sum = [1, 2, 3, 7, 8]
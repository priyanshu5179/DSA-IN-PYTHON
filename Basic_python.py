'''a=234
print(a)
'''
print (432)
nums = [5, 2, 8, 1, 4]

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[j] < nums[i]:
            count += 1
    print(f"Numbers less than {nums[i]} = {count}")

n = int(input())
nums = str(input())
nums = nums.replace(" ", "")

for i in range(0, len(nums), 5):
    try:
        print(nums[i:i+5])
    except:
        print(nums[i:])
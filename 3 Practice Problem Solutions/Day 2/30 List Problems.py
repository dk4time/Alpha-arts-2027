#Reverse A List
nums = list(map(int, input().split()))

print(nums[::-1])

#Second Largest
nums = list(map(int, input().split()))

nums = list(set(nums))
nums.sort()

print(nums[-2])

#Largest Smallest Sum Average
nums = list(map(int, input().split()))

print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#Remove Duplicates
nums = list(map(int, input().split()))

result = list(set(nums))

print(result)

#Rotate List
nums = list(map(int, input().split()))
k = int(input())

k %= len(nums)

print(nums[-k:] + nums[:-k])
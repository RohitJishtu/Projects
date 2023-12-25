# Two Sum
# Example 1:

# Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. Example 2:

# Input: nums = [3,2,4], target = 6 Output: [1,2] Example 3:

# Input: nums = [3,3], target = 6 Output: [0,1]


nums = [3, 2, 4]
target = 6
output = []
dict = {}

# Iterate through the elements in 'nums'
for i in range(0, len(nums)):
    # Check if the current element complements any previous element
    if nums[i] in dict:
        # Found a pair, add indices to 'output'
        output.append(i)
        output.append(dict[nums[i]])
        # Display current dictionary state for reference
        print('dict If', dict)
    else:
        # Store the complement (target - current element) with its index
        dict[target - nums[i]] = i
        # Display current dictionary state for reference
        print('dict Else', dict)

# Display the final output containing indices of matching pairs
print(output)
import sys

def findSingleton(start, end):
    middle = (start + end) // 2

    if len(nums) == 1:
        print(nums[0])
    # if duplicate is on the left of middle
    elif middle > 0 and nums[middle] == nums[middle - 1]:
        if (middle - 1) % 2 != 0:
            return findSingleton(start, middle - 2)
        else:
            return findSingleton(middle + 1, end)

    #if duplicate is on the right of middle
    elif middle < (len(nums) - 1) and nums[middle] == nums[middle + 1]:
        if (end - (middle + 1)) % 2 != 0:
            return findSingleton(middle + 2, end)
        else:
            return findSingleton(start, middle - 1)
    else:
        return nums[middle]

#----------------------------------------------------------------

if len(sys.argv) != 2:
    print("Missing unique list file.")
    sys.exit(1)

filename = sys.argv[1]

nums = []

with open(filename, 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)

startIndex = 0
endIndex = len(nums) - 1

print(findSingleton(startIndex, endIndex))



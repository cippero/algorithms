# twoSum takes an array and a target sum and returns a pair that make up that sum or False

def twoSum(nums, target):
  pairs, current = [], None
  while nums:
    try: 
      current = pairs.index(nums[0])
      if pairs[current] in pairs:
        pairs.append(nums.pop(0))
        return ([current, len(pairs)-1])
      else: pairs.append(target-nums.pop(0))
    except ValueError: pairs.append(target-nums.pop(0))
  return False


print(twoSum([2,8,7,15],9))
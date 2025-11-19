# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# use object to store complimentary numnbers and indexes, { c:i, ...}
# loop through array and 
# use target - currentNumber and check if the compliment has been seen, if so return tuple
#  
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
#

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#
def pair_sum(numbers, target_sum):
  compliment = {}

  for i in range(len(numbers)):
    target = target_sum - numbers[i]
    if target in compliment:
      return (compliment[target], i)
    else:
      compliment[numbers[i]] = i
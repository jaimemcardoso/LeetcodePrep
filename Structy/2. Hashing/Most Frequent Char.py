# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# map through using hashmap, to get frequencies then map again and get most_frrequent char
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#  O(N)

def most_frequent_char(s):
  pass # todo
  counter = {}
  for char in s:
    counter[char] = counter.get(char, 0) + 1
    
  mostFrequent = s[0]
  
  for key in counter:
    if counter[key] > counter[mostFrequent]:
      mostFrequent = key
  return mostFrequent
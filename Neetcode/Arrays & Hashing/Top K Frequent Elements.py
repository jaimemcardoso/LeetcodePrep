# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# Brute force: we can use a counter and then loop through that k times finding max k items
# then append those keys to a result array
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
#
#
# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
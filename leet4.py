from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Mapping charCount to List of Anagrams

        for word in strs:
            count = [0] * 26  # Initialize the count of each character

            for char in word:
                count[ord(char) - ord("a")] += 1

            # Use the character count as a key
            anagrams[tuple(count)].append(word)

        return list(anagrams.values())  # Return the grouped anagrams as a list

# Example usage
# solution = Solution()
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(solution.groupAnagrams(strs))

"""
Day 03 - Coding Challenges (from m01-coding-questions.pdf)
"""

def two_sum(nums: list, target: int) -> list:
    """Challenge 4: O(n) Two Sum implementation using hash map."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def group_anagrams(strs: list) -> list:
    """Challenge 5: Groups anagrams together."""
    anagram_map = {}
    for s in strs:
        sorted_key = "".join(sorted(s))
        anagram_map.setdefault(sorted_key, []).append(s)
    return list(anagram_map.values())

def transpose_matrix(matrix: list) -> list:
    """Challenge 6: Transposes a 2D matrix."""
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

if __name__ == "__main__":
    print("Two Sum ([2, 7, 11, 15], target=9):", two_sum([2, 7, 11, 15], 9))
    print("Group Anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    mat = [[1, 2, 3], [4, 5, 6]]
    print("Transpose:", transpose_matrix(mat))

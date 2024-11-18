from typing import List, Dict


class Solution:
    def __init__(self, data: List[str]):
        self.data = data

    def group_anagrams(self)->Dict:
        anagram_map: Dict = {}

        for item in self.data:
            sorted_str = ''.join(sorted(item))
            if sorted_str in anagram_map.keys():
                anagram_map[sorted_str].append(item)
            else:
                anagram_map[sorted_str] = [item]
        else:
            return anagram_map


if __name__ == "__main__":
    data = ['on', 'tar', 'rat', 'art', 'no']
    obj = Solution(data)
    print(obj.group_anagrams())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        # for s in strs:
        #     hash_str = {}
        #     for char in s:
        #         if char not in hash_str:
        #             hash_str[char] = hash_str.get(char, 0) + 1

        # hash_str = count_char(s)

        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)
            
            if key not in groups:
                groups[key] = []
            groups[key].append(s)


        return list(groups.values())
        
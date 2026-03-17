class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 매 단어마다 딕셔너리를 만들어 두기
        dictionary = []
        for word in strs:
            char_count = {char: word.count(char) for char in word}
            dictionary.append(char_count)

        # 단어를 순회하면서 일치하는 딕셔너리가 있는지 확인해보기?
        result = []
        for i in range(len(strs)):
            group = []
            if strs[i] not in group:
                group.append(strs[i])
            for j in range(i+1, len(strs)):
                if dictionary[i] == dictionary[j]:
                    group.append(strs[j])
            result.append(group)
        return result


solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))

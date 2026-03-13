"""
A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
"""

# 덩어리로 나눈다 -> 어떻게? /로 split?

# .. -> 이전에 있던 것을 하나 지운다 (결과에 push 했던 것을 pop 한다)
# . -> 이것 자체를 지운다 (pop 결과를 결과에 push를 안 한다)
# 연속된 / -> 한 개만 남기고 결과에 push한다

# 맨 마지막에 오는 하나 또는 연속된 / -> 없앤다


# ///......../a/../b/c/../d/./ / / / / / / -> /......../b/d
# ["", "", "", "........", "a", "..", "b", "c", "..", "d", ".", "", "", "", "", "", "", ""]
# / -> /
# . -> /

class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path = []
        path = path.split('/')[::-1]
        while len(path) != 0:
            directory = path.pop()
            if directory == "":
                continue
            elif directory == ".":
                continue
            elif directory == "..":
                if simplified_path:
                    simplified_path.pop()
                else:
                    continue
            else:
                simplified_path.append(directory)

        if not simplified_path:
            return "/"
        else:
            return "/" + "/".join(simplified_path)
        
solution = Solution()
path = "/.../a/../b/c/../d/./"
print(solution.simplifyPath(path))
        
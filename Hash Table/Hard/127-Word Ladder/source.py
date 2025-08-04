from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        relationMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                relationMap[pattern].append(word)
        visitedVertex = set([beginWord])
        BFS_vertices = deque([beginWord])
        level = 1
        while BFS_vertices:
            for i in range(len(BFS_vertices)):
                word = BFS_vertices.popleft()
                if word == endWord:
                    return level
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighborWord in relationMap[pattern]:
                        if neighborWord not in visitedVertex:
                            visitedVertex.add(neighborWord)
                            BFS_vertices.append(neighborWord)
            level += 1
        return 0


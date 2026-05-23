class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def countSubs(self, s):
        # code here
        # returning the count of the substrings
        # naive approach will be using two for loops and iterating over and counting them
        # and add a set ds to store the unique occurances !
        # uniq_occ=set()
        # for i in range(len(s)):
        #     str=""
        #     for j in range(i,len(s)):
        #         str=str+s[j]
        #         uniq_occ.add(str)
        # count=len(uniq_occ)
        # return count
        # time complexity is O(n^2) *log(M) wjere M is the size of the string

        # Approach 2 usign the Trie Node
        count = 0
        root = TrieNode()
        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    node.children[s[j]] = TrieNode()
                    count = count + 1
                node = node.children[s[j]]
        return count

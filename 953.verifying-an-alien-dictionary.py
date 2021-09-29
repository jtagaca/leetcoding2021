#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # what empty input 
        # string
        # true false 
        # 
        
        #hashtable?
        #asking me 
        # frequency 
        # looking up if the differing character at word 1 and word 2 are sorted in our map
        # differing character is different
        # we look up the differing character in the hashmap
        # compare the indexes 
        # if ever the index of the character at word 1 is> word2 character 2 index 
        # return False 
        # .len of iterator is the same as the len of word2 but word 1 is still not finished 
        #  ["hello","leetcode"]
        #Build map 
        #O(N*W) where n is the len of the words and w is the max char of a word 
        # O(1) because we always have O(26) in our hashmap
         #["apple","app"],
        hashm={c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            word1,word2=words[i], words[i+1]
            for cIDX in range(len(word1)):
                if cIDX==len(word2):
                    return False
                if word1[cIDX]!=word2[cIDX]:
                    if hashm[word1[cIDX]]>hashm[word2[cIDX]]:
                        return False
                    break
        return True 
                
        
        
        
        
        
        
# @lc code=end


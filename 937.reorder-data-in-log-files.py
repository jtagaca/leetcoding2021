# @before-stub-for-debug-begin
from python3problem937 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letlog = []
        digitlog = []
        # we determined if it is a digit log or letter log by checking of the second
        # position is a digit and then  we do not need to sort it
        # other wise we break it down
        # and we sort it by the first index
        # sort by second and third
        for log in logs:
            if log.split()[1].isdigit():
                digitlog.append(log)
            else:
                letlog.append(log.split())
        # sorted using the first letter to the end letter
        #sorting by word and if word is the same we sord by letter 
        letlog.sort(key=lambda x: x[0])
        
        # sorted using the next letter until the end
        # same thing but we sort here first since ↑ because we are 
        # removing the need to presort if all of the letters are the same since the top sorted the 
        # words alphabetically
        letlog.sort(key=lambda x: x[1:])

        for i in range(len(letlog)):
            letlog[i] = (" ".join(letlog[i]))
        letlog.extend(digitlog)
        return letlog

# @lc code=end

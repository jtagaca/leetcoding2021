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
        letlog.sort(key=lambda x: x[0])
        # sorted using the next letter until the end
        letlog.sort(key=lambda x: x[1:])

        for i in range(len(letlog)):
            letlog[i] = (" ".join(letlog[i]))
        letlog.extend(digitlog)
        return letlog

# @lc code=end

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = 0
        abbr_idx = 0
        count = 0
        
        #Time/Space Complexity
        #Time: O(N), where N = len of abbreviation
        #Space: O(1)
        # we are dependent on abbreviation word  
        # we are using this for bounds we will always have 1 more iteration 
        while abbr_idx < len(abbr) and word_idx < len(word):
            # # checking if it's a digit as well as if it's a leading 0 
            if abbr[abbr_idx].isdigit() and abbr[abbr_idx] != '0':
                # updating the start 
                start = abbr_idx
                # checking if the current is a digit until it is not a digit 
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    abbr_idx += 1
                # we will have extra +1 after the above since we have had the +1
                # we are just casting count here 
                count = int(abbr[start:abbr_idx])
                # we keep going and if ever count still has some value and we are already at the last index of word 
                # then we know that it is not posible 
                while count > 0 and word_idx < len(word):
                    word_idx += 1
                    count -= 1
                # we just check if they are not the same 
            else:
                if abbr[abbr_idx] != word[word_idx]:
                    return False
                # updating
                word_idx += 1
                abbr_idx += 1
                # checking if the idx value is the same as the since the the idx will always have +1
                # values as well as the abbr_idx 
        return word_idx == len(word) and abbr_idx == len(abbr) and count == 0

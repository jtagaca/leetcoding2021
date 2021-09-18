class Solution:
    def intToRoman(self, num: int) -> str:
        # hashmap problem?
        # if remainder is 40 then we need the smaller to the left than to the right
        # IX
        # order matters
        # if 4 or 9?

        hashm : {
            'I' : 1,
            'IV':4,
            'V' : 5,
            'IX':9,
            'X' : 10,
            'XL':40,
            'L' : 50,
            'XC':90,
            'C' : 100,
            'CD':400,
            'D' : 500,
            'CM':900,
            'M' : 1000
        }
        copy=num
        temp=[]
        for key, value in reversed(hashm.items()):
            while copy>0:
                if copy>=value:
                    temp.append(key)
                    copy-=value
                else:
                    break
        return ("").join(temp)
                    

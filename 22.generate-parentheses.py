class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if len of tempString is n*2
        # openParent count 
        # close parenthesis count 
        # if open is n and close is n 
        # open < n 
        # close < open 
        
        result =[]
        # this will have a time of O(2^n) and this will have a space of 
        # O(n*2)
        stack=[]
        def backtrack(openp,closep,stack ):
            nonlocal n

            if openp==n and closep==n:
                tempStr=("").join(stack)
                result.append(tempStr)
                return
            if openp < n:
                stack.append("(")
                backtrack(openp+1, closep,stack)
                # after we have explored it we then just removed it and move on 
                stack.pop()
            # after the first add this will never run because we popped the ( on the first 
            # and open p = 0 and close p = 0 ↓
            if closep < openp:
                stack.append(")")
                # after we have explore we just remove it 
                backtrack(openp, closep+1,stack)
                stack.pop()
        # 0,0 works because our call will 
        backtrack(0,0,stack)
        
        return result 
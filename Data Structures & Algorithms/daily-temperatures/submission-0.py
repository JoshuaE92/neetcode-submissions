class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ret=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if(not stack):
                stack.append(i)
            else:
                if temperatures[i]<=temperatures[stack[-1]]:
                    stack.append(i)
                else:
                        while stack and temperatures[i]>temperatures[(stack[-1])]:
                            compare=stack.pop()
                            ret[compare]=i-compare
                        stack.append(i)
        return ret


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=["+","-","*","/"]
        for c in tokens:
            if c in op:
                if c=="+":
                    val1=(stack.pop())
                    val2=(stack.pop())
                    stack.append(val1+val2)
                if c=="-":
                    val1=(stack.pop())
                    val2=(stack.pop())
                    stack.append(val2-val1)
                if c=="/":
                    val1=(stack.pop())
                    val2=(stack.pop())
                    stack.append(int(val2/val1))
                if c=="*":
                    val1=(stack.pop())
                    val2=(stack.pop())
                    stack.append(val1*val2)
            else:
                stack.append(int(c))
        return stack[-1]
            
        

        
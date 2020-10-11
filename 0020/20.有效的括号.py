class Solution():
    def isValid(self, s):
        if len(s) % 2 == 1:#首先判断是不是单数字符串
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:#遍历字符串
            if ch in pairs:#遇到后括号执行if
                if not stack or stack[-1] != pairs[ch]:
                #如果这个时候stack为空，说明第一个遇到的是后括号，不符合题意，返回false；如果stack中最后一个与这个后括号对应的前括号不相同，说明顺序有问题，不符合题意，返回false。
                    return False
                stack.pop()#如果这个后括号满足题意，把之前添加的这个后括号对应的前括号从最后一位删掉
            else:
                stack.append(ch)#每次遍历遇到前括号的时候加在stack的最后面
        
        return not stack

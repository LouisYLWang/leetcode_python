#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#
class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf") 


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x
        

    def pop(self):
        """
        :rtype: None
        """
        top = self.stack.pop()
        if top == self.min:
            #print(self.stack)
            temp_stack = MinStack()
            for i in self.stack:
                #print(temp_stack.stack)
                temp_stack.push(i)
                #print(temp_stack.getMin())
            self.min = temp_stack.getMin()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


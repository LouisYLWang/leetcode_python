#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        self.stack2 = list()
        for i in self.stack1[::-1]:
            self.stack2.append(i)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        peek = self.stack2.pop()
        self.stack1 = list()
        for i in self.stack2[::-1]:
            self.stack1.append(i)
        return peek

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.num = []
        def itrator(nestedList):
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    self.num.append(nestedList[i].getInteger())
                else:
                    itrator(nestedList[i].getList())
        itrator(nestedList)
        self.idx = 0
        print(self.num)
    def next(self) -> int:
        cur = self.num[self.idx]
        self.idx += 1
        return cur 
    def hasNext(self) -> bool:
        return True if self.idx < len(self.num) else False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
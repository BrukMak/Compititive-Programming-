"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        di = {}
        for index in range(len(employees)):
            di[employees[index].id] = index
        print(di)
        tot_importance = 0
        def dfs(node):
            nonlocal tot_importance
            tot_importance += node.importance
            for sub in node.subordinates:
                dfs(employees[di[sub]]) 
                
        dfs(employees[di[id]])  
        return tot_importance
                
            
            

            

            
        

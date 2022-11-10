#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
from collections import defaultdict
def graphColoring(graph, k, V):
    
    #your code here
    
    
    color = [0] * V
    if coloring(0, graph, color, k, V):
        return 1
    return 0
    
def coloring(node, graph, color, M, N):
    if node == N:
        return True
      
    for clr in range(1, M+1):
        if isSafe(node, clr, graph, color):
            color[node] = clr
            if coloring(node + 1, graph, color, M, N):
                return True
            color[node] = 0
    return False
def isSafe(node, clr, graph, color):
    for i, v in enumerate(graph[node]):
        if v and color[i] == clr:
            return False
    return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
#User function Template for python3

class Solution:
    #Heapify function to maintain heap property
    def getLeftChild(self, i):
        return 2*i + 1
    def getRightChild(self, i):
        return 2*i + 2
    def getParent(self, i):
        return (i - 1)/2
    #Insert
    def insert(self, arr,val):
        arr.append(val)
        i = len(arr)-1
        while arr[getParent(i)] > val:
            i = self.getParent(i)
            swap(arr[i],val)
            
    #Remove
    def remove(self,arr,indx):
        arr[indx], arr[len(arr)-1] = arr[len(arr) -1] , arr[indx]
        arr.pop(-1)
        self.heapify(arr,len(arr), indx)
    
    #Update
    def update(self,arr,indx,val):
        arr[indx] = val
        heapify(arr,len(arr),indx)
    
    #getMin
    
    def getMin(self, arr):
        
        # self.remove(arr,0)
        return arr[0]
    
    def swap(self, i, j,arr):
        arr[i], arr[j] = arr[j] ,arr[i]
    
    def isleaf(self, indx, n):
        return (indx + 1)*2 > n
        
    def heapify(self,arr, n, i):
        cur = i 
        l = self.getLeftChild(i)
        r = self.getRightChild(i)
        
        if l < n and arr[l] < arr[i]:
            i = l
        if r < n and arr[r] < arr[i]:
            i = r
        
        if i != cur:
            arr[i], arr[cur] = arr[cur] , arr[i]
            self.heapify(arr,n,i)
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(len(arr)-1,-1,-1):
            self.heapify(arr,n,i)
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(len(arr) - 1, -1,-1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr,i,0)
        arr.reverse()
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends

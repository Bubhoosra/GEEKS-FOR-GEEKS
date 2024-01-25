#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # print(W)
        v=[]
        w=[]
        s=[]
        d={}
        for i in range(n):
            p=arr[i]
            v.append(p.value)
            w.append(p.weight)
            s.append(p.value/p.weight)
            r=(p.value/p.weight)
            d[i]=r
        k=sorted(d.items(), key=lambda item: item[1],reverse=True)
        
        # print(k)
        # for i in d:
        #     k.append(d[i])
        # print(k)
        s=sorted(s)
        # print(s)
        # k=k[::-1]
        # print(k)
        p=0
        c=-1
        # print(s)
        # return 240.000000
        n=len(k)
        for i in range(n):
            j=k[i][0]
            if W>0 and arr[j].weight<=W:
                W-=arr[j].weight
                p+=arr[j].value*(1.000000)
                c=j
            else:
                break
        # print(p,j)
        if(W>0 and j<n and j!=c):
            p+=(arr[j].value)*(W/arr[j].weight)
        # print(p)
        return p
            
            
        
        # print(arr)
        # return 240.000000
    
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends
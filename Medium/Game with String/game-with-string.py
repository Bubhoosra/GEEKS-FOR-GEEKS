#User function Template for python3

class Solution:
    def minValue(self, s, k):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        
        for i in d:
            l.append(d[i])
        if k==0:
            res=0
            for i in l:
                res+=(i**2)
            return res
        # l=sorted(l)
        j=0
        while(True):
            
            x=max(l)
            z=l.index(x)
            l[z]-=1
            j+=1
            if j==k:
                break
        res=0
        for i in l:
            res+=(i**2)
        return res
            
        # d1={}
        # for i in d:
        #     if d[i] not in d1:
        #         d1[d[i]]=1
        #     else:
        #         d1[d[i]]+=1
        # # for i in d:
        # #     d[i]-=k
        # d=dict(sorted(d1.items(), key=lambda item: item[1],reverse=True))
        # x=0
        # j=1
        # s=1
        
        
        # for i in d:
        #     x=d[i]-1
        #     j+=1
        #     if x not in d:
        #         d[i]=1
        #     else:
        #         d[x]+=1
        #     if j==k:
        #         break
        # res=0
        # for i in d:
        #     res+=(d[i]**2)
        # return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends
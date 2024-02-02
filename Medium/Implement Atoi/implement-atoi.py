#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        k="1234567890"
        c=0
        p=""
        for i in s:
            if i=="0" and c==0:
                continue
                
            elif i in k:
                c=1
                p+=i
            elif i=="-" and c==0:
                p+=i
            else:
                return -1
        if len(p)==0 or (len(p)==1 and p=="-"):
            return 0
        return int(p)
        # Code here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
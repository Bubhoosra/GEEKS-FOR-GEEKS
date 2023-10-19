#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        s=""
        p=""
        for i in S:
            if i not in s:
                s+=i
            else:
                if len(p)<len(s):
                    p=s
                z=""
                c=0
                s+=i
                for j in range(len(s)):
                    if i==s[j]:
                        c=j
                        break
                        
                for k in range(c+1,len(s)):
                    z+=s[k]
                
                s=z
        if len(p)<len(s):
            p=s
        if len(p)==0:
            return len(s)
                    
        return len(p)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends
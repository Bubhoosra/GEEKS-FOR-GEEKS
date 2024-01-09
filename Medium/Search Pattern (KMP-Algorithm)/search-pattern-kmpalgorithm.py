#User function Template for python3

class Solution:
    def search(self, pat, txt):
        l=[]
        for i in range(len(txt)):
            if txt[i]==pat[0]:
                n=len(pat)
                if n+i<=len(txt) and txt[i:n+i]==pat:
                    l.append(i+1)
        # print(l)
        return l
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends
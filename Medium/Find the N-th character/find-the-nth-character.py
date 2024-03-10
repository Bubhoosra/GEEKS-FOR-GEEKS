#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        
        i=0
        while(r>0):
            r-=1
            i=0
            q=""
            while(i<len(s)):
                if s[i]=="1":
                    q+="10"
                elif s[i]=="0":
                    q+="01"
                i+=1
            
            s=q[:n+1]
        return  s[n]
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends
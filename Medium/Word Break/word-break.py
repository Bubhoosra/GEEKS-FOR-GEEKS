#User function Template for python3

class Solution:
    def wordBreak(self, n, s, d):
        l=[]
        x=s[0]
        for i in d:
            if i[0]==x:
                l.append(i)
        while(len(l)>0):
            n=l.pop()
            if n==s:
                return True
            j=0
            c=0
            for i in n:
                if i==s[j]:
                    j+=1
                else:
                    c=1
                    break
            if c==0:
                y=len(n)
                x=s[y]
                for i in d:
                    if i[0]==x:
                        l.append(n+i)
        return False
                
            
            
        # Complete this function


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends
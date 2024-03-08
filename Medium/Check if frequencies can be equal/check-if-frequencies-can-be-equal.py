#User function Template for python3
class Solution:
    def sameFreq(self, s):
        D={}
        for i in s:
            if i not in D:
                D[i]=1
            else:
                D[i]+=1
        m=set()
        c=0
        for i in D:
            m.add(D[i])
        l=list(m)
        if len(l)>2:
            return False
        
        
        if len(l)==1:
            return True
        l=sorted(l)
        m1=0
        m2=0
        for i in D:
            if l[0]==D[i]:
                m1+=1
            else:
                m2+=1
        if m1==1 and l[0]==1:
            return True
        if l[1]-l[0]==1 and (m2==1):
            return True
        return False
            
        
            
            
        # return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends
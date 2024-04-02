#User function Template for python3
class Solution:
	def NBitBinary(self, n):
	    k=0
	    res=0
	    ans=[]
	    while(k<n):
	        res+=(2**k)
	        k+=1
	    
	    for i in range(res,0,-1):
	       
	        p=bin(i)
	        p=p.replace("0b","")
	        c=0
	        s=""
	        one=0
	        zero=0
	        for j in p:
	            s+=j
	            if j=="1":
	                one+=1
	            else:
	                zero+=1
	            if one<zero:
	                c=1
	                break
	        
	        if len(p)==n and c==0:
	            ans.append(p)
	    return ans
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends
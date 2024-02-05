#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        if head==None:
            temp1=Node(data)
            temp1.next=temp1
            return temp1
        d={}
        temp=head
        # for starting
        if data<=temp.data:
            temp1=Node(data)
            temp1.next=head
            while(temp.next!=head):
                temp=temp.next
            temp.next=temp1
            head=temp1
            # print(temp.data)
            return head
        else:
            temp=head
            while(temp.next!=head):
                if data<=temp.data:
                    temp1=Node(data)
                    prev.next=temp1
                    temp1.next=temp
                    return head
                prev=temp
                temp=temp.next
            if(temp.data<=data):
                temp1=Node(data)
                temp.next=temp1
                temp1.next=head
                return head
            elif prev.data<=data:
                temp1=Node(data)
                prev.next=temp1
                temp1.next=temp
                return head
            
        
        # for mid
        
        

#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        data=int(input())

        cll=LinkedList()
        for e in arr:
            cll.push(e)
            
        reshead=Solution().sortedInsert(cll.head,data)
        printList(reshead)
        print()
        


# } Driver Code Ends
"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def rearrange(self, head):
        temp=head
        c=1
        even=[]
        odd=[]
        while(temp!=None):
            if c%2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            c+=1
            temp=temp.next
        # print(c)
        even=even[::-1]
        # print(odd)
        l=odd+even
        # print(l)
        temp=head
        i=0
        while(temp!=None):
            temp.data=l[i]
            i+=1
            temp=temp.next
            
        # Code here


#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
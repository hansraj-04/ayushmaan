# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None   
# class SLL:
#     def __init__(self):
#         self.head = None  

#     def Insert_at_begin(self, data):
#         new_node = node(data)
#         new_node.next = self.head 
#         self.head = new_node       

#     def Insert_at_end(self, data):
#         new_node = node(data)
#         if self.head is None:       
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:        
#                 temp = temp.next
#             temp.next = new_node

#     def display(self):
#         if self.head is None:
#             print("List is empty")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data, end=" → ")
#                 temp = temp.next
#             print("None")

# sll = SLL()
# sll.Insert_at_begin(15)
# sll.Insert_at_begin(10)
# sll.Insert_at_begin(5)
# sll.Insert_at_end(20)
# sll.Insert_at_end(25)

# sll.display()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SLL:
#     def __init__(self):
#         self.head = None

#     def insert_end(self, data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new

#     def insert_at_position(self, data, pos):
#         new = Node(data)
#         if pos == 1:
#             new.next = self.head
#             self.head = new
#             return
#         temp = self.head
#         for _ in range(pos - 2):
#             if not temp:
#                 print("Position out of range")
#                 return
#             temp = temp.next
#         new.next = temp.next
#         temp.next = new

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" → ")
#             temp = temp.next
#         print("None")

# s = SLL()
# s.insert_end(10)
# s.insert_end(20)
# s.insert_end(30)
# s.display()

# s.insert_at_position(15, 2)  
# s.display()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SLL:
#     def __init__(self):
#         self.head = None

#     def insert_end(self, data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new

#     def traverse(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" → ")
#             temp = temp.next
#         print("None")

# s = SLL()
# s.insert_end(10)
# s.insert_end(20)
# s.insert_end(30)

# s.traverse()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SLL:
#     def __init__(self):
#         self.head = None

#     def insert_end(self, data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new

#     def delete_begin(self):
#         if self.head:
#             print("Deleted:", self.head.data)
#             self.head = self.head.next

#     def delete_end(self):
#         if not self.head:
#             print("List empty")
#         elif not self.head.next:
#             print("Deleted:", self.head.data)
#             self.head = None
#         else:
#             temp = self.head
#             while temp.next.next:
#                 temp = temp.next
#             print("Deleted:", temp.next.data)
#             temp.next = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" → ")
#             temp = temp.next
#         print("None")

# # --- Test ---
# s = SLL()
# s.insert_end(10)
# s.insert_end(20)
# s.insert_end(30)
# s.display()

# s.delete_begin()
# s.display()

# s.delete_end()
# s.display()


# class SLL:
#     def deletion_at_begning(self):
#         temp.next=None
#     def deletion_at_end(self):
#         print()
#         prev=self.head
#         temp=self.head.next
#         while temp.next:
#             prev=temp
#             temp=temp.next
#         prev.next=None


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SLL:
#     def __init__(self):
#         self.head = None

#     def insert_end(self, data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new

#     def insert_at_position(self, data, pos):
#         new = Node(data)
#         if pos == 1:
#             new.next = self.head
#             self.head = new
#             return
#         temp = self.head
#         for _ in range(pos - 2):
#             if not temp:
#                 print("Position out of range")
#                 return
#             temp = temp.next
#         new.next = temp.next
#         temp.next = new

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" → ")
#             temp = temp.next
#         print("None")



# s = SLL()
# s.insert_end(10)
# s.insert_end(20)
# s.insert_end(30)
# s.display()

# s.insert_at_position(15, 2)  
# s.display()






# def insert_end(self, data):
#         new = Node(data)
#         if not self.head:
#             self.head = new
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new

    

#     def sum_all_nodes(self):
#         total = 0
#         temp = self.head
#         while temp:
#             total += temp.data
#             temp = temp.next
#         return total



# def sum_even_data(self):
#         total = 0
#         temp = self.head
#         while temp:
#             if temp.data % 2 == 0:
#                 total += temp.data
#             temp = temp.next
#         return total


# def count_nodes(self):
#         count = 0
#         temp = self.head
#         while temp:
#             count += 1
#             temp = temp.next
#         return count

# def sum_all(self):
#      s=0
#      temp=self.head
#      while temp!=None:
#             s+=temp.data
#             temp=temp.next
#         print(s)


# def count_all(self):
#     c=0
#     temp=self.head
#     while temp!=None:
#         c+=1
#         temp=temp.next
#     print(c)

# def sum_even(self):
#      t=self.head
#      s=0
# while t!=None:
#             if t.data%2==0:
#                 s+=t.data
#             t=t.next
#             print(s)

# def sum_even_nodes(self):
#      t=self.head
#      s=0
#      pos=1
#      while t!=None:
#             if pos%2==0:
#                 s+=t.data
#             t=t.next
#             pos+=1


# def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # Use two pointers: slow and fast
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next          # move slow by 1 step
#             fast = fast.next.next     # move fast by 2 steps

#             if slow == fast:          # if they meet, cycle exists
#                 return True

#         return False 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head

#         while curr:
#             nxt = curr.next     # store next node
#             curr.next = prev    # reverse the link
#             prev = curr         # move prev forward
#             curr = nxt          # move curr forward

#         return prev   # prev will be the new head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
#         second = dummy

     
#         for _ in range(n + 1):
#             first = first.next

        
#         while first:
#             first = first.next
#             second = second.next

       
#         second.next = second.next.next

#         return dummy.next


# class Node:
#     def __init__(self, data):
#         self.val = data
#         self.left = None
#         self.right = None


# def inorder(root):
#     if root is None:
#         return
#     inorder(root.left)
#     print(root.val, end=" ")
#     inorder(root.right)


# def preorder(root):
#     if root is None:
#         return
#     print(root.val, end=" ")
#     preorder(root.left)
#     preorder(root.right)


# def postorder(root):
#     if root is None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.val, end=" ")


# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(2)
# root.left.right = Node(8)
# root.right.left = Node(15)
# root.right.right = Node(25)
# root.left.left.left = Node(1)

# print("Inorder: ")
# inorder(root)
# print("\nPreorder: ")
# preorder(root)
# print("\nPostorder: ")
# postorder(root)



# class Node:
#     def __init__(self, data):
#         self.val = data
#         self.left = None
#         self.right = None


#     def levelorder(root):
#        if root is None:
#         return
#        q = deque([root])
#        while q:
#         node = q.popleft()
#         print(node.val, end=" ")
#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)



# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(2)
# root.left.right = Node(8)
# root.right.left = Node(15)
# root.right.right = Node(25)
# root.left.left.left = Node(1)

# print("Level Order: ")
# levelorder(root)

# def sum_Of_Nodes(root):
#     if root is None:
#         return 0
#     return root.val + sum_Of_Nodes(root.left) + sum_Of_Nodes(root.right)

# def sum_Of_even_Nodes(root):
#     if root is None:
#         return 0
#     even_sum = root.val if root.val % 2 == 0 else 0
#     return even_sum + sum_Of_even_Nodes(root.left) + sum_Of_even_Nodes(root.right)

# def height(root):
#     if root is None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))



#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None

#         if root == p or root == q:
#             return root

#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)

#         if left and right:
#             return root
#         return left if left else right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:
        #     return None

        # if root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        # return left if left else right

# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
#         g.sort()
#         s.sort()
#         i = j = 0
#         while i < len(g) and j < len(s):
#             if g[i] <= s[j]:
#                 i += 1
#             j += 1
#         return i

# Security Key
# import collections

# def find_security_key(data: int) -> int:
#     if data < 0:
#         data = abs(data)
    
#     if data == 0:
#         return -1

#     s_data = str(data)

#     digit_counts = collections.Counter(s_data)

#     security_key = 0
    
#     for digit, count in digit_counts.items():
#         if count > 1:
#             security_key += 1  

    
#     if security_key == 0:
#         return -1
#     else:
#         return security_key

# print(f"Security key for 12345: {find_security_key(12345)}")
# print(f"Security key for 11223: {find_security_key(11223)}")  
# print(f"Security key for 77897: {find_security_key(77897)}") 
# print(f"Security key for 0: {find_security_key(0)}")        
# print(f"Security key for 555: {find_security_key(555)}")     
# print(f"Security key for 121314: {find_security_key(121314)}") 

# encode as a number
# data,digit=map(int,input().split(" "))
# a=str(data)
# b=str(digit)
# c=0
# for i in a:
#     if i==b:
#         c+=1
# print(c)

# sum of adjacent digits
# def findTotalDistance(n,arr):
#     total_distance=0
#     for i in range(n-1):
#         distance=abs(arr[i]-arr[i+1])
#         total_distance+=distance
#     return total_distance


# odd even 
# l=[10,98,3,33,12,22,21,11]
# l1=[]
# l2=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# l3=l1+l2
# print(l3)

# secret message agency

# import math
# def count_square_plots(numOfPlots,areas):
#     count = 0
#     for area in areas:
#         side_length = math.isqrt(area)
#         if side_length * side_length == area:
#             count += 1
#     return count


# vals =[-10,-7,-3,4,2]
# vals.sort()
# prod1=vals[-1]*vals[-2]
# prod2=vals[0]*vals[1]
# if prod2>prod1:
#     print(vals[0]+vals[1])
# else:
#     print(vals[-1]+vals[-2])



# ch='D'
# k=3
# lower='abcdefghijklmnopqrstuvwxyz'
# upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# if ch in lower:
#     idx=lower.index(ch)
#     out=lower[(idx+k)%26]
# elif ch in upper:
#     idx=upper.index(ch)
#     out=upper[(idx+k)%26]
# else:
#     out=ch
# print(out)

# pooled cab services
# def find_employees_in_range(input_string):
    
#     parts = list(map(int, input_string.split(',')))
    
#     N = parts[0]  
#     employee_distance = parts[1:N+1]  
#     lower_bound = parts[N+1]  
#     upper_bound = parts[N+2]  
    
#     employees_in_range = []
#     for distance in employee_distance:
#         if lower_bound <= distance <= upper_bound:
#             employees_in_range.append(distance)
    
#     return employees_in_range

# input_data = "6,30,50,29,38,12,48,39,55"
# result = find_employees_in_range(input_data)
# print(result)

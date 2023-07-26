NAME:DOSUNMU OLAMIDE DEBORAH
MATRIC NUMBER:125/21/2/0072
DEPARTMENT:STATISTICS
COURSE:CSC 204 
        

## create single linked list class in package linkedlists
"""
  Test with this[1,3,4,5,6,7,8,9,2,22,15,55,45,23,24,26,28]
  (Hint : Create insert and display methods first then other list operation)
  """
  class SinglyLinkedList:
  def_init_(self):
  self.head = None

  def insert(self, data):
  new_node = Node(data) ## Making use of the node class created in question 1i
if self.head is None:
self.head =new_node
  else:
     current = self.head
     while current.next_node:
      current=current.next_node
      current.next_node = new_node

      def display(self):
        elements = []
        current= self.head
        while current:
           elements.append(str(current.data))
           current=current.next_node
           print  (" ".join(elements)) 
#Test with the given data
data_list= [1,3,4,5,6,7,8,7,9,2,22,15,5545,23,24,26,28]
Linked_list= SinglyLinkedList()

for data in data_list:
Linked_list.insert(data)

Linked_list.display()




## Method to display the minimum data in the single linked
 min_data = current.data
 while current.next_node:
 if current.data < min_data:
 min_data = current.data
 current= current.next_node
 return min_data

## Method to display the maximum data in the single linked list
 def display_max(self):
 current = self.head
 if(current is None):
 return current

 max_data = current.data
 while current.next_node:
 if current.data > max_data:
 max_data = current.data
 current= current.next_node
 return max_data


 
   
def to_list(self):# Convert the single linked list into a python list
data_list =[]
current= self.head
while current:
      data_list.append(current.data)
      current=current.next_node
      return data_list

def Convert_to_bst(self, data_list): # convert the data_list to a binary search tree
# data_list = self.to_list()
# data_list.sort() # Ensure the list is sorted
if not data_list:
    return None

    mid_point= len(data_list) // 2 # Floor division of the len of the data_list
    root_data = data_list[mid_point]# The mid-data will be the root data of the bst
    root=BSTNode(root_data)#Create a new node using the BSTNode class

    root.left=self.convert_to_bst(data_list[:mid_point])
root.right=self.convert_to_bst(data_list[:mid_point + 1:])

return root

class BSTNode:
    def_init_(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

from single_linked_list import Queue

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a Single Linked List and insert the data
    sll = SingleLinkedList()
    for data in data_list:
        sll.insert(data)

    # Display the Single Linked List
    sll.display()
# Find the maximum and minimum values in the linked list
    max_value = sll.find_max()
    min_value = sll.find_min()
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")

    # Convert the linked list to a binary search tree
    bst_root = sll.convert_to_bst(data_list)

    # In-order traversal of the BST to display the tree
    print("\nBinary Search Tree (In-order traversal):")
    def in_order_traversal(root):
        if root:
            in_order_traversal(root.left)
            print(root.data, end=' ')
            in_order_traversal(root.right)
    in_order_traversal(bst_root)
# Test binary search
    search_value = 22
    index = sll.binary_search(search_value)
    if index != -1:
        print(f"Binary search: {search_value} found at index {index}")
    else:
        print(f"Binary search: {search_value} not found")


# Testing Queueing operations
    queue = Queue()
    for data in data_list:
        queue.enqueue(data)

    print("\nQueue:")
    queue.display()

    print("Dequeue:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()

    queue.sort_queue()
    print("\nSorted Queue:")
    queue.display()

        






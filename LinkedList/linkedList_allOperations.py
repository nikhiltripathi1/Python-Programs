class node:
    def _init_(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    head=None
    def _init_(self):
        self.head = None
    
    # function to add a node at front
    def add_at_front(self, data):
        self.head = node(data=data)  

    # function to check whether the list is empty
    def is_empty(self):
        return self.head == None

    # function to add node at the end
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # function to delete any node
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # function to get the last node
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # function to print the list nodes
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next


s = linked_list()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()

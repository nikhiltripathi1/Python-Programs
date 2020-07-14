class node:
        def __init__(self,data=None,next=None):
                self.data=data
                self.next=next
        def __repr__(self):
                return repr(self.data)
class link_list:
        def __init__(self):
                self.head=None
        def __repr__(self):
                nodes=[]
                curr=self.head
                while curr:
                        nodes.append(repr(curr))
                        curr=curr.next
                return '->'.join(nodes)
        def prepend(self,data):
                self.head=node(data=data,next=self.head)
        def addnode(self,data):
                if not self.head:
                    self.head=node(data=data)
                    return
                curr=self.head
                while curr.next:
                        curr=curr.next
                curr.next=node(data=data)

s=link_list()
s.addnode("hello")
s.addnode("hello")
print(s)

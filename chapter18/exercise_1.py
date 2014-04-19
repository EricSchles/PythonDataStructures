class Node:
    def __init__(self,cargo=None,next=None,prev=None):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print self.cargo,

    def print_forward(self):
        if self.next != None:
            print self.cargo,
            head = self.next
            head.print_forward()
        if self.next == None:
            print self.cargo,

    def __str__(self):
        return str(self.cargo)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_forward(self):
        print "[",
        if self.head != None:
            self.head.print_forward()
        print "]",

    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self,cargo):
        if self.head == None:
            self.addFirst(cargo)
        else:
            node = Node(cargo)
            curr = self.head

            while curr.next != None:
                curr = curr.next    
            prev = curr
            curr.next = node
            curr = curr.next
            curr.prev = prev
                
            self.length += 1

    def remove(self,cargo):
        if self.head == None: return
        curr = self.head
        while curr.cargo != cargo:
            curr = curr.next
        #curr now points to the node we need to delete
        if curr == None: return #didn't find the element
        if curr.next != None:
            next_node = curr.next
            prev_node = curr.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            prev_node = curr.prev
            prev_node.next = None
        

    def print_head(self):
        print self.head

listing = LinkedList()

listing.insert(5)
listing.insert(6)
listing.insert(7)
listing.insert(8)
listing.insert(9)

listing.print_forward()
listing.remove(8)
listing.remove(9)
listing.print_forward()

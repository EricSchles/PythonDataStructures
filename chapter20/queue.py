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

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self,cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            self.head = node
        else:
            last = self.head
            while last.next: last = last.next
            last.next = node
        self.length = self.length +1 

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head   = None
        self.last   = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo

class ListQueue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def insert(self,cargo):
        self.list.insert(0,cargo) 

    def remove(self):
        return self.list.pop()


class PriorityQueue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, item):
        node = Node(item)
        curr = self.head
        if curr == None:
            self.head = node
        else:
            while curr.next != None: curr = curr.next
            prev = curr
            curr.next = node
            curr = curr.next
            curr.prev = prev
        self.length += 1

    def find(self):
        maxi = None
        item = None
        curr = self.head
        while curr != None:
            if curr.cargo > maxi: 
                maxi = curr.cargo
            curr = curr.next
        item = maxi
        return item

    #used for remove only
    def item_return(self,item):
        curr = self.head
        while curr != None:
            if curr.cargo == item:
                return curr
            curr = curr.next

    def remove(self):
        maxi = None
        item = self.find()
        curr = self.item_return(item)
        if curr.next != None and curr.prev != None:
            next_node = curr.next
            prev_node = curr.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        elif curr.next != None and curr.prev == None:
            curr.next = None
        elif curr.next == None and curr.prev != None:
            prev_node = curr.prev
            prev_node.next = None
        else:
            pass
        self.length -= 1
        return item



q = PriorityQueue()
q.insert(11)
q.insert(12)
q.insert(14)
q.insert(13)
while not q.is_empty(): print q.remove()

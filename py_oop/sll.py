class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def printAllVals(self):
        temp = self.head
        while(temp.next != None):
            print temp.value
            temp = temp.next
        print temp.value
    def addBack(self, val):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = Node(val)
    def addFront(self, val):
        new_node = Node(self.head.value)
        new_node.next = self.head.next
        self.head.value = val
        self.head.next = new_node
    def insertBefore(self, nextVal, val):
        if self.head.value == nextVal:
            new_node = Node(self.head.value)
            new_node.next = self.head.next
            self.head.value = val
            self.head.next = new_node
        else:
            temp = self.head
            while (temp.next.value != nextVal):
                temp = temp.next
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
    def insertAfter(self, preVal, val):
        if preVal == self.head.value:
            new_node = Node(val)
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            temp = self.head
            while(temp.value != preVal):
                temp = temp.next
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
    def removeNode(self, val):
        if self.head.value == val:
            if self.head.next == None:
                self.head.value = None
            else:
                self.head = self.head.next
        else:
            temp = self.head
            while(temp.next.value != val):
                temp = temp.next
            temp.next = temp.next.next


list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.addFront(5)
list.insertAfter('Alice', 'Charles')
list.removeNode(5)
list.printAllVals()

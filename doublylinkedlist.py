#------------------------------------------
# helper Node class
#------------------------------------------
class Node(object):
    """
    Each node is a combination of data and a pointer 
    to the next node
    """
    def __init__(self,data = None, next_node = None, previous_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev

    def set_data(self, new_data):
        self.data = new_data

#------------------------------------------
# doublyLinkedList class
#------------------------------------------
class LinkedList(object):
    """
    LinkedList stores the head of the list.
    """

    def __init__(self,head = None):
        self.head = head
        self.length = 0

    def get_length(self):
        return self.length

    # insert front node
    def add(self, data):
        new_node = Node(data)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node
        self.length += 1
        return self.length

    def remove(self, data):
        curr_node = self.head

        while curr_node:
            if curr_node.get_data() == data:
                next = curr_node.get_next()
                prev = curr_node.get_prev()
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.head = curr_node
                self.length -=1
                return True

            else: 
                curr_node = curr_node.get_next()
        return False
# find node
    def find (self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == data:
                return data
            else:
                curr_node = curr_node.get_next()
        return None

myList = LinkedList()
print(myList.add(6))
print(myList.add(8))
print(myList.add(12))
print(myList.remove(8))
print(myList.remove(6))
print(myList.find(12))
print(myList.find(6)) 
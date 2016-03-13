#------------------------------------------
# helper Node class
#------------------------------------------
class Node(object):
    """
    Each node is a combination of data and a pointer 
    to the next node
    """
    def __init__(self,data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_data(self, new_data):
        self.data = new_data

#------------------------------------------
# LinkedList class
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
    def insert_front(self, data):
        if (data == None):
            return False

        new_node = Node(data)
        new_node.set_next(head)
        self.head = new_node
        self.length += 1
        return True

    # remove front
    def remove_front(self):
        if (self.length == 0 ):
            return False

        temp_node = self.head
        self.head = self.head.get_next()
        temp_node.set_next(None)
        self.length -= 1
        return True

    # Insert an element at the end of the list
    def insert_last(self, data):
        if (data == None):
            return False
        new_node = Node(data)
        curr_node = self.head

        while(curr_node.get_next() != None):
            curr_node = curr_node.get_next()

        curr_node.set_next(new_node)
        self.length += 1
        return True

    # Remove Last
    def remove_last(self):
        if (self.length == 0 ):
            return None

        curr_node = self.head

        while(curr_node.get_next().get_next() != None):
            curr_node = curr_node.get_next()

        temp_node = curr_node.get_next()
        curr_node.set_next(None)
        self.length -= 1
        return temp_node

    def get_data_at_n(self, n):
        curr_node = self.head
        counter = 0

        while(counter<n):
            curr_node = curr_node.get_next()
            counter += 1

        return curr_node.get_data()

    def insert_at_n(self, data, n):
        if (data == None):
            return False
        if (n < 0):
            return False
        if (n == 0):
            return insert_front(data)
        if (n > self.length+1):
            return False

        new_node = Node(data)
        curr_node = self.head
        counter = 0

        while(counter<n-1):
            curr_node = curr_node.get_next()
            counter += 1

        new_node.set_next(curr_node.get_next())
        curr_node.set_next(new_node)
        self.length += 1
        return True

    def remove_at_n(self, n):
        if (self.length == 0 ) or (n < 0) or (n > self.length):
            return None
        if (n == 0):
            return remove_front()

        curr_node = self.head
        counter = 0

        while(counter<n-1):
            curr_node = curr_node.get_next()
            counter += 1

        tmp_node = curr_node.get_next()
        curr_node.set_next(tmp_node.get_next())
        tmp_node.set_next(None)

        self.length -= 1
        return tmp_node

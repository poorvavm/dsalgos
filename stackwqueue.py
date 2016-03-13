# Create stack using queue
#------------------------------------------
# Stack class
#------------------------------------------
class stack_using_queues:
    data_q = None
    empty_q = None
    length = 0

    def __init__(self):
        self.data_q = queue()
        self.empty_q = queue()
        self.length  = 0

    def push(self, element):
        if (element == None):
            return None
        self.empty_q.enqueue(element)

        shuffle_element = self.data_q.dequeue()
        while(shuffle_element):
            self.empty_q.enqueue(shuffle_element)
            shuffle_element = self.data_q.dequeue()

        temp = self.data_q
        self.data_q = self.empty_q
        self.empty_q = temp
        self.length += 1
            return element

    def pop(self):
        if (self.length == 0):
            return None 
        self.length -= 1
        return self.data_q.dequeue()
        
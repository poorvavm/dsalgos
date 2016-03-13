# Create queue using stack
#------------------------------------------
# Queue using stack class
#------------------------------------------
class queue_using_stack:
    data_stack = None
    empty_stack = None
    length = 0

    def __init__(self):
        self.data_stack = stack()
        self.temp_stack = stack()
        self.length = 0

    def enqueue(self, element):
        if (element == None):
            return None
        # empty data stack into empty stack
        #pop data stack into empty stack
        shuffle_element = self.data_Stack.pop()
        while(shuffle_element):
            self.temp_stack.push(shuffle_element)
            shuffle_element = self.data_Stack.pop()
        # push element in data_Stack
        self.data_Stack.push(element)
        #push element in data stack
        #pop from temp stack and push in data stack
        reshuffle_element = self.temp_stack.pop()
        while(reshuffle_element):
            self.data_Stack.push(reshuffle_element)
            reshuffle_element=self.temp_stack.pop()
            self.length += 1
            return element

    def dequeue(self):
        if (self.length == 0):
            return None
            self.length -= 1
            return self.data_stack.pop()

### To test the class###
if __name__ == "__main__":
    q1 = queue()
    print q1

    q1.enqueue('3')
    q1.enqueue('23')
    print q1

    print q1.dequeue()
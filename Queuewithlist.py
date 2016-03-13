#create queue with a list
#------------------------------------------
# Queue class
#------------------------------------------
class queue:
    inner_list = []
    length = 0

    def __init__(self):
        self.inner_list = []
        self.length = 0

    def __str__(self):
        return ', '.join(self.inner_list)

    def enqueue(self, element):
        self.inner_list.append(element)
        self.length += 1
        return element

    def dequeue(self):
        if (self.length <= 0):
            return None

        val = self.inner_list.pop(0)
        if val:
            self.length -= 1
        return val
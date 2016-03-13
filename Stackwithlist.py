#create stack with a list
#------------------------------------------
# Stack class
#------------------------------------------
class stack:
    inner_list = []
    length = 0

    def __init__(self):
        self.inner_list = []
        self.length = 0

    def __str__(self):
        return ', '.join(self.inner_list)

    def push(self, element):
        self.inner_list.append(element)
        self.length += 1

    def pop(self):
        if (self.length <= 0):
            return None

        val = self.inner_list.pop()
        if val:
            self.length -= 1
        return val
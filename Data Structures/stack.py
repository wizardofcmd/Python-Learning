# Writing own Stack Data Structure Class
# Will implement Test Cases

class Stack():
    def __init__(self, collection, item):
        self.collection = []
        self.item = item

    def push(self, collection, item):
        collection.append(item)

    def peek(self, collection):
        # [-1] references the last element in the list
        return collection[-1]

    def pop(self, collection):
        popped = collection[-1]
        collection[-1].remove(popped)
        return popped

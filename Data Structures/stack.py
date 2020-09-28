# Writing my own Stack Data Structure Class
# Will implement Test Cases

class Stack():
    """Class that allows for Stack functionality"""
    def __init__(self, collection, item):
        self.collection = []
        self.item = item

    def push(self, item):
        """Push an item to the top of the stack."""
        self.collection.append(item)

    def peek(self):
        """Look at the top of the stack."""
        # [-1] references the last element in the list
        return self.collection[-1]

    def pop(self):
        """Remove the last added item to the stack."""
        popped = self.collection[-1]
        self.collection[-1].remove(popped)
        return popped

    def isEmpty(self):
        """Check if the stack is empty."""
        if self.collection:
            return True
        else:
            return False

    def clear(self):
        """Clear all items in the stack."""
        for item in self.collection:
            self.collection.remove(item)

    def showStack(self):
        """Loop through the whole stack and print each item to the user."""
        for item in self.collection:
            print(item)
        print()

import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """Testing the Stack class"""

    def setUp(self):
        """Create a stack data structure to store items into a list"""
        self.S = Stack()

    def test_push(self):
        """Test that an item is added to the stack."""
        item = 'blackberry'
        self.S.push(item)
        """Check that the item is added to the stack."""
        self.assertIn(item, self.S.collection)

    def test_peek(self):
        """Test that the top item in the stack is returned."""
        self.S.push('banana')
        top = self.S.peek()
        self.assertEqual(top, 'banana')

    def test_pop(self):
        """Test that the top item in the stack is removed."""
        self.S.push('apple')
        self.S.push('strawberry')
        self.S.pop()
        self.assertNotIn('strawberry', self.S.collection)

    def test_is_empty(self):
        """Test that the method correctly returns True if stack is empty."""
        answer = self.S.is_empty()
        self.assertEqual(answer, True)

    def test_clear(self):
        """Test that the stack is successfully emptied."""
        self.S.push('blueberry')
        self.S.clear()
        self.assertTrue(self.S.is_empty())
        
unittest.main()

"""

The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.

"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        current_pos = 1

        def find_obj(current, position, current_pos):
            if current_pos == position:
                return current
            else:
                current = current.next
                current_pos += 1
                return find_obj(current, position, current_pos)

        return find_obj(current, position, current_pos)


    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        prev_elem = self.get_position(position - 1)
        new_element.next = prev_elem.next
        prev_elem.next = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        current_pos = 1
        while current.value != value:
            current_pos += 1
            current = current.next

        if (current_pos == 1):
            self.head = current.next
        else:
            prev_elem = self.get_position(current_pos - 1)
            prev_elem.next = current.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

class DoubleListNode(object):
    """ Double list node"""
    def __init__(self,  data,  prev,  next):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoubleList(object):
    """ Class representing a double connected list"""
    head = None
    tail = None
    
    def append(self,  data):
        new_node = DoubleListNode(data,  None,  None)
        if (self.head is None):
            self.head = self.tail = new_node
        else:
            # Append node to tail.
            self.tail.next = new_node
            # Connect reverse direction.
            new_node.prev = self.tail
            new_node.next = None
            # Move tail.
            self.tail = new_node
    
    def print_forward(self):
        """ Prints elements in the list in forwards direction"""
        print("List forward=")
        tmp_node = self.head
        while(tmp_node is not None):
            print (tmp_node.data)
            # Move to next node.
            tmp_node = tmp_node.next
            
    def print_reverse(self):
        """ Prints elements in the list in reversed direction"""
        print("List backward=")
        tmp_node = self.tail
        while(tmp_node is not None):
            print (tmp_node.data)
            # Move to prev node.
            tmp_node = tmp_node.prev


class TreeNode(object):
    """ Class representing a tree"""
    def __init__(self,  data):
        self.data = data
        self.left = None
        self.right = None

    def set_left_leaf(self,  data):
        self.left = TreeNode(data)
        
    def set_right_leaf(self,  data):
        self.right = TreeNode(data)

    def set_left_node(self,  node):
        self.left = node
        
    def set_right_node(self,  node):
        self.right = node

    def print_tree(self):
        print("Tree=")
        self.print_recursive_depth_first(self)
    
    def print_recursive_depth_first(self,  node):
        if node is None:
            return
        # If this is a valid node - print data...
        print (node.data)
        # ... and go deeper - left first...
        self.print_recursive_depth_first(node.left)
        # ... and then right.
        self.print_recursive_depth_first(node.right)
       
    def to_dll(self):
        """ Method recursively traverses the tree (left, depth first) and addes nodes to newly created DLL"""
        dll = DoubleList()
        self.dll_add_recursive_depth_first(self,  dll)
        return dll
        
        
    def dll_add_recursive_depth_first(self,  node,  dll):
        if node is None:
            return
        # If this is a valid node - go deeper - left first...
        self.dll_add_recursive_depth_first(node.left,  dll)
        # Then add node to dll.
        dll.append(node.data)
        # ... and finally right.
        self.dll_add_recursive_depth_first(node.right,  dll)


if __name__ == "__main__":
    # List test.
    #d = DoubleList ()
    #d.append(2)
    #d.append(4)
    #d.print_forward()
    # Tree test.
    tree = TreeNode(10)
    # Left root node.
    left = TreeNode(12)
    left.set_left_leaf(25)
    left.set_right_leaf(30)
    tree.set_left_node(left)
    # Right root node.
    right = TreeNode(15)
    right.set_left_leaf(36)
    tree.set_right_node(right)
    #tree.print_tree()
    
    # Turn tree to double linked list.
    d = tree.to_dll()
    d.print_forward()
    d.print_reverse()


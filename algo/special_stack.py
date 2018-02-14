
class SpecialStack(object):
    """ Stack that can always return min value with O(1)"""
    stack = []
    mins = []
    
    def push(self,  data):
        # Append data to regular stack.
        self.stack.append(data)
        # Append data to stack with minimum values.
        if (not self.mins ) or (data < self.mins[-1]):
            self.mins.append(data)
        else:
            self.mins.append(self.mins[-1])
    
    def pop(self):
        if (not self.stack):
            print("Pop failure - stack empty")
            return None
        self.mins.pop()
        return self.stack.pop()
    
    def get_min(self):
        if (not self.stack):
            return "Stack empty"
        return self.mins[-1]
        
if __name__ == "__main__":
    stack = SpecialStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.get_min())
    stack.push(5)
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.get_min())
    stack.pop()
    
    

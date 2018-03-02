#https://www.programcreek.com/2012/12/leetcode-evaluate-reverse-polish-notation/
# Evaluate Reverse Polish Notation

def eval_rpn(expr):
    ''' Evaluates Reverse Polish Notation using stack-like approach'''
    ops = ['*','+','-','/']

    # Define operation "switch".
    op = (lambda a, b, val:
        a*b if val == '*' else
        a+b if val == '+' else
        a-b if val == '-' else
        a/b if val == '/' else
        0)

    # Stack with values.
    values=[]
    for val in expr:
        #print (values)
        #print("val=", val)
        if val in ops:
            # Edge case I: not enough elements on the stack - improper expression.
            if (len(values) < 2):
                print("Edge case 1")
                return -1
            # Get values
            b = values.pop()
            a = values.pop()
            # Perform operation.
            c = op(a, b, val)
            print(a, b, c)
            # Push result to stack.
            values.append(c)
        # Check if it is valid digit. Enable floats i.e. replace first . with empty string - but only the first one!
        elif val.replace('.','',1).isdigit():
            # Push value to stack.
            values.append(float(val))
        else:
            # Invalid symbol
            print("Edge case 3")
            return -1            
    # Edge case II: too many elements on the stack left - improper expression.
    if (len(values) > 1):
        print("Edge case 2")
        return -1
    # We have parsed the whole expression.
    return values.pop()
    
if __name__ == "__main__":
    #expr = ["2", "1", "+", "3", "*"]
    expr = ["4", "10", "5", "/", "+"]
    expr = ["4.25", "1.1", "+"]
    print("Result = {}".format(eval_rpn(expr)))
    
    
    

# Cracking, chap.8, p.350

def loop_multiply(a, b):
    # Simple for loop - adding one value number of times.
    (min_val, max_val) = (a,b) if a<b else (b,a)
    sum = 0
    for _ in range(min_val):
        print("compute")
        sum += max_val
    return sum

def rec_multiply(a, b, sum=0):
    # Recursive.
    # Stop condition.
    if a == 0 or b == 0:
        return 0
    (min_val, max_val) = (a,b) if a<b else (b,a)
    print(f"compute {a} * {b}")
    # "remove" 1 item from the equation and recurse with "multiplication".
    return max_val + rec_multiply(min_val-1, max_val, sum)

print(rec_multiply(6,4))
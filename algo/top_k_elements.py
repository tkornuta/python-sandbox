# https://www.programcreek.com/2014/05/leetcode-top-k-frequent-elements-java/
# Given a non-empty array of integers, return the k most frequent elements.

items = 'a b c d e r f b h y u j m n b c y s y e y c v h g u x i k x a c x x s x d b c d e r g k j'.split(' ')
k = 6

print("items = ",items)

# Solution I:
# Sort items.
sort_items = sorted(items)
print(sort_items)
# Remove the first element
prev_el = sort_items.pop(0)
count = 1
# Create (element-counter) tuple and add it to a list.
el_count = [(prev_el, count)] 
# Iterate through the rest of elements.
for el in sort_items:
    # Check element
    if el == prev_el:
        count += 1
        el_count[-1] = (prev_el, count) 
    else:
        count = 1
        prev_el = el
        el_count.append((prev_el, count))
print(el_count)

# Sort in descending order.
el_count.sort(key=lambda el: el[1],reverse=True)
print(el_count)
# Get first K elements.
output = [el[0] for el in el_count[0:k]]
print("output =", output)


# Solution II: unfinished...
# 1. create set of unique elements
unique_items = set(items)
print("unique items =",unique_items)
print(list(enumerate(unique_items)))



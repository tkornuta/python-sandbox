# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

# inputs: 5, 15, 1, 3
# expected outputs: 5, 15, 5, 5

def running_mean(inputs):
    running_sum = 0
    outputs = []
    for i, value in enumerate(inputs):
        running_sum += value
        outputs.append(value/(i+1))

    return outputs

def insertion_sort(input, sorted):
    index = -1
    for i in range(len(sorted)):
        if sorted[i] > input:
            index = i
            break
    #print(index)
    if index == 0:
        # Edge case: first position.
        sorted.insert(0, input)
    elif index == -1:
        # Edge case: last position.
        sorted.append(input)
    else:
        sorted.insert(index, input)
    return sorted

def running_median(inputs):
    sorted_inputs = []
    outputs = []
    for i, value in enumerate(inputs):
        # Insert value in the right place.
        sorted_inputs = insertion_sort(value, sorted_inputs)
        #print(sorted_inputs)
        # Get median index.
        index = int(len(sorted_inputs)/2)
        #print(index, " -> ", sorted_inputs[index])
        outputs.append(sorted_inputs[index])
    return outputs

inputs= [5,15,1,3]
#inputs= [26, 5,15,1,3, 27,20,18,4]
print("Inputs: ", inputs)
print("Running means: ", running_mean(inputs))
print("Running medians: ", running_median(inputs))
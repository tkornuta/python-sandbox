def triplet(lst):
    for x in range(len(lst)):
        for y in range(x+1,  len(lst)):
            for z in range (y+1,  len(lst)):
                if (lst[x]**2 + lst[y]**2) == lst[z]**2:
                    print ("Found Pythagorean triplet: {}, {}, {}".format(lst[x], lst[y], lst[z]))
                    return True
    return False


if __name__ == "__main__":
    lst = [3, 1, 4, 6, 5]
    print(triplet(lst))


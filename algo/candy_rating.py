
def give_candies(ratings):
    
    # Analyse how many candies are possessed by left direct neighbor.
    left_neightbor = [1]*len(ratings)
    for i in range(1,  len(ratings)):
        if (ratings[i] > ratings[i-1]):
            left_neightbor[i] = left_neightbor[i-1]+1
    print(left_neightbor)
    
        # Analyse how many candies are possessed by right direct neighbor.
    right_neightbor = [1]*len(ratings)
    for i in range(len(ratings)-2,  -1,  -1):
        if (ratings[i] > ratings[i+1]):
            right_neightbor[i] = right_neightbor[i+1]+1
        #elif  (ratings[i] == ratings[i+1]):
        #    right_neightbor[i] = right_neightbor[i+1]
    print(right_neightbor)

    # Number of candies that each kid receives is the max of lest and right.
    candies = []
    for i in range(len(ratings)):
        candies.append(max(left_neightbor[i],  right_neightbor[i]))
    print(candies)

    return sum(candies)

if __name__ == "__main__":

    ratings1 = [1, 4, 3, 3, 3, 1]
    ratings2 = []
    ratings3 = [0]
    ratings4 = [10]
    ratings5 = [1, 2, 3, 4, 2, 3,  2]
    ratings6 = [1, 2, 3, 3, 3, 2, 1]
    print("Solution:")
    print (give_candies(ratings6))


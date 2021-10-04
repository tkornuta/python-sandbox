# 1. A robot delivery problem.

# You are presented with a robot that’s trying to deliver goods to a “linear” neighborhood.
#                 0 1 2 3 4 5 6 7
#                 _ _ _ _ _ _ _ _
#                 a b c d e f g h

# Your robot is told to search for a house with a particular name (e.g., “g”). The robot can ask any of the neighbors for directions to the resident it’s looking for.

# Query(int house_id, string name) \in {-1, 1, 0}

# Query(4, “g”) ⇒ 1

# Where "-1" is left, "1" is right and "0" means this is the place you are looking for.

# I would like an algorithm that finds the index of the target house, while incurring minimal costs assuming you pay “1” for each question asked.

# name: name of the person you’re searching for.

# N: the number of houses.


# EVEN
#                 0 1 2 3 4 5 6 7
#                 _ _ _ _ _ _ _ _
#                 a d c e f t g h


#deliver("e")
#index = 4
#search_range = 4
#Query(4, "e") -> -1 ("f")

#search_range = 2
#index = 2
#Query(2, "e") -> 1

#search_range = 1
#index = 3
#Query(2, "e") -> 0 # -> Found!


# ODD
#                 0 1 2 3 4 5 6
#                 _ _ _ _ _ _ _
#                 a d c e f t g

#deliver("t")
#index = 4
#search_range = 4
#Query(4, "t") -> 1

#search_range = 2
#index = 6
#Query(6, "t") -> -1

#search_range = 1
#index = 5
#Query(5, "t") -> 0 # -> Found!

# 1st use-case.
#house_mapping = "a d c e f t g".split()

# 2nd use-case.
house_mapping = "a d c e f t g h".split()


def Query(index: int, target: str) -> int: # {0,-1,1}
    
    # Jackpot!
    if house_mapping[index] == target:
        return 0
    
    # Check it if is in the left table.
    if target in house_mapping[:index]:
        return -1

    # Check it if is in the righ table.
    if target in house_mapping[index+1:]:
        return 1



def deliver(houses: list, target: str):
    """ Assumptions:
    1) House ids are unique.
    2) House is there ;)
    """
    lenght = len(houses)

    # Starting in the middle
    index = int(lenght/2)
    search_range = lenght/2

    # Edge case: no houses.
    if lenght == 0:
        return "Sorry, cannot deliver the package!"
    
    while True:
        # Knock, knock.
        ans = Query(index, target) 
        # Terminal condition.
        if ans == 0:
            return index
        elif ans == -1:
            # Decrease the search range.
            search_range = search_range/2
            delta = int(search_range) if int(search_range) > 0 else 1
            # Look at the left.
            index -= delta
        else: # ans = 1
            # Decrease the search range.
            search_range = search_range/2
            delta = int(search_range) if int(search_range) > 0 else 1
            # Look at the right.
            index += delta
        
# Call it.
print(deliver(house_mapping, "d"))
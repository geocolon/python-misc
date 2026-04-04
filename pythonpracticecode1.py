# Your task: Given this list of edges, 
# write a function that builds an adjacency list (dictionary). 
# Don't look at the study guide.
# 
# What are the edges? Write a function that builds an adjacency list.
# Is the there mixed types or characters? Is there any size limits to the list?
# Are were sorting too? #/

edges1 = [
    ("ghost-1", "ghost-2"),
    ("ghost-1", "ghost-3"),
    ("ghost-2", "ghost-4"),
    ("ghost-3", "ghost-4"),
]

def drone_adjac(edges):
    result = {}
    for drone_a, drone_b in edges:
        # Option A: check manually
        if drone_a not in result:
            result[drone_a] = []
        result[drone_a].append(drone_b)

        if drone_b not in result:
            result[drone_b] = []
        result[drone_b].append(drone_a)
    return result
            # Option B: use setdefault (does the same thing in one line)
            # result.setdefault(drone_a, []).append(drone_b)
print(drone_adjac(edges1))   
print("----************************----")
print("----************************----")

# Your function should return:
# {
#   "ghost-1": ["ghost-2", "ghost-3"],
#   "ghost-2": ["ghost-1", "ghost-4"],
#   "ghost-3": ["ghost-1", "ghost-4"],
#   "ghost-4": ["ghost-2", "ghost-3"],
# }

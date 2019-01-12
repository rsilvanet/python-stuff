relations = {}
relations["start"] = {}
relations["start"]["a"] = 6
relations["start"]["b"] = 2
relations["a"] = {}
relations["a"]["end"] = 1
relations["b"] = {}
relations["b"]["a"] = 3
relations["b"]["end"] = 5
relations["end"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []

def getLowerCostNode(costs):
    lowerCost = float("inf")
    lowerCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowerCost and node not in processed:
            lowerCost = cost
            lowerCostNode = node
    return lowerCostNode

node = getLowerCostNode(costs)

while node is not None:
    cost = costs[node]
    children = relations[node]
    for child in children.keys():
        newCost = cost + children[child]
        if costs[child] > newCost:
            costs[child] = newCost
            parents[child] = node
    processed.append(node)
    node = getLowerCostNode(costs)
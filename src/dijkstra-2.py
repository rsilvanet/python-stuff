class Node:
    children = {}
    name = ""
    cost = 100
    parent = None
    verified = False

    def __init__(self, name):
        self.name = name

nodeBook = Node("Book")
nodePoster = Node("Poster")
nodeLP = Node("LP")
nodeBass = Node("Bass")
nodeDrum = Node("Drum")
nodePiano = Node("Piano")
nodeBook.children = {}
nodeBook.children[nodePoster] = 0
nodeBook.children[nodeLP] = 5
nodePoster.children = {}
nodePoster.children[nodeBass] = 30
nodePoster.children[nodeDrum] = 35
nodeLP.children = {}
nodeLP.children[nodeBass] = 15
nodeLP.children[nodeDrum] = 20
nodeBass.children = {}
nodeBass.children[nodePiano] = 20
nodeDrum.children = {}
nodeDrum.children[nodePiano] = 10

lowerCostNode = None
lowerCostValue = 100
currentNode = nodeBook

for childNode in currentNode.children.keys():
    if currentNode.children[childNode] < lowerCostValue:
        lowerCostNode = childNode
        lowerCostValue = currentNode.children[childNode]

lowerCostNode.cost = lowerCostValue
lowerCostNode.verified = True

for childNode in lowerCostNode.children.keys():
    childNode.cost = lowerCostNode.cost + lowerCostNode.children[childNode]
    childNode.parent = lowerCostNode

print(lowerCostNode.name)
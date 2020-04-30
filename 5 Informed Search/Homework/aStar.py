class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.COST = cost


    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_BEST(fringe)
        if GOAL_STATE.__contains__(node.STATE):
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        #print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.COST = cost_lookup[node.STATE][child]

        successors = INSERT(s, successors)

    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    queue.extend(list)
    return queue

'''
Removes and returns the first element from fringe
'''
def REMOVE_BEST(queue):

    index = 0
    bestIndex = 0
    best = 0
    for node in queue:
        if index == 0:
            best = lookup[node.STATE] + node.COST
        if lookup[node.STATE] + node.COST < best:
            best = lookup[node.STATE] + node.COST
            bestIndex = index
        index += 1

    return queue.pop(bestIndex)

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

cost_lookup = {
    'A': {
        'B': 1,
        'C': 2,
        'D': 4,
    },
    'B': {
        'F': 5,
        'E': 4,
    },
    'C': {
        'E': 1,
    },
    'D': {
        'H': 1,
        'I': 4,
        'J': 2,
    },
    'D': {
        'H': 1,
        'I': 4,
        'J': 2,
    },
    'E': {
        'G': 2,
        'H': 3,
    },
    'F': {
        'G': 0,
    },
    'G': {
        'K': 0,
    },
    'H': {
        'K': 6,
        'L': 5,
    },
    'I': {
        'L': 3,
    },
    'J': {},
    'K': {},
    'L': {}
}

lookup = {
    'A': 6,
    'B': 5,
    'C': 5,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 4,
    'H': 1,
    'I': 2,
    'J': 1,
    'K': 0,
    'L': 0
}

INITIAL_STATE = 'A'
GOAL_STATE = ['L', 'K']
STATE_SPACE =  {'A': ['B', 'C', 'D'],
               'B': ['E', 'F'],
               'C': ['E'],
               'D': ['H', 'I', 'J'],
               'E': ['G', 'H'],
               'F': ['G'],
               'G': ['K'],
               'H': ['K', 'L'],
               'I': ['L'],
               'J': [],
               'K': [],
               'L': []}


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    #print(path)
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
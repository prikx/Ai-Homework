A = 'A'
B = 'B'
percepts = []
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Clean'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    # ...
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left'
    # ...
}

def LOOKUP(percepts, table):
    return table.get(tuple(percepts))


def TABLE_DRIVEN_AGENT(percept):
    percepts.append(percept)
    return LOOKUP(percepts, table)


def run():
    print('Action \tPercepts')
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)


run()
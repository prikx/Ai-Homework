A = 'A'
B = 'B'

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}
rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}
# Ex rule (if location == A && Dirty then rule 1)

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}

def INTERPRET_INPUT(input): # No interpretation
    return input

def RULE_MATCH(state, rules): # Match rule for a given state
    return rules.get(tuple(state))

def SIMPE_REFLEX_AGENT(percept): # Determine action
    state = INTERPRET_INPUT(percept)
    rule = RULE_MATCH(state, rules)
    return RULE_ACTION[rule]

def Sensors(): # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])

def Actuators(action): # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A

def run(n): # run the agent through n steps
    print('Current New')
    print('location status action location status')
    for i in range(1, n):
        (location, status) = Sensors() # Sense Environment before action
        print('{:12s}{:8s}'.format(location, status), end='')
        action = SIMPE_REFLEX_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors() # Sense Environment after action
        print('{:8s}{:12s}{:8s}'.format(action, location, status))

run(10)
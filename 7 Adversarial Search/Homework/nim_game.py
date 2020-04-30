def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for state in successors_of(state):
            v = max(v, min_value(state))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for state in successors_of(state):
            v = min(v, max_value(state))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state


"""
Go over each pile in the state. If there is no pile that is larger than three. Then you lose
"""


def is_terminal(state):
    for pileSize in state:
        terminal = True
        if pileSize >= 3:
            terminal = False
    return terminal


"""
If the length of the state is divisible with two then the computer will have lost because the player made the last move.
Therefore you need to look for state with an uneven length of the piles.
"""


def utility_of(state):
    if len(state) % 2 == 0:
        return -1
    else:
        return 1


"""
Create a list of all possible successor states.
"""


def successors_of(state):
    possible_states = []

    # Go over every pile
    for pile in state:
        upper_range = int(pile/2)
        if pile < 3:
            continue

        # Go over each split
        for j in range(1, upper_range):

            # Make a copy and remove the original pile from it.
            new_possible_states = state[:]
            new_possible_states.remove(pile)

            if pile % 2 == 0 and j == pile / 2:
                continue

            # Add the two new piles to the state
            new_possible_states.append(j)
            new_possible_states.append(pile - j)
            possible_states.append(new_possible_states)

    return possible_states


def display(state):
    print(state)


def main():
    state = [15]
    while not is_terminal(state):
        state = minmax_decision(state)
        if not is_terminal(state):
            display(state)

            # Get user input
            choice = int(input("Which pile do you want to split? type a number between 1 - " + str(len(state)) + " : "))
            choice_two = int(input("How many tokens go in the first pile"))
            new_pile = state[choice-1] - choice_two

            # Remove old and add new piles to the state
            state.remove(state[choice-1])
            state.append(choice_two)
            state.append(new_pile)
            display(state)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
def alpha_beta_decision(state):
    infinity = float('inf')

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity

        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(
        successors_of(state),
        lambda a: min_value(a, infinity, -infinity)
    )
    return state


def is_terminal(state):
    for pileSize in state:
        terminal = True
        if pileSize >= 3:
            terminal = False
    return terminal


def utility_of(state):
    if len(state) % 2 == 0:
        return -1
    else:
        return 1


def successors_of(state):
    possible_states = []

    # Go over every pile
    for pile in state:
        upper_range = int(pile / 2)

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


def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = alpha_beta_decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile do you want to split? type a number between 1 - " + str(len(list_of_piles)) + " : ")
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        print('How many tokens go in the first pile')
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [7]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()

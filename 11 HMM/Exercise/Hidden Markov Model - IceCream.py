import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    big_n = len(states) - 2 
    big_t = len(observations) - 1

    forward = np.pi * np.ones((big_n + 2, big_t + 1))

    for s in inclusive_range(1, big_n):
        forward[s, 1] = transitions[0, s] * emissions[s, observations[1]]

    for t in inclusive_range(2, big_t):
        for s in inclusive_range(1, big_n):
            forward[s, t] = np.array(
                [forward[s_mark, t - 1] * transitions[s_mark, s] * emissions[s, observations[t]] for s_mark in
                 inclusive_range(1, big_n)]).sum()

    probability = np.array([forward[s, big_t] * transitions[s, big_n + 1] for s in inclusive_range(1, big_n)]).sum()
    return probability



def compute_viterbi(states, observations, transitions, emissions):
    N = len(states) - 2
    T = len(observations) - 1

    viterbi = np.pi * np.ones((N + 2, T + 1))
    backpointer = 100 * np.ones((N + 2, T + 1), dtype=int)

    for s in inclusive_range(1, N):
        viterbi[s, 1] = transitions[0, s] * emissions[s, observations[1]]
        backpointer[s, 1] = 0

    for t in inclusive_range(2, T):
        for s in inclusive_range(1, N):
            viterbi[s, t] = np.array(
                [viterbi[s_mark, t - 1] * transitions[s_mark, s] * emissions[s, observations[t]] for s_mark in
                 inclusive_range(1, N)]).max()
            backpointer[s, t] = np.array(
                [viterbi[s_mark, t - 1] * transitions[s_mark, s] for s_mark in inclusive_range(1, N)]).argmax() + 1

    qf = N + 1
    viterbi[qf, T] = np.array([viterbi[s, T] * transitions[s, qf] for s in inclusive_range(1, N)]).max()
    backpointer[qf, T] = np.array([viterbi[s, T] * transitions[s, qf] for s in inclusive_range(1, N)]).argmax() + 1

    backpointers = backpointer[1:, 1:]
    state_index = T - 1
    result = []
    for i in reversed(range(len(backpointers))):
        state_index = backpointers[i, state_index]
        result.append(states[state_index])

    return result


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))
    return max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()

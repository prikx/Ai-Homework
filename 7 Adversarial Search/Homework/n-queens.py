import random
from random import randint
import queens_fitness

p_mutation = 0.20
num_of_generations = 5000


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(0, 2):
            mother, father = random_selection(population, fitness_fn)
            children = reproduce(mother, father)
            for child in children:
                if random.uniform(0, 1) < p_mutation:
                    child = mutate(child)
                new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = new_population

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    r = randint(0, len(mother))
    child1 = list(mother)
    child2 = list(father)

    for x in range (r, len(father)):
        child1[x] = father[x]
        child2[x] = mother[x]
    return [tuple(child1), tuple(child2)]


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    ind = list(individual)
    ri = randint(0, len(ind)-1)
    rn = randint(1, 8)
    ind[ri] = rn

    mut = tuple(ind)
    return mut


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """
    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)

    selected = ((), ())

    fitness = [fitness_fn(individual) for individual in ordered_population]

    while selected[0] == selected [1]:
        selected = tuple(random.choices(ordered_population, weights=fitness, k=2))
    return selected


def fitness_function(individual):
    return (queens_fitness.fitness_fn_positive(individual))


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 28
    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (2, 6, 1, 8, 3, 5, 4, 2),
        (6, 2, 8, 3, 6, 4, 3, 1),
        (1, 2, 5, 4, 8, 6, 2, 8),
        (4, 1, 5, 6, 3, 4, 2, 1)
    }
    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + "  Fitness: " + str(fitness_function(fittest)))


if __name__ == '__main__':
    pass
    main()

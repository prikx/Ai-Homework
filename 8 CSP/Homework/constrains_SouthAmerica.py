from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if len(assignment) == 15:
            return assignment
        unassigned = self.select_unassigned_variable(assignment)
        for x in self.order_domain_values(unassigned, assignment):
            if self.is_consistent(unassigned, x, assignment):
                assignment[unassigned] = x
                result = self.recursive_backtracking(assignment)
                if result:
                    return result
                del assignment[unassigned]
        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    CR, Pa, Co, Ve, G, Su, Gu, Br, Ec, Pe, Bo, Par, Ur, Ar, Ch = "Costa Rica", "Panama", "Colombia", "Venezuela", "Guyana", "Suriname", "French Guyana", "Brasil", "Ecuador", "Peru", "Bolivia", "Paraguay", "Uruguay", "Argentina", "Chile"

    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [CR, Pa, Co, Ve, G, Su, Gu, Br, Ec, Pe, Bo, Par, Ur, Ar, Ch]
    domains = {
        CR: values[:],
        Pa: values[:],
        Co: values[:],
        Ve: values[:],
        G: values[:],
        Su: values[:],
        Gu: values[:],
        Br: values[:],
        Ec: values[:],
        Pe: values[:],
        Bo: values[:],
        Par: values[:],
        Ur: values[:],
        Ar: values[:],
        Ch: values[:],
    }
    neighbours = {
        CR: [Pa],
        Pa: [CR, Co],
        Co: [Pa, Ve, Br, Ec, Pe],
        Ve: [Co, Br, G],
        G: [Ve, Su, Br],
        Su: [G, Gu, Br],
        Gu: [Su, Br],
        Br: [Gu, Su, G, Ve, Co, Pe, Bo, Par, Ar, Ur],
        Ec: [Co, Pe],
        Pe: [Ec, Br, Co, Bo, Ch],
        Bo: [Pe, Br, Par, Ar, Ch],
        Par: [Bo, Br, Ar],
        Ur: [Ar, Br],
        Ar: [Ch, Bo, Par, Br, Ur],
        Ch: [Ar, Bo, Pe]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        CR: constraint_function,
        Pa: constraint_function,
        Co: constraint_function,
        Ve: constraint_function,
        G: constraint_function,
        Su: constraint_function,
        Gu: constraint_function,
        Br: constraint_function,
        Ec: constraint_function,
        Pe: constraint_function,
        Bo: constraint_function,
        Par: constraint_function,
        Ur: constraint_function,
        Ar: constraint_function,
        Ch: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html

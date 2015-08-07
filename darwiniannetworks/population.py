from darwin.potential import (
    Potential,
    multiply,
    divide,
    marginalize
    )


class Population(Potential):

    def __init__(self, variables=[], cardinalities=[], values=[],
                 combative=[], docile=[],
                 evidence={}):
        # Default values, in case user is just using algebraic mode
        if len(combative) > 0 and len(variables) == 0:
            variables = combative + docile
        if len(cardinalities) == 0:
            cardinalities = [2]*len(variables)
        if len(values) == 0:
            from random import random
            values = [random()]*(2**len(variables))
            norm = sum(values)
            values = [v/norm for v in values]
        # Call super constructor
        super().__init__(variables, cardinalities, values,
                         combative, docile, evidence)

    @staticmethod
    def from_potential(potential):
        return Population(potential.variables,
                          potential.cardinalities,
                          potential.values,
                          potential.left_hand_side,
                          potential.right_hand_side,
                          potential.evidence
                          )

    def combative(self):
        return self.left_hand_side

    def docile(self):
        return self.right_hand_side

    def merge(self, other_population):
        if len(
            set(self.combative).intersection(set(other_population.combative))
           ) > 0:
            potential = divide(self, other_population)
        else:
            potential = multiply(self, other_population)
        return Population.from_potential(potential)

    def replicate(self, variables):
        potential = marginalize(self, variables)
        return Population.from_potential(potential)

from random import choice

class Dice:
    def __init__(self, sides, weights=None):
        if weights == None:
            weights = [1] * sides
        if len(weights) != sides:
            raise ValueError("Length of Weights must equal sides!")
        self.sides = sides
        self.weights = weights
    def roll(self, iterations=1):
        results = []
        for x in range(iterations):
            options = []
            for (side, weight) in enumerate(self.weights):
                options += [side+1] * weight
            results.append(choice(options))
        return results

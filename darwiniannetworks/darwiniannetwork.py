class DarwinianNetwork():

    def __init__(self):
        self.populations = set()

    def add_population(self, population):
        self.populations.add(population)

    def add_populations(self, populations):
        for population in populations:
            self.add_population(population)

    def delete_population(self, population):
        self.populations.remove(population)

    def delete_populations(self, populations):
        for population in populations:
            self.delete_population(population)

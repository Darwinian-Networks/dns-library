import unittest
from darwiniannetworks.population import Population
from darwiniannetworks.darwiniannetwork import DarwinianNetwork


class TestDarwinianNetwork(unittest.TestCase):

    def setUp(self):
        self.pop1 = Population(combative=["a"], docile=["b"])
        self.pop2 = Population(combative=["b"], docile=["c", "d"])
        self.pop3 = Population(combative=["c"])
        self.pop4 = Population(combative=["d"])

        self.dn = DarwinianNetwork()
        self.dn.add_populations([self.pop1, self.pop2, self.pop3, self.pop4])

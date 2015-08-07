import unittest
from darwiniannetworks.population import Population


class TestPopulation(unittest.TestCase):

    def setUp(self):
        self.pop1 = Population(combative=["a"], docile=["b"],
                               values=[0.3, 0.5, 0.7, 0.5],
                               cardinalities=[2, 2])
        self.pop2 = Population(combative=["b"], docile=["c"],
                               values=[0.1, 0.2, 0.9, 0.8],
                               cardinalities=[2, 2])

    def test_combative_docile(self):
        self.assertListEqual(sorted(self.pop1.combative()), ["a"])
        self.assertListEqual(sorted(self.pop1.docile()), ["b"])
        self.assertListEqual(sorted(self.pop2.combative()), ["b"])
        self.assertListEqual(sorted(self.pop2.docile()), ["c"])

    def test_merge(self):
        pop3 = self.pop1.merge(self.pop2)
        self.assertListEqual(["{:.2f}".format(n) for n in pop3.values],
                             ['0.03', '0.05', '0.14', '0.10', '0.27',
                             '0.45', '0.56', '0.40'])
        self.assertListEqual(pop3.combative(), ["a", "b"])
        self.assertListEqual(pop3.docile(), ["c"])

    def test_replicate(self):
        pop3 = self.pop1.merge(self.pop2)
        pop4 = pop3.replicate(["a"])
        self.assertListEqual(["{:.2f}".format(n) for n in pop4.values],
                             ['0.08', '0.24', '0.72', '0.96'])
        self.assertListEqual(pop4.combative(), ["b"])
        self.assertListEqual(pop4.docile(), ["c"])

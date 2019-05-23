import unittest2
from count_unique_names import count_unique_names

class count_unique_names_tests(unittest2.TestCase):
    """
    Test countUniqueNames function
    """

    def test_given_examples(self):
        self.assertEqual(count_unique_names("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"), 1)
        self.assertEqual(count_unique_names("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(count_unique_names("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah"), 1)
        self.assertEqual(count_unique_names("Michele", "Egli", "Deborah", "Egli", "Michele Egli"), 2)

    def test_my_examples(self):
        self.assertEqual(count_unique_names("Elizabeth", "Egli", "Deborah", "Egli", "Michele Egli"), 3)
        self.assertEqual(count_unique_names("Elizabeth", "Egli", "", "Egli", "Michele Egli"), 3)
        self.assertEqual(count_unique_names("Brad", "Pitt", " ", "Johnson", "Pitt Brad"), 2)
        self.assertEqual(count_unique_names("dwayne", "Johnson", "Dwayne", "johnson", "Johnson Dwayne"), 1)
        self.assertEqual(count_unique_names("dwayne", "Johnson", "Dwayne", "johnson", "JOHNSON DWAYNE"), 1)


if __name__ == '__main__':
    unittest2.main()
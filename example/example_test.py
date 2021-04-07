import unittest
import pdb


class Example(unittest.TestCase):
    def setup(self):
        pass

    #def test_assert_raises(self):
    #    self.assertRaises(AttributeError, [].get)

    def test_assert_raises(self):         # Smarter way than the above
        with self.assertRaises(AttributeError):
            [].get


if __name__ == '__main__':
    exam = Example()
    exam.test_assert_raises()


import unittest


class Useful(unittest.TestCase):
    def setUp(self):
        pass

    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_almost_equal_delta_0_5(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)

    def test_assert_almost_equal_places(self):
        self.assertAlmostEqual(1, 1.00001, places=4)

    def test_assert_raises(self):
        self.assertRaises(ValueError, int, "a")

    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get



if __name__ == '__main__':
    useful = Useful()
    useful.test_assert_equal()
    useful.test_assert_almost_equal_delta_0_5()
    useful.test_assert_almost_equal_places()
    useful.test_assert_raises()
    useful.test_assert_raises_alternative()

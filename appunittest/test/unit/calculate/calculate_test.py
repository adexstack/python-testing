try:
    import unittest
    from appunittest.calculate import Calculate
except Exception as e:
    print("Some Modules are missing {}".format(e))


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_returns_failed_result(self): # Should fail
        self.assertEqual(3, self.calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")


if __name__ == '__main__':
    unittest.main()

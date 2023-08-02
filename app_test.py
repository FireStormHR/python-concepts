import unittest


class TestStringMethodsTest(unittest.TestCase):

    def test_upper_test(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper_test(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2) # type: ignore


if __name__ == '__main__':
    unittest.main()

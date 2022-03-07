import unittest
import fn_file


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fn_file.get_setting(), {'path_in': 'in', 'path_out': 'out', 'extension': 'txt'})


if __name__ == '__main__':
    unittest.main()

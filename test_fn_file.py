import unittest
import fn_file


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fn_file.get_setting(), {'path_in': 'in', 'path_out': 'out', 'extension': 'txt'})

    def test_emptyStr(self):
        str1 = '43'
        str2 = ''
        self.assertTrue(str1 is not None)
        self.assertFalse(bool(str2))


if __name__ == '__main__':
    unittest.main()

def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def division(num):
        return num/n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    run()
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):
            # Make the closure test here
            self.assertEqual(make_division_by(3)(9),3)
            self.assertEqual(make_division_by(8)(16),2)
            self.assertEqual(make_division_by(10)(50),5)
            self.assertEqual(make_division_by(20)(1000),50)
            
    unittest.main()

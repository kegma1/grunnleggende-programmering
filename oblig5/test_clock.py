from clock import Clock  # The code to test
import unittest   # The test framework

class Test_Clock(unittest.TestCase):

    def setUp(self):  # RUNS AUTOMATICALLY BEFORE EACH TEST!
        self.__clock = Clock()

    def test_set_clock_illegal_values(self):
            self.__clock.set_clock(-1,13,42, 40, 70, 80)
            self.assertEqual(str(self.__clock), "0000-01-01 00:00:00")
        
    def test_inc_sec_from_default_values(self):
            self.__clock.inc_sec()
            self.assertEqual(str(self.__clock), "0000-01-01 00:00:01")
    
    def test_inc_min_from_default_values(self):
        self.__clock.inc_min()
        self.assertEqual(str(self.__clock), "0000-01-01 00:01:00")
    
    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(2021, 1, 30, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(str(self.__clock), "2021-02-01 00:00:00")
   
    # flere test cases... :-) spesielt tip-over tilfeller

if __name__ == '__main__':
    unittest.main()
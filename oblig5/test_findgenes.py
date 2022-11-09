import unittest   # The test framework
from findgenes import *

class Test_genome(unittest.TestCase):
    def test_emty_string(self):
        result = findGenes("")
        self.assertEqual(result[0], "No genes found")    

    def test_rubbish_string(self):
        result = findGenes("I AM A STRING WITH NO GENES WHATSOEVER")
        self.assertEqual(result[0], "No genes found")

    def test_output(self):
        result = findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT ")
        self.assertEqual(result, ["TTT", "GGGCGT"])

    def test_output2(self):
        result = findGenes("AAAAATGAAAATAAATGAGGTTATAA")
        self.assertEqual(result, ["AGGTTA"]) 

    def test_two_start_seq(self):
        result = findGenes("ATGATG")
        self.assertEqual(result[0], "No genes found")   

    def test_empty_gene(self):
        result = findGenes("ATGTAA")
        self.assertEqual(result[0], "No genes found")     

if __name__ == '__main__':

    unittest.main()


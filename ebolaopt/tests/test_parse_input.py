# Python2.7
import unittest
import pylab
import numpy

from ebolaopt.parse_input import parse_data

class TestParseInput(unittest.TestCase):

    def xtest_parse_data(self):
        """Test parsing of epidemic data."""
        #XXX Testing should be more automatic and not involve plotting
        countries = ["Guinea","Liberia","Nigeria","Sierra Leone","Spain","United States"]
        for country in countries:
            days, cases = parse_data("ebolaopt/data/ebola-case-counts-and-deaths-fro.csv", country)
            pylab.plot(days, cases, 'k-o')
            pylab.xlabel("day")
            pylab.ylabel("cases")
            pylab.title(country)
            pylab.show()

    def test_parse_data_bad(self):
        self.assertRaises(ValueError, parse_data, "ebolaopt/data/ebola-case-counts-and-deaths-fro.csv", "Badinput")

if __name__ == '__main__':
    unittest.main()

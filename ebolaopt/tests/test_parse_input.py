# Python2.7
import unittest
import pylab
import numpy

from ebolaopt.parse_input import parse_data
from ebolaopt.parse_input import parse_resources

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

    def test_parse_resources(self):
        resource_dict = parse_resources("ebolaopt/data/resources.csv")
        self.assertIn("total", resource_dict.keys())
        self.assertIn("interventions", resource_dict.keys())

if __name__ == '__main__':
    unittest.main()

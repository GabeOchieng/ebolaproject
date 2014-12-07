# Python2.7
import unittest
import pylab

class TestParseInput(unittest.TestCase):

    def test_parse_data(self):
        """Test parsing of epidemic data."""
        #XXX Testing should be more automatic and not involve plotting
        from ebolaopt.parse_input import parse_data
        countries = ["Guinea","Liberia","Nigeria","Sierra Leone","Spain","United States"]
        for country in countries:
            days, cases = parse_data("ebolaopt/data/ebola-case-counts-and-deaths-fro.csv", country)
            pylab.plot(days, cases, 'k-o')
            pylab.xlabel("day")
            pylab.ylabel("cases")
            pylab.title(country)
            pylab.show()

if __name__ == '__main__':
    unittest.main()

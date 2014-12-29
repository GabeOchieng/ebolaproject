# Python2.7
import numpy
import csv
import datetime

# TODO: move this to Yile's code
def parse_data(filename, country):
    """Given the file path of the raw data csv file, extract the number of cases
    vs. time for a given country. country name should match string in csv file.
    """
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile)
        # First row
        firstrow = datareader.next()
        if country in firstrow is False:
            raise ValueError("Please enter a valid country name.")
        col_ind = firstrow.index(country)

        cases = []
        days = []
        # Iterate over subsequent rows
        for row in datareader:
            if len(row) > 1:
                count = row[col_ind]
                if count: # If it is not empty
                    count = int(count)
                    # Convert date to an integer representing days
                    day = int(datetime.datetime.strptime(row[0], '%Y-%m-%d').strftime('%j'))
                    days.append(day)
                    cases.append(count)
        days = numpy.array(days)
        cases = numpy.array(cases)

    return days, cases






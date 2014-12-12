# Python2.7
import numpy
import csv
import datetime

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


#XXX To do: map recognizable names like "drugs" to model parameter names like "delta_2"
def parse_resources(filename):
    """Parse a csv file of total budget constraint and cost of each
    intervention."""
    
    resource_dict = {"interventions":{}}
    
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile)
        # Iterate over rows
        for row in datareader:
            if row[0].lower() == "total":
                resource_dict["total"] = float(row[1])
            else:
                resource_dict["interventions"][row[0]] = (float(row[1]), float(row[2]))
    #XXX To do: check inputs

    return resource_dict



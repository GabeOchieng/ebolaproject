# Python2.7

# This code runs optimize() with all default arguments, but with
# no plotting. It profiles the code and prints the number of
# function calls and time usage for each part of the code.

import cProfile
from ebolaopt import optimize

pr = cProfile.Profile()
pr.enable()

from ebolaopt import optimize
optimize(plot=False, plot_fit=False)

pr.disable()
pr.print_stats(sort='time')

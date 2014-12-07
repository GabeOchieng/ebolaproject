Getting Started
===============

Example usage::

    myopt = ebolaopt.Optimizer() # Create a new optimizer object
    myopt.InputRawData("data_file.txt") # Input data to fit to
    myopt.InputConstraints("constraints.txt")
    myopt.InputCosts("costs.txt")
    optimum = myopt.FindOptimum(algorithm="NelderMead") # Calculate!
    myopt.OutputSteps() # Display more output info
    myopt.PlotOptimum()


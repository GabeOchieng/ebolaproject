Getting Started
===============

Example usage::

    import ebolaopt
    # Create a new optimizer object
    myopt = ebolaopt.Optimizer(data_file="case_counts.csv", constraints_file="constraints.csv")
    myopt.initialize_model() # Do the deterministic fitting
    myopt.initialize_stoch_solver() # Initialize the stochastic model
    optimum = myopt.run_optimization() # Calculate optimum allocation
    myopt.represent_allocation(optimum) # Show final result

This should print the following output::

    beta_H should get 3.34 percent of the allocation
    delta_2 should get 81.28 percent of the allocation
    theta_1 should get 15.36 percent of the allocation

In order to learn more about the epidemic trajectory, you can plot with (ADD INFO HERE)
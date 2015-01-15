.. EbolaOpt documentation master file, created by
   sphinx-quickstart on Wed Dec  3 23:05:39 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EbolaOpt's documentation!
====================================

This software package determines how to optimally allocate a given, finite 
number of resources during an Ebola virus outbreak in order to minimize the 
spread of the disease and contain the outbreak. This software package
uses a stochastic compartmental model to simulate the spread of the disease.
Given resource constraints and epidemic information, it fits the model
parameters to the epidemic data and use that model to forecast the effect of 
certain interventions on the trajectory of the disease. By modeling the effects 
of different intervention distributions, the software determines how a fixed 
quantity of resources can be allocated in order to have the greatest positive 
impact on controlling an Ebola epidemic.

For the most recent version of EbolaOpt, visit our github page at 
https://github.com/altafang/ebolaproject.

An html version of this documentation (if you are not looking at it already)
is at http://www.princeton.edu/~alta/ebolaproject/.

Contents
========

.. toctree::
   :maxdepth: 3

   background
   installation
   getting_started
   gui
   functions 
   classobjects
   warnings



.. commenting out the indices and tables thing

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`


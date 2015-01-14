Warnings and Pitfalls
=====================

Getting Different Results Each Time
-----------------------------------

On some computers, running the same optimization with the same inputs multiple
times can lead to significantly different outputs. The reason for this is that 
calculations may be performed with very small precision errors that ultimately 
lead the model fitting to different results since the optimization necessary
for model fitting is a local rather than global minimization. For more 
information, see:
http://blog.nag.com/2011/02/wandering-precision.html

Interventions Worsen The Epidemic
---------------------------------

In some situations, the simulations will demonstrate that applying 
interventions may actually worsen the epidemic and result in greater numbers 
of cases and deaths. This may arise when for example the death rate within 
the hospital is greater than outside, so that increased hospitalization leads 
to more deaths.

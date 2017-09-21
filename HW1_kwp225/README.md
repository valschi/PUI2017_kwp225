# PUI HW 1 Assignment 3

This extra credit assignment creates a reproducible research chunk of code with pseudorandom datasets. 

Using the numpy random number generator (RNG) with a defined seed, a array called ReprRandAll was populated with 50 different 2x100 numpy arrays. To obtain different means (and standard deviations) for each of the 50 arrays/datasets, the numpy RNG was used again to vary the mu and sigma with each loop iteration.

The plot function was used to plot ReprRandAll, with each of the 50 datasets represented by a different color.

For the challenge to give different mean values along the x-axis and y-axis, a nested for loop was used to iterate first through the 50 datasets, and then along the two dimensions representing the x- and y- coordinates. Within the second loop, the sigma and mu were randomized via the RNG so that the x- and y- values would have different means and standard deviations within the same dataset.
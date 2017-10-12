Reviewed Citibike project proposal for Anastasia Sagalovitch, as9788.

I was unable to run the notebook (possibly an issue on my end with the environmental variable…) and there weren’t any rendered tables or plots in the uploaded notebook on GitHub. But the idea/hypothesis is straightforward, and the code is straightforward enough so that I could understand what was supposed to happen.

The idea that there are more trips during the summer than the winter makes sense intuitively. However, the null hypothesis is formulated incorrectly - we want the null hypothesis to be rejected as a result of the analysis. The current null hypothesis (the number of riders in July 2016 is greater than or equal to the number of riders in January 2016) should be reversed with the alternative hypothesis so that we are testing (and hopefully rejecting) the complement of the original idea. 

In addition, I think the hypotheses should be formulated in a way so that there is a ratio or proportion being compared rather than sample totals. An alternative hypothesis formulation could be something like:
Null: The average number of weekly rides in July is less than or equal to the average number of weekly rides in January.
Alternative: The average number of weekly rides in July is greater to the average number of weekly rides in January.

For that formulation, I would suggest using a z-test to compare the means - the data is non-parametric and unpaired.

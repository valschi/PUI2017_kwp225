### Kent Pan
### PUI HW 2

Part 1:
I worked on both Part 1 and Part 2 individually. Writing the beginning of the script was straightforward by referencing the examples that were available to us through the class materials. After accessing the MTA API, it took some time to understand the JSON format - using an online JSON formatter was extremely helpful in understanding the data. After this step, it was fairly straightforward to write the for loop necessary to go through the bus data and print the information for each active bus (bus ID, latitude, and longitude).

Part 2:
The beginning of Part 2 was nearly identical to Part 1, and my conceptual approach to the problem was very similar to Part 1 as well. After taking some time to understand what was required, I started testing my code by printing the data like in Part 1 before tackling the output/csv portion. After that, I realized that I could replace the print function with a “write to csv” function to get the output file. I used the try/except function in my file writing code since that was what was recommended to us (and what I used) in the USCL exercises. From this I realized that I could use the same concept to capture the “N/A” cases that would normally cause errors.

Part 3:
For Part 3, Sam Ovenshine helped me find the link to the available datasets through the Urban Profiler while the Data Facility was down. From here, I accessed the dataset I was interested in and assigned the data to a pandas data frame, which was then plotted. I worked mostly independently while writing the code, but discussed some issues/errors that I ran into with Valeria Schiavon and Matt Sauter while I was working, particularly with the dataframe plot method.

Extra Credit:
This was nearly identical to Part 3, although there were some difficulties with working the date/time data since they were strings and not datetime objects. I worked closely with Matt Sauter and Matt Dwyer while writing the code to troubleshoot the code and plot the data.
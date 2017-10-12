Part 1:
I worked on this part individually to evaluate someone else’s Citibike project proposal. The file was submitted to the original repository as a pull request, and is also included in the folder here for reference.

Part 2:
I worked on this part in a group with Valeria Schiavon and Alex Shannon. We each looked for a separate test to fill the tables and coordinated the results.

| **Statistical Analyses        |  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi square        | 1, Gender | categorical | 1, colour choice for overlay| categorical | 0 | NA |         Does gender influence the choice of colour of overlays or PTLs of patients with Visual Stress? | Gender does not influence choice of colour | 0.05 assumed, based on that (Chi-square 6.46, p = 0.040) and (Chi-square 0.788, p = 0.674) | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0163326 |
  |||||||||


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Multivariate Regression	| 3, precipitation, wind speed, relative humidity | Ordinal | 1, Vegetative Coverage| Ordinal | Soil profile, sunshine hours, minimum temp, max temp | Categorical | Do climate factors effect vegetation coverage in Northwest China? | vegetation coverage in areas with higher precipitation <= vegetation coverage in areas with lower precipitation | 0.05 | [Trend Patterns of Vegetative Coverage and Their Underlying Causes in the Deserts of Northwest China over 1982 – 2008](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0126044) |
  |||||||||


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Logistic Regression	| 3, susceptible groups (elderly, respiratory condition, cardiovascular condition) | Categorical | 1, activity change| Ordinal | 5 (gender, race, education, smoking, and body mass index) | Categorical | Does poor air quality cause people with susceptible conditions to change their activity? | Percentage of people who changed activities due to air quality <= 0 | 0.05 | [Activity Change in Response to Bad Air Quality, National Health and Nutrition Examination Survey, 2007–2010](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0050526) |
  |||||||||



Part 3:
This part involved performing two statistical tests (z-test and chi-squared test) with the provided numbers in the table. I worked on this mostly individually, and had some help from Matt Sauter in understanding the chi-squared test and checking my values.

Part 4:
This part involved testing the Citibike data to look for correlations in the sample data. We looked for correlations in the trip duration of bikers who ride during the day vs night, and in the age of bikers for trips originating in Manhattan vs Brooklyn. The biggest challenge was wrangling and processing the provided data into a format that could be tested with the scipy functions, and then understanding what the scipy functions tested for in order to evaluate the results. In this section, I coded independently but discussed questions throughout with Davey Ives, Matt Dwyer, and Valeria Schiavon. In addition, Matt Sauter helped me understand how to approximate the borough delineations via latitude/longitude boundaries.
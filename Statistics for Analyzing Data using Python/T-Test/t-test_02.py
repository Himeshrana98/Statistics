# Consider another example with huge data
## ages of the college students (population)
### class student mean of all the ages


import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)  # For reproducibility
school_ages = stats.poisson.rvs(loc=18,mu=35,size=1500)  # Simulating ages of 1500 students
classA_ages = stats.poisson.rvs(loc=18,mu=30,size=60)  # Simulating ages of 60 students in Class A
print("school_ages", (school_ages))
#school_ages # [ 18  19  20 ...  51  52  53]
print("classA_ages", (classA_ages))
#classA_ages # [ 18  19  20 ...  51  52  53]
print("classA_ages mean:", np.mean(classA_ages))
# classA_ages mean: 46.9


result = stats.ttest_1samp(classA_ages, popmean=np.mean(school_ages))
print("t-statistic:", result[0], "p_value:", result[1])
# t-statistic: -9.604796510704091 p-value: 1.139027071016194e-13
# The t-statistic is negative, indicating that the sample mean is less than the population mean.
# The p-value is less than 0.05, which means we reject the null hypothesis

if result.pvalue < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
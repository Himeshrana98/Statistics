## T-Test

ages = [23, 25, 31, 29, 22, 24, 30, 28, 27, 26]

import numpy as np

ages_mean = np.mean(ages)
print("Mean age:", ages_mean)
# mean age: 26.5

sample_size = 6
age_sample = np.random.choice(ages,sample_size)
print("Sampled ages:", age_sample)
 # Sampled ages: [26 22 31 25 27 26]

np.mean(age_sample)
# mean of sampled ages: 26.166666666666668

from scipy import stats
t_stat, p_value = stats.ttest_1samp(age_sample,30)
print("t-statistic:", t_stat, "p-value:", p_value)
# t-statistic: -1.0954451150103321 p-value: 0.3263462029087193
# The t-statistic is negative, indicating that the sample mean is less than the population mean of 30.  
# accepting the null hypothesis that the true mean is 30.
# The p-value is greater than 0.05, which means we do not reject the null hypothesis.


t_stat, p_value = stats.ttest_1samp(age_sample,31)
print("t-statistic:", t_stat, "p-value:", p_value)
# t-statistic: -1.7320508075688772 p-value: 0.1341640786499874
# The t-statistic is negative, indicating that the sample mean is less than the population mean of 31.
# The p-value is greater than 0.05, which means we do not reject the null hypothesis.


t_stat, p_value = stats.ttest_1samp(age_sample,28)
print("t-statistic:", t_stat, "p-value:", p_value)
# t-statistic: -0.3651483716701107 p-value: 0.7240780980520524
# The t-statistic is negative, indicating that the sample mean is less than the population mean of 28.
# The p-value is greater than 0.05, which means we do not reject the null hypothesis.


t_stat, p_value = stats.ttest_1samp(age_sample,26)
print("t-statistic:", t_stat, "p-value:", p_value)
# t-statistic: -1.7320508075688772 p-value: 0.1341640786499874
# The t-statistic is negative, indicating that the sample mean is less than the population mean of 26.
# The p-value is greater than 0.05, which means we do not reject the null hypothesis.

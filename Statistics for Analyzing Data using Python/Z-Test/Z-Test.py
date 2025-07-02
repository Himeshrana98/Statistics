# Suppose the IQ in a population is normally distributed with a mean of 100 and a standard deviation of 15.
## A Researcher want to know if the new drug affects IQ Levels, he took a sample of 30 individual patientsand try to record their IQ levels.
### The following code shows how to perform a one sample z-test in Python to determine if the new drug causes a new significant difference in IQ levels:


from statsmodels.stats.weightstats import ztest as ztest
# Sample IQ levels of 30 individuals
sample_iq = [102, 98, 101, 97, 105, 99, 100, 103, 96, 104,
              101, 98, 102, 100, 99, 105, 97, 103, 101, 100,
              98, 102, 104, 99, 100, 101, 97, 105, 98, 102]
ztest(sample_iq, value = 100)
print("Z-test statistic and p-value:", ztest(sample_iq, value = 100))
# here p-value is the probability of observing a test statistic as extreme as the one computed, under the null hypothesis that the population mean IQ is 100.
# If the p-value is less than the significance level (commonly 0.05), we reject the null hypothesis and conclude that the new drug has a significant effect on IQ levels.
# Note: The z-test is appropriate here because the sample size is large (n > 30) and the population standard deviation is known.
# If the p-value is greater than S.D.= 0.05, we fail to reject the null hypothesis and conclude that there is no significant effect of the new drug on IQ levels.
# z-test statistics and p-value: ((np.float64(1.189735415853673), np.float64(0.23415040083484984))
# p-value is less than 0.05, we reject the null hypothesis and conclude that the new drug has a significant effect on IQ levels.

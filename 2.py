from RandomNumbers import *
from scipy import stats
from scipy.stats import weibull_min
import numpy as np


def getRandomNumbers(size, seed):
    np.random.seed(seed)
    list = np.random.uniform(0, 1, size)
    return list


rn = getRandomNumbers(500, 1)

blade = normalDistribution(rn, 42000, 663)
pitch = normalDistribution(rn, 84534, 506)
gearbox = logarithmicNormalDistribution(rn, 11, 1.2)
brake = exponentialDistribution(rn, 120000, 0)
frequency = exponentialDistribution(rn, 45000, 0)
generator = weibullDistribution(rn, 1.2, 76000, 0)
lubrication = weibullDistribution(rn, 1.3, 66000, 0)
electrical = weibullDistribution(rn, 1.5, 35000, 0)
yaw = extremeDistribution(rn, 65000, 370)

minimumData = []

for i in range(500):
    tempArray = list()
    tempArray.append(blade[i])
    tempArray.append(pitch[i])
    tempArray.append(gearbox[i])
    tempArray.append(brake[i])
    tempArray.append(frequency[i])
    tempArray.append(generator[i])
    tempArray.append(lubrication[i])
    tempArray.append(electrical[i])
    tempArray.append(yaw[i])

    minimumData.append(min(tempArray))

print('Normal')
mean_Normal, sd_Normal = normalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_Normal}, SD:  {sd_Normal}")

print()

print('Logarithmic Normal')
mean_Logarithmic, sd_Logarithmic = logarithmicNormalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_Logarithmic}, SD:  {sd_Logarithmic}")

print()

print('Exponential')
mean_Exponential = exponentialDistributionParam(minimumData)
print('Estimation:')
print(f"Mean:  {mean_Exponential}")

print()

print('Weibull')
n,m = weibullDistributionParams(minimumData, 1.3)
print('Estimation:')
print(f"N:  {n}, M: {m}")

print()

print('Extreme maximum value')
locMax, scaleMax = extremeDistributionParams(minimumData)
print('Estimation:')
print(f"Loc:  {locMax}, Scale: {scaleMax}")

print()

print('Extreme minimum value')
locMin, scaleMin = extremeMinDistributionParams(minimumData)
print('Estimation:')
print(f"Loc:  {locMin}, Scale: {scaleMin}")

print()

#2.2

#H0 - same distribution
#H1 - different distribution

print("Anderson-Darling test")
normalDisAndersonTest = stats.anderson(minimumData, 'norm')
print(f"normal {normalDisAndersonTest}")

print()

logNormalDisAndersonTest = stats.anderson(minimumData, 'logistic')
print(f"logarithmic normal {logNormalDisAndersonTest}")

print()

exponentialDisAndersonTest = stats.anderson(minimumData, 'expon')
print(f"exponential {exponentialDisAndersonTest}")

print()

# extremeDisAndersonTest = stats.anderson(minimumData, 'gumbel')
# print(f"gumbel {extremeDisAndersonTest}")
#
# print()

# weibull_values = weibullDistribution(getRandomNumbers(500, 1),m,n, 0)
# weibullDisAndersonTest = stats.anderson_ksamp([minimumData,weibull_values])
# print(f"weibull {weibullDisAndersonTest}")
#
# print()
#
# gumbilMin_values = extremeDistribution(getRandomNumbers(500, 1),locMin, scaleMin)
# gumbilMinAndersonTest = stats.anderson_ksamp([minimumData,gumbilMin_values])
# print(f"gumbilMin {gumbilMinAndersonTest}")
#
# print()
#
# gumbilMax_values = extremeDistribution(getRandomNumbers(500, 1),locMax, scaleMax)
# gumbilMaxAndersonTest = stats.anderson_ksamp([minimumData,gumbilMax_values])
# print(f"gumbilMax {gumbilMaxAndersonTest}")
#
# print()
#
# normal_values = normalDistribution(getRandomNumbers(500, 1),mean_Normal, sd_Normal)
# normalAndersonTest = stats.anderson_ksamp([minimumData,normal_values])
# print(f"normal {normalAndersonTest}")
#
# logarithmic_values = logarithmicNormalDistribution(getRandomNumbers(500, 1),mean_Logarithmic, sd_Logarithmic)
# logarithmicAndersonTest = stats.anderson_ksamp([minimumData,logarithmic_values])
# print(f"logarithmic {logarithmicAndersonTest}")
#
# exponential_values = exponentialDistribution(getRandomNumbers(500, 1),mean_Exponential, 0)
# exponentialAndersonTest = stats.anderson_ksamp([minimumData,exponential_values])
# print(f"logarithmic {exponentialAndersonTest}")
#
#
# print()
#
# print("Kolmogorov-Smirnov test")
#
# print("normal" , stats.stats.ks_2samp(minimumData,normal_values))
# print()
# print("logarithmic" , stats.stats.ks_2samp(minimumData,logarithmic_values))
# print()
# print("weibull" , stats.stats.ks_2samp(minimumData,weibull_values))
# print()
# print("exponential" , stats.stats.ks_2samp(minimumData,exponential_values))
# print()
# print("gumbel_max" , stats.stats.ks_2samp(minimumData,gumbilMax_values))
# print()
# print("gumbel_min", stats.stats.ks_2samp(minimumData,gumbilMin_values))

# normalDisSmirnovTest = stats.kstest(minimumData, 'norm', args=(mean_Normal, sd_Normal), N=500)
# print(f"normal {normalDisSmirnovTest}")
#
# exponentialDisSmirnovTest = stats.kstest(minimumData, np.random.exponential(scale=mean_Exponential, size=500), N=500)
# ks_exp_test = stats.kstest(min_dist_vector, np.random.exponential(scale=exponential_estimate_mean, size=500), N=500)
#
# print(f"exponential {exponentialDisSmirnovTest}")
#
# logarithmicDisSmirnovTest = stats.kstest(minimumData, np.random.lognormal(scale=mean_Logarithmic, sigma=sd_Logarithmic, size=500), N=500)
# print(f"logarithmic {logarithmicDisSmirnovTest}")
#
# weibullDisSmirnovTest = stats.kstest(minimumData, weibull_min.rvs(m, loc=1.3, scale=n, size=500), N=500)
# print(f"weibull {weibullDisSmirnovTest}")
#
# gumbelMaxDisSmirnovTest = stats.kstest(minimumData, np.random.gumbel(loc=locMax, scale=scaleMax, size=500), N=500)
# print(f"gumbel Max {gumbelMaxDisSmirnovTest}")
#
# gumbelMinDisSmirnovTest = stats.kstest(minimumData, np.random.gumbel(loc=locMin, scale=scaleMin, size=500), N=500)
# print(f"gumbel Min {gumbelMinDisSmirnovTest}")
# print()

print("Chi-square test")

print("normal distribution:")
NormalDisChiSqTest = stats.chisquare(minimumData,
                                  np.random.normal(loc=mean_Normal, scale=sd_Normal, size=500))
print(f"normal {NormalDisChiSqTest}")
print("")

print("logarithmic distribution:")
logNormalDisChiSqTest = stats.chisquare(minimumData,
                               np.random.lognormal(mean=mean_Logarithmic, sigma=sd_Logarithmic,
                                                   size=500))
print(f"logarithmic {logNormalDisChiSqTest}")
print("")

print("exponential distribution:")
exponentialDisChiSqTest = stats.chisquare(minimumData, np.random.exponential(scale=mean_Exponential, size=500))
print(f"exponential {exponentialDisChiSqTest}")
print("")

print("weibull distribution:")
weibullDisChiSqTest = stats.chisquare(minimumData,
                              weibull_min.rvs(m, loc=1.3, scale=n,
                                              size=500))
print(f"weibull {weibullDisChiSqTest}")

print("")

print("gumbel max distribution:")
gumbellMaxDisChiSqTest = stats.chisquare(minimumData,
                                      np.random.gumbel(loc=locMax, scale=scaleMax,
                                                       size=500))
print(f"gumbel max {gumbellMaxDisChiSqTest}")
print("")

print("gumbel min distribution:")
gumbellMinDisChiSqTest = stats.chisquare(minimumData,
                                      np.random.gumbel(loc=locMin, scale=scaleMin,
                                                       size=500))
print(f"gumbel min {gumbellMinDisChiSqTest}")
print("")




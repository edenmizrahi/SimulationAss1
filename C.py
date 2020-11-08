
from RandomNumbers import *
from random import *
import numpy as np

def randomNumbers(size, seed):
    np.random.seed(seed)
    list = np.random.uniform(0, 1, size)
    return list

def ExponentialComparison(u):
    # Random 500 values for each distribution with seed=0.5
    exponentialList1 = exponentialDistribution(randomNumbers(500,1),u,0)
    exponentialParam1 = exponentialDistributionParam(exponentialList1)
    print(f"Mean:  {exponentialParam1}")
    print(f"Distribution rate:  {exponentialParam1/u}")

    #Random 500 more values for each distribution with seed=0.5
    exponentialList2 = exponentialDistribution(randomNumbers(500,1),u,0)
    exponentialParam2 = exponentialDistributionParam(exponentialList2)
    print(f"Mean:  {exponentialParam2}")
    print(f"Distribution rate:  {exponentialParam2/u}")

    #Random 500 more values for each distribution with other seed=0.8
    exponentialList3 = exponentialDistribution(randomNumbers(500,5),u,0)
    exponentialParam3 = exponentialDistributionParam(exponentialList3)
    print(f"Mean:  {exponentialParam3}")
    print(f"Distribution rate:  {exponentialParam3/u}")

    #Random 10000 more values for each distribution with seed=1
    exponentialList4 = exponentialDistribution(randomNumbers(10000,10), u, 0)
    exponentialParam4 = exponentialDistributionParam(exponentialList4)
    print(f"Mean:  {exponentialParam4}")
    print(f"Distribution rate:  {exponentialParam4/u}")

def NormalComparison(u,sd):

    # Random 500 values for each distribution with seed=1
    #NormalList1 = normalDistribution(random500, u, sd)
    NormalList1 = normalDistribution(randomNumbers(500,1), u, sd)
    mean1, sd1 = normalDistributionParams(NormalList1)
    print(f"Mean:  {mean1}, SD:  {sd1}")
    print(f"Distribution rate:  mean:{mean1 / u}, sd:{sd1 / sd}")
    #Random 500 more values for each distribution with seed=5
    #NormalList2 = normalDistribution(firstRandom500, u, sd)
    NormalList2 = normalDistribution(randomNumbers(500,1), u, sd)
    mean2, sd2 = normalDistributionParams(NormalList2)
    print(f"Mean:  {mean2}, SD:  {sd2}")
    print(f"Distribution rate:  mean:{mean2 / u}, sd:{sd2 / sd}")
    #Random 500 more values for each distribution with other seed=10
    #NormalList3 = normalDistribution(secondRandom500, u, sd)
    NormalList3 = normalDistribution(randomNumbers(500,5), u, sd)
    mean3, sd3 = normalDistributionParams(NormalList3)
    print(f"Mean:  {mean3}, SD:  {sd3}")
    print(f"Distribution rate:  mean:{mean3 / u}, sd:{sd3 / sd}")

    #Random 10000 more values for each distribution with seed=1
    #NormalList4 = normalDistribution(thirdRandom10000, u, sd)
    NormalList4 = normalDistribution(randomNumbers(10000,5), u, sd)
    mean4, sd4 = normalDistributionParams(NormalList4)
    print(f"Mean:  {mean4}, SD:  {sd4}")
    print(f"Distribution rate:  mean:{mean4 / u}, sd:{sd4 / sd}")

def LogarithmicNormalComparison(u,sd):

    # Random 500 values for each distribution with seed=1
    NormalList1 = logarithmicNormalDistribution(randomNumbers(500,1), u, sd)
    mean1, sd1 = logarithmicNormalDistributionParams(NormalList1)
    print(f"Mean:  {mean1}, SD:  {sd1}")
    print(f"Distribution rate:  mean:{mean1 / u}, sd:{sd1 / sd}")

    #Random 500 more values for each distribution with seed=1
    NormalList2 = logarithmicNormalDistribution(randomNumbers(500,1), u, sd)
    mean2, sd2 = logarithmicNormalDistributionParams(NormalList2)
    print(f"Mean:  {mean2}, SD:  {sd2}")
    print(f"Distribution rate:  mean:{mean2 / u}, sd:{sd2 / sd}")

    #Random 500 more values for each distribution with other seed=5
    NormalList3 = logarithmicNormalDistribution(randomNumbers(500,5), u, sd)
    mean3, sd3 = logarithmicNormalDistributionParams(NormalList3)
    print(f"Mean:  {mean3}, SD:  {sd3}")
    print(f"Distribution rate:  mean:{mean3 / u}, sd:{sd3 / sd}")

    #Random 10000 more values for each distribution with seed=10
    NormalList4 = logarithmicNormalDistribution(randomNumbers(10000,5), u, sd)
    mean4, sd4 = logarithmicNormalDistributionParams(NormalList4)
    print(f"Mean:  {mean4}, SD:  {sd4}")
    print(f"Distribution rate:  mean:{mean4 / u}, sd:{sd4 / sd}")

def ExtremeComparison(u,sd):

    # Random 500 values for each distribution with seed=1
    # ExtremeList1 = extremeDistribution(random500, u, sd)
    ExtremeList1 = extremeDistribution(randomNumbers(500, 1), u, sd)
    mean1, sd1 = extremeDistributionParams(ExtremeList1)
    print(f"Mean:  {mean1}, SD:  {sd1}")
    print(f"Distribution rate:  mean:{(mean1 / u)*100}, sd:{(sd1 / sd)*100}")

    #Random 500 more values for each distribution with seed=1
    #ExtremeList2 = extremeDistribution(firstRandom500, u, sd)
    ExtremeList2 = extremeDistribution(randomNumbers(500,1), u, sd)
    mean2, sd2 = extremeDistributionParams(ExtremeList2)
    print(f"Mean:  {mean2}, SD:  {sd2}")
    print(f"Distribution rate:  mean:{(mean2 / u)*100}, sd:{(sd2 / sd)*100}")

    #Random 500 more values for each distribution with other seed=5
    #ExtremeList3 = extremeDistribution(secondRandom500, u, sd)
    ExtremeList3 = extremeDistribution(randomNumbers(500,5), u, sd)
    mean3, sd3 = extremeDistributionParams(ExtremeList3)
    print(f"Mean:  {mean3}, SD:  {sd3}")
    print(f"Distribution rate:  mean:{(mean3 / u)*100}, sd:{(sd3 / sd)*100}")

    #Random 10000 more values for each distribution with seed=10
    #ExtremeList4 = extremeDistribution(thirdRandom10000, u, sd)
    ExtremeList4 = extremeDistribution(randomNumbers(10000,5), u, sd)
    mean4, sd4 = extremeDistributionParams(ExtremeList4)
    print(f"Mean:  {mean4}, SD:  {sd4}")
    print(f"Distribution rate:  mean:{(mean4 / u)*100}, sd:{(sd4 / sd)*100}")

def WeibullComparison(n, m, t0):

    # Random 500 values for each distribution with seed=1
    #WeibullList1 = weibullDistribution(random500, m, n, t0)
    WeibullList1 = weibullDistribution(randomNumbers(500,1), m, n, t0)
    n1, m1 = weibullDistributionParams(WeibullList1, m)
    print(f"scale:  {n1}, shape:  {m1}")
    print(f"Distribution rate:  scale:{n1 / n}, shape:{m1 / m}")

    #Random 500 more values for each distribution with seed=1
    #WeibullList2 = weibullDistribution(firstRandom500, m, n, t0)
    WeibullList2 = weibullDistribution(randomNumbers(500,1), m, n, t0)
    n2, m2 = weibullDistributionParams(WeibullList2, m)
    print(f"scale:  {n2}, shape:  {m2}")
    print(f"Distribution rate:  scale:{n2 / n}, shape:{m2 / m}")

    #Random 500 more values for each distribution with other seed=5
    #WeibullList3 = weibullDistribution(secondRandom500, m, n, t0)
    WeibullList3 = weibullDistribution(randomNumbers(500,5), m, n, t0)
    n3, m3 = weibullDistributionParams(WeibullList3, m)
    print(f"scale:  {n3}, shape:  {m3}")
    print(f"Distribution rate:  scale:{n3 / n}, shape:{m3 / m}")

    #Random 10000 more values for each distribution with seed=10
    #WeibullList4 = weibullDistribution(thirdRandom10000, m, n, t0)
    WeibullList4 = weibullDistribution(randomNumbers(10000,10), m, n, t0)
    n4, m4 = weibullDistributionParams(WeibullList4, m)
    print(f"scale:  {n4}, shape:  {m4}")
    print(f"Distribution rate:  scale:{n4 / n}, shape:{m4 / m}")


############## Exponential ######################
print()
print('Brake System - Exponential')
print('Mean: 120,000')
print()
ExponentialComparison(120000)
print()
print('Frequency converter - Exponential')
print('Mean: 45,000')
print()
ExponentialComparison(45000)

############## Normal ######################
print()
print('Blade - normal')
print('Mean: 42000, SD: 663')
print()
NormalComparison(42000,663)
print()
print('Pitch Control System - normal')
print('Mean: 84534, SD: 506')
print()
NormalComparison(84534,506)

##############Gearbox - Logarithmic Normal######################
print()
print('Gearbox - Logarithmic Normal')
print('Mean: 11, SD: 1.2')
print()
LogarithmicNormalComparison(11,1.2)
##############Yaw system - Extreme maximum value######################
print()
print('Yaw system - Extreme maximum value')
print('Location: 65,000, Scale: 370')
print()
ExtremeComparison(65000,370)

############## Weibull ######################
print()
print('Generator - Weibull')
print('Scale: 76,000, Shape: 1.2')
print()
WeibullComparison(76000,1.2, 0)

print()
print('Lubrication system - Weibull')
print('Scale: 66,000, Shape: 1.3')
print()
WeibullComparison(66000,1.3, 0)

print()
print('Electrical system - Weibull')
print('Scale: 35,000, Shape: 1.5')
print()
WeibullComparison(35000,1.5, 0)

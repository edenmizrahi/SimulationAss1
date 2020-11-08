from RandomNumbers import *
from scipy import stats


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
mean_blade, sd_blade = normalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_blade}, SD:  {sd_blade}")

print()

print('Logarithmic Normal')
mean_gearbox, sd_gearbox = logarithmicNormalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_gearbox}, SD:  {sd_gearbox}")

print()

print('Exponential')
mean_brake = exponentialDistributionParam(minimumData)
print('Estimation:')
print(f"Mean:  {mean_brake}")

print()

print('Weibull')
mean_lubrication = weibullDistributionParams(minimumData, 1.3)
print('Estimation:')
print(f"Mean:  {mean_lubrication}")

print()

print('Extreme maximum value')
mean_yaw = extremeDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_yaw}")

print()

print('Extreme minimum value')
mean_yaw = extremeMinDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_yaw}")



#2.2

#H0 - same distribution
#H1 - different distribution

# Chi-square test

print("Anderson-Darling test")
normalDisAndersonTest = stats.anderson(minimumData, 'norm')
print(f"normal {normalDisAndersonTest}")

logNormalDisAndersonTest = stats.anderson(minimumData, 'logistic')
print(f"logarithmic normal {logNormalDisAndersonTest}")

exponentialDisAndersonTest = stats.anderson(minimumData, 'expon')
print(f"exponential {exponentialDisAndersonTest}")

extremeDisAndersonTest = stats.anderson(minimumData, 'gumbel')
print(f"exponential {extremeDisAndersonTest}")

#weibullDisAndersonTest = stats.anderson_ksamp([minimumData,weibull_values])
#print(f"weibull {weibullDisAndersonTest}")

print("")

print("Kolmogorov-Smirnov test")
normalDisSmirnovTest = stats.kstest(minimumData, 'norm', args=(mean_blade, sd_blade), N=500)
print(f"normal {normalDisSmirnovTest}")

exponentialDisSmirnovTest = stats.kstest(minimumData, np.random.exponential(scale=mean_brake, size=500), N=500)
print(f"exponential {normalDisSmirnovTest}")

print("Chi-square test")
print("normal distribution:")

print("")
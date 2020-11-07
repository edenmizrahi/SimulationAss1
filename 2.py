from RandomNumbers import *

rn = randomNumbers(0.5, 500)

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

print('Blade - normal')
print('Mean: 42000, SD: 663')
mean_blade, sd_blade = normalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_blade}, SD:  {sd_blade}")

print()

print('Pitch Control System - normal')
print('Mean: 84534, SD: 506')
mean_pitch, sd_pitch = normalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_pitch}, SD:  {sd_pitch}")

print()

print('Gearbox - Logarithmic Normal')
print('Mean: 11, SD: 1.2')
mean_gearbox, sd_gearbox = logarithmicNormalDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_gearbox}, SD:  {sd_gearbox}")

print()

print('Brake System - Exponential')
print('Mean: 120,000')
mean_brake = exponentialDistributionParam(minimumData)
print('Estimation:')
print(f"Mean:  {mean_brake}")

print()

print('Frequency converter - Exponential')
print('Mean: 45,000')
mean_frequency = exponentialDistributionParam(minimumData)
print('Estimation:')
print(f"Mean:  {mean_frequency}")

print()

print('Generator - Weibull')
print('Scale: 76,000, Shape: 1.2')
mean_generator = weibullDistributionParams(minimumData, 1.2)
print('Estimation:')
print(f"Mean:  {mean_generator}")

print()

print('Lubrication system - Weibull')
print('Scale: 66,000, Shape: 1.3')
mean_lubrication = weibullDistributionParams(minimumData, 1.3)
print('Estimation:')
print(f"Mean:  {mean_lubrication}")

print()

print('Electrical system - Weibull')
print('Scale: 35,000, Shape: 1.5')
mean_electrical = weibullDistributionParams(minimumData, 1.5)
print('Estimation:')
print(f"Mean:  {mean_electrical}")

print()

print('Yaw system - Extreme maximum value')
print('Location: 65,000, Scale: 370')

mean_yaw = extremeDistributionParams(minimumData)
print('Estimation:')
print(f"Mean:  {mean_yaw}")
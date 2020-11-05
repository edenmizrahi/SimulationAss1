from RandomNumbers import *
import chaospy

#50 numbers
uniform = chaospy.Uniform(0,1)
random50 = uniform.sample(50, rule='halton')
#200 numbers
uniform = chaospy.Uniform(0,1)
random200 = uniform.sample(200, rule='halton')
#500 numbers
uniform = chaospy.Uniform(0,1)
random500 = uniform.sample(500, rule='halton')


##############blade - normal######################

print('Blade - normal')
print('Mean: 42000, SD: 663')
print()
#50
bladeList50 = normalDistribution(random50, 42000, 663)
mean_blade50,sd_blade50= normalDistributionParams(bladeList50)
print('50 numbers')
print('Estimation:')
print(f"Mean:  {mean_blade50}, SD:  {sd_blade50}")
#200
bladeList200 = normalDistribution(random200, 42000, 663)
mean_blade200,sd_blade200= normalDistributionParams(bladeList200)
print('200 numbers')
print('Estimation:')
print(f"Mean:  {mean_blade200}, SD:  {sd_blade200}")
#500
bladeList500 = normalDistribution(random500, 42000, 663)
mean_blade500,sd_blade500= normalDistributionParams(bladeList500)
print('500 numbers')
print('Estimation:')
print(f"Mean:  {mean_blade500}, SD:  {sd_blade500}")

##############Pitch Control System - normal######################
print()
print('Pitch Control System - normal')
print('Mean: 84534, SD: 506')
print()
#50
pitchList50 = normalDistribution(random50, 84534, 506)
mean_pitch50,sd_pitch50= normalDistributionParams(pitchList50)
print('50 numbers')
print('Estimation:')
print(f"Mean:  {mean_pitch50}, SD:  {sd_pitch50}")
#200
pitchList200 = normalDistribution(random200, 84534, 506)
mean_pitch200,sd_pitch200= normalDistributionParams(pitchList200)
print('200 numbers')
print('Estimation:')
print(f"Mean:  {mean_pitch200}, SD:  {sd_pitch200}")
#500
pitchList500 = normalDistribution(random500, 84534, 506)
mean_pitch500,sd_pitch500= normalDistributionParams(pitchList500)
print('500 numbers')
print('Estimation:')
print(f"Mean:  {mean_pitch500}, SD:  {sd_pitch500}")

##############Gearbox - Logarithmic Normal######################
print()
print('Gearbox - Logarithmic Normal')
print('Mean: 11, SD: 1.2')
print()
#50
gearboxList50 = logarithmicNormalDistribution(random50, 11, 1.2)
mean_gearbox50,sd_gearbox50= logarithmicNormalDistributionParams(gearboxList50)
print('50 numbers')
print('Estimation:')
print(f"Mean:  {mean_gearbox50}, SD:  {sd_gearbox50}")
#200
gearboxList200 = logarithmicNormalDistribution(random200, 11, 1.2)
mean_gearbox200,sd_gearbox200= logarithmicNormalDistributionParams(gearboxList200)
print('200 numbers')
print('Estimation:')
print(f"Mean:  {mean_gearbox200}, SD:  {sd_gearbox200}")
#500
gearboxList500 = logarithmicNormalDistribution(random500, 11, 1.2)
mean_gearbox500,sd_gearbox500= logarithmicNormalDistributionParams(gearboxList500)
print('500 numbers')
print('Estimation:')
print(f"Mean:  {mean_gearbox500}, SD:  {sd_gearbox500}")

##############Brake System - Exponential######################
print()
print('Brake System - Exponential')
print('Mean: 120,000')
print()
#50
brakeList50 = exponentialDistribution(random50, 120000, 0)
mean_brake50= exponentialDistributionParam(brakeList50)
print('50 numbers')
print('Estimation:')
print(f"Mean:  {mean_brake50}")
#200
brakeList200 = exponentialDistribution(random200, 120000, 0)
mean_brake200= exponentialDistributionParam(brakeList200)
print('200 numbers')
print('Estimation:')
print(f"Mean:  {mean_brake200}")
#500
brakeList500 = exponentialDistribution(random500, 120000, 0)
mean_brake500= exponentialDistributionParam(brakeList500)
print('500 numbers')
print('Estimation:')
print(f"Mean:  {mean_brake500}")

##############Frequency converter - Exponential######################
print()
print('Frequency converter - Exponential')
print('Mean: 45,000')
print()
#50
frequencyList50 = exponentialDistribution(random50, 45000, 0)
mean_frequency50= exponentialDistributionParam(frequencyList50)
print('50 numbers')
print('Estimation:')
print(f"Mean:  {mean_frequency50}")
#200
frequencyList200 = exponentialDistribution(random200, 45000, 0)
mean_frequency200= exponentialDistributionParam(frequencyList200)
print('200 numbers')
print('Estimation:')
print(f"Mean:  {mean_frequency200}")
#500
frequencyList500 = exponentialDistribution(random500, 45000, 0)
mean_frequency500= exponentialDistributionParam(frequencyList500)
print('500 numbers')
print('Estimation:')
print(f"Mean:  {mean_frequency500}")

##############Generator - Weibull######################
print()
print('Generator - Weibull')
print('Scale: 76,000, Shape: 1.2')
print()
#50
generatorList50 = weibullDistribution(random50, 1.2, 76000, 0)
#mean_generator50= weibullDistributionParams(generatorList50)
print('50 numbers')
print('Estimation:')
#print(f"Mean:  {mean_generator50}")
#200
generatorList200 = weibullDistribution(random200, 1.2, 76000, 0)
#mean_generator200= weibullDistributionParams(generatorList200)
print('200 numbers')
print('Estimation:')
#print(f"Mean:  {mean_generator200}")
#500
generatorList500 = weibullDistribution(random500, 1.2, 76000, 0)
#mean_generator500= weibullDistributionParams(generatorList500)
print('500 numbers')
print('Estimation:')
#print(f"Mean:  {mean_generator500}")

##############Lubrication system - Weibull######################
print()
print('Lubrication system - Weibull')
print('Scale: 66,000, Shape: 1.3')
print()
#50
lubricationList50 = weibullDistribution(random50, 1.3, 66000, 0)
#mean_lubrication50= weibullDistributionParams(lubricationList50)
print('50 numbers')
print('Estimation:')
#print(f"Mean:  {mean_lubrication50}")
#200
lubricationList200 = weibullDistribution(random200, 1.3, 66000, 0)
#mean_lubrication200= weibullDistributionParams(lubricationList200)
print('200 numbers')
print('Estimation:')
#print(f"Mean:  {mean_lubrication200}")
#500
lubricationList500 = weibullDistribution(random500, 1.3, 66000, 0)
#mean_lubrication500= weibullDistributionParams(lubricationList500)
print('500 numbers')
print('Estimation:')
#print(f"Mean:  {mean_lubrication500}")

##############Electrical system - Weibull######################
print()
print('Electrical system - Weibull')
print('Scale: 35,000, Shape: 1.5')
print()
#50
electricalList50 = weibullDistribution(random50, 1.5, 35000, 0)
#mean_electrical50= weibullDistributionParams(electricalList50)
print('50 numbers')
print('Estimation:')
#print(f"Mean:  {mean_electrical50}")
#200
electricalList200 = weibullDistribution(random200, 1.5, 35000, 0)
#mean_electrical200= weibullDistributionParams(electricalList200)
print('200 numbers')
print('Estimation:')
#print(f"Mean:  {mean_electrical200}")
#500
electricalList500 = weibullDistribution(random500, 1.5, 35000, 0)
#mean_electrical500= weibullDistributionParams(electricalList500)
print('500 numbers')
print('Estimation:')
#print(f"Mean:  {mean_electrical500}")

##############Yaw system - Extreme maximum value######################
print()
print('Yaw system - Extreme maximum value')
print('Location: 65,000, Scale: 370')
print()
#50
yawList50 = extremeDistribution(random50, 65000, 370)
#mean_yaw50= extremeDistributionParams(yawList50)
print('50 numbers')
print('Estimation:')
#print(f"Mean:  {mean_yaw50}")
#200
yawList200 = extremeDistribution(random200, 65000, 370)
#mean_yaw200= extremeDistributionParams(yawList200)
print('200 numbers')
print('Estimation:')
#print(f"Mean:  {mean_yaw200}")
#500
yawList500 = extremeDistribution(random500, 65000, 370)
#mean_yaw500= extremeDistributionParams(yawList500)
print('500 numbers')
print('Estimation:')
#print(f"Mean:  {mean_yaw500}")


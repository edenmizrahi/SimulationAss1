import scipy as scipy
from scipy.stats import t


from RandomNumbers import *

def rand_100_for_each_destribution():
    normalList=list()
    #normal
    mean_normal_blade=42000
    sd_normal_blade=663
    bladeList_mean=list()
    bladeList_sd = list()

    mean_normal_PCS=84534
    sd_normal_PCS=506
    PCSList_mean = list()
    PCSList_sd = list()

    mean_logar_gearbox = 11
    sd_logar_gearbox = 1.2
    gearboxList_mean = list()
    gearboxList_sd = list()

    mean_exponential_brake=120000
    brakeList = list()
    brakeList_mean = list()

    mean_exponential_frequency=45000
    frequencyList = list()
    frequencyList_mean = list()

    for i in range(0,100):
        rn=randomNumbers(i,500)
        #blade
        blade_randoms = normalDistribution(rn,mean_normal_blade,sd_normal_blade)
        mean_normal_blade,sd_normal_blade= normalDistributionParams(blade_randoms)
        bladeList_mean.append(mean_normal_blade)
        bladeList_sd.append(sd_normal_blade)

        # Pitch control system
        pitch_control_system_randoms =(normalDistribution(rn,mean_normal_PCS,sd_normal_PCS))
        mean_normal_PCS,sd_normal_PCS=normalDistributionParams(pitch_control_system_randoms)
        PCSList_mean.append(mean_normal_PCS)
        PCSList_sd.append(sd_normal_PCS)

        # gearbox
        gearbox_randoms =logarithmicNormalDistribution(rn,mean_logar_gearbox,sd_logar_gearbox)
        mean_logar_gearbox,sd_logar_gearbox=logarithmicNormalDistributionParams(gearbox_randoms)
        gearboxList_mean.append(mean_logar_gearbox)
        gearboxList_sd.append(sd_logar_gearbox)

        #brake system:
        brake_randoms=exponentialDistribution(rn,mean_exponential_brake,0)
        mean_exponential_brake=exponentialDistributionParam(brake_randoms)
        brakeList_mean.append(mean_exponential_brake)

        #frequency converter
        frequency_randoms = exponentialDistribution(rn, mean_exponential_frequency,0)
        mean_exponential_frequency = exponentialDistributionParam(frequency_randoms)
        frequencyList_mean.append(mean_exponential_frequency)

        #generator
        #lubrication
        #electrical system
        #Yaw system
    return bladeList_mean,bladeList_sd, PCSList_mean,PCSList_sd,gearboxList_mean,gearboxList_sd,brakeList_mean,frequencyList_mean


def confidence_interval (sample):
    confidence_level = 0.90
    degrees_freedom = len(sample) - 1
    sample_mean = np.mean(sample)
    sample_standard_error = scipy.stats.sem(sample)
    confidence_interval = scipy.stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

    return confidence_interval


blade_mean,blade_sd,pitch_mean,pitch_sd,gearbox_mean,gearbox_sd, brake_mean, frequency_mean = rand_100_for_each_destribution()
print ("*****Confidence Interval*****")
print(f"Blade mean interval: {confidence_interval(blade_mean)}")
print(f"Blade sd interval: {confidence_interval(blade_sd)}")
print(f"Pitch mean interval: {confidence_interval(pitch_mean)}")
print(f"Pitch sd interval: {confidence_interval(pitch_sd)}")
print(f"Gearbox mean interval: {confidence_interval(gearbox_mean)}")
print(f"Gearbox sd interval: {confidence_interval(gearbox_sd)}")
print(f"Brake mean interval: {confidence_interval(brake_mean)}")
print(f"Frequency mean interval: {confidence_interval(frequency_mean)}")

print()
print ("*****Confidence Interval Top decile Bottom decile*****")
blade_mean.sort()
blade_mean_decile=list()
blade_sd_decile=list()

pitch_mean_decile=list()
pitch_sd_decile=list()

gearbox_mean_decile=list()
gearbox_sd_decile=list()

brake_mean_decile=list()

frequency_mean_decile=list()


for i in range(0,10):
    blade_mean_decile.append(blade_mean[i])
    blade_sd_decile.append(blade_sd[i])
    pitch_mean_decile.append(pitch_mean[i])
    pitch_sd_decile.append(pitch_sd[i])
    gearbox_mean_decile.append(gearbox_mean[i])
    gearbox_sd_decile.append(gearbox_sd[i])
    brake_mean_decile.append(brake_mean[i])
    frequency_mean_decile.append(frequency_mean[i])

for i in range(90,100):
    blade_mean_decile.append(blade_mean[i])
    blade_sd_decile.append(blade_sd[i])
    pitch_mean_decile.append(pitch_mean[i])
    pitch_sd_decile.append(pitch_sd[i])
    gearbox_mean_decile.append(gearbox_mean[i])
    gearbox_sd_decile.append(gearbox_sd[i])
    brake_mean_decile.append(brake_mean[i])
    frequency_mean_decile.append(frequency_mean[i])

print(f"Blade mean interval: {confidence_interval(blade_mean_decile)}")
print(f"Blade sd interval: {confidence_interval(blade_sd_decile)}")
print(f"Pitch sd interval: {confidence_interval(pitch_sd_decile)}")
print(f"Pitch mean interval: {confidence_interval(pitch_mean_decile)}")
print(f"Gearbox sd interval: {confidence_interval(gearbox_sd_decile)}")
print(f"Gearbox mean interval: {confidence_interval(gearbox_mean_decile)}")
print(f"Brake sd interval: {confidence_interval(brake_mean_decile)}")
print(f"Frequency sd interval: {confidence_interval(frequency_mean_decile)}")




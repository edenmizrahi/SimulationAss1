import scipy as scipy

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
    confidence_level = 0.95
    degrees_freedom = len(sample) - 1
    sample_mean = np.mean(sample)
    sample_standard_error = scipy.stats.sem(sample)
    confidence_interval = scipy.stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

    return confidence_interval


blade_mean,blade_sd,pitch_mean,pitch_sd,gearbox_mean,gearbox_sd, brake_mean, frequency_mean = rand_100_for_each_destribution()

print(confidence_interval(blade_mean))
x=0;



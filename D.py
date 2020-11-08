import scipy as scipy
from scipy.stats import norm
from RandomNumbers import *

mean_normal_blade_ = 42000
sd_normal_blade_ = 663
bladeList_mean = list()
bladeList_sd = list()

mean_normal_PCS_ = 84534
sd_normal_PCS_ = 506
PCSList_mean = list()
PCSList_sd = list()

mean_logar_gearbox_ = 11
sd_logar_gearbox_ = 1.2
gearboxList_mean = list()
gearboxList_sd = list()

mean_exponential_brake_ = 120000
brakeList = list()
brakeList_mean = list()

mean_exponential_frequency_ = 45000
frequencyList = list()
frequencyList_mean = list()

n_weibull_generator_ = 76000
m_weibull_generator_ = 1.2
generatorList = list()
generatorList_m = list()
generatorList_n = list()

n_weibull_lubrication_ = 66000
m_weibull_lubrication_ = 1.3
lubricationList = list()
lubricationList_m = list()
lubricationList_n = list()

n_weibull_electrical_ = 35000
m_weibull_electrical_ = 1.5
electricalList = list()
electricalList_m = list()
electricalList_n = list()

mean_extreme_yaw_ = 65000
sd_extreme_yaw_ = 370
yawListList_mean = list()
yawListList_sd = list()
def rand_100_for_each_destribution():
    normalList=list()
    #normal
    mean_normal_blade_=42000
    sd_normal_blade_=663
    bladeList_mean=list()
    bladeList_sd = list()

    mean_normal_PCS_=84534
    sd_normal_PCS_=506
    PCSList_mean = list()
    PCSList_sd = list()

    mean_logar_gearbox_ = 11
    sd_logar_gearbox_ = 1.2
    gearboxList_mean = list()
    gearboxList_sd = list()

    mean_exponential_brake_=120000
    brakeList = list()
    brakeList_mean = list()

    mean_exponential_frequency_=45000
    frequencyList = list()
    frequencyList_mean = list()

    n_weibull_generator_ = 76000
    m_weibull_generator_ = 1.2
    generatorList = list()
    generatorList_m = list()
    generatorList_n = list()

    n_weibull_lubrication_ = 66000
    m_weibull_lubrication_ = 1.3
    lubricationList = list()
    lubricationList_m = list()
    lubricationList_n = list()

    n_weibull_electrical_ = 35000
    m_weibull_electrical_ = 1.5
    electricalList = list()
    electricalList_m = list()
    electricalList_n = list()

    mean_extreme_yaw_ = 65000
    sd_extreme_yaw_ = 370
    yawList_mean = list()
    yawList_sd = list()


    for i in range(0,100):
        #rn=randomNumbers(i,500)
        np.random.seed(i)
        rn = np.random.uniform(0, 1, 500)
        #blade
        blade_randoms = normalDistribution(rn,mean_normal_blade_,sd_normal_blade_)
        mean_normal_blade,sd_normal_blade= normalDistributionParams(blade_randoms)
        bladeList_mean.append(mean_normal_blade)
        bladeList_sd.append(sd_normal_blade)

        # Pitch control system
        pitch_control_system_randoms =(normalDistribution(rn,mean_normal_PCS_,sd_normal_PCS_))
        mean_normal_PCS,sd_normal_PCS=normalDistributionParams(pitch_control_system_randoms)
        PCSList_mean.append(mean_normal_PCS)
        PCSList_sd.append(sd_normal_PCS)

        # gearbox
        gearbox_randoms =logarithmicNormalDistribution(rn,mean_logar_gearbox_,sd_logar_gearbox_)
        mean_logar_gearbox,sd_logar_gearbox=logarithmicNormalDistributionParams(gearbox_randoms)
        gearboxList_mean.append(mean_logar_gearbox)
        gearboxList_sd.append(sd_logar_gearbox)

        #brake system:
        brake_randoms=exponentialDistribution(rn,mean_exponential_brake_,0)
        mean_exponential_brake=exponentialDistributionParam(brake_randoms)
        brakeList_mean.append(mean_exponential_brake)

        #frequency converter
        frequency_randoms = exponentialDistribution(rn, mean_exponential_frequency_,0)
        mean_exponential_frequency = exponentialDistributionParam(frequency_randoms)
        frequencyList_mean.append(mean_exponential_frequency)

        #generator:
        generator_randoms = weibullDistribution(rn, m_weibull_generator_,n_weibull_generator_,0)
        n_weibull_generator,m_weibull_generator = weibullDistributionParams(generator_randoms,m_weibull_generator_)
        generatorList_m.append(m_weibull_generator)
        generatorList_n.append(n_weibull_generator)

        #lubrication
        lubrication_randoms = weibullDistribution(rn, m_weibull_lubrication_,n_weibull_lubrication_,0)
        n_weibull_lubrication,m_weibull_lubrication = weibullDistributionParams(lubrication_randoms,m_weibull_lubrication_)
        lubricationList_m.append(m_weibull_lubrication)
        lubricationList_n.append(n_weibull_lubrication)

        #electrical system
        electrical_randoms = weibullDistribution(rn, m_weibull_electrical_,n_weibull_electrical_,0)
        n_weibull_electrical,m_weibull_electrical = weibullDistributionParams(electrical_randoms,m_weibull_electrical_)
        electricalList_m.append(m_weibull_electrical)
        electricalList_n.append(n_weibull_electrical)

        #Yaw system
        yaw_randoms = extremeDistribution(rn,mean_extreme_yaw_,sd_extreme_yaw_)
        mean_extreme_yaw, sd_extreme_yaw= extremeDistributionParams(yaw_randoms)
        yawList_mean.append(mean_extreme_yaw)
        yawList_sd.append(sd_extreme_yaw)


    return generatorList_m,generatorList_n,lubricationList_m,lubricationList_n,electricalList_m,electricalList_n,yawList_mean,yawList_sd,bladeList_mean,bladeList_sd, PCSList_mean,PCSList_sd,gearboxList_mean,gearboxList_sd,brakeList_mean,frequencyList_mean


def confidence_interval (sample):
    confidence_level = 0.90
    degrees_freedom = len(sample) - 1
    sample_mean = np.mean(sample)
    sample_standard_error = scipy.stats.sem(sample)
    confidence_interval = scipy.stats.norm.interval(confidence_level, sample_mean, sample_standard_error)

    return confidence_interval

generator_m,generator_n,lubrication_m,lubrication_n,electrical_m,electrical_n,yaw_location,yaw_scale,blade_mean,blade_sd,pitch_mean,pitch_sd,gearbox_mean,gearbox_sd, brake_mean, frequency_mean = rand_100_for_each_destribution()
print ("*****Confidence Interval*****")
print(f"Blade mean interval: {confidence_interval(blade_mean)}  original Value :{mean_normal_blade_} mean value : {np.mean(blade_mean)}")
print(f"Blade sd interval: {confidence_interval(blade_sd)} original Value :{sd_normal_blade_} sd value : {np.mean(blade_sd)} ")
print(f"Pitch mean interval: {confidence_interval(pitch_mean)} original Value :{mean_normal_PCS_} mean value : {np.mean(pitch_mean)}")
print(f"Pitch sd interval: {confidence_interval(pitch_sd)} original Value :{sd_normal_PCS_} sd value : {np.mean(pitch_sd)}" )
print(f"Gearbox mean interval: {confidence_interval(gearbox_mean)} original Value :{mean_logar_gearbox_} mean value : {np.mean(gearbox_mean)}")
print(f"Gearbox sd interval: {confidence_interval(gearbox_sd)} original Value :{sd_logar_gearbox_} sd value : {np.mean(gearbox_sd)}")
print(f"Brake mean interval: {confidence_interval(brake_mean)} original Value :{mean_exponential_brake_} mean value : {np.mean(brake_mean)}")
print(f"Frequency mean interval: {confidence_interval(frequency_mean)} original Value :{mean_exponential_frequency_ }mean value : {np.mean(frequency_mean)}")
print(f"Generator m interval: {confidence_interval(generator_m)} original Value :{m_weibull_generator_ }")
print(f"Generator n interval: {confidence_interval(generator_n)} original Value :{n_weibull_generator_ }")
print(f"lubrication m interval: {confidence_interval(lubrication_m)} original Value :{m_weibull_lubrication_ }")
print(f"lubrication n interval: {confidence_interval(lubrication_n)} original Value :{n_weibull_lubrication_ }")
print(f"electrical m interval: {confidence_interval(electrical_m)} original Value :{m_weibull_electrical_ }")
print(f"electrical n interval: {confidence_interval(electrical_n)} original Value :{n_weibull_electrical_ }")
print(f"yaw location interval: {confidence_interval(yaw_location)} original Value :{mean_extreme_yaw_ }")
print(f"yaw scale interval: {confidence_interval(yaw_scale)} original Value :{sd_extreme_yaw_ }")


generator_m.sort()
generator_n.sort()
lubrication_m.sort()
lubrication_n.sort()
electrical_m.sort()
electrical_n.sort()
yaw_location.sort()
yaw_scale.sort()
blade_mean.sort()
blade_sd.sort()
pitch_mean.sort()
pitch_sd.sort()
gearbox_mean.sort()
gearbox_sd.sort()
brake_mean.sort()
frequency_mean.sort()

print ("*****Confidence Interval 10% *****")
print(f"Blade mean interval: {blade_mean[9]} ,{blade_mean[90]}  original Value :{mean_normal_blade_} mean value : {np.mean(blade_mean)}")
print(f"Blade sd interval: {blade_sd[9]} ,{blade_sd[90]} original Value :{sd_normal_blade_} sd value : {np.mean(blade_sd)} ")
print(f"Pitch mean interval: {pitch_mean[9]} ,{pitch_mean[90]} original Value :{mean_normal_PCS_} mean value : {np.mean(pitch_mean)}")
print(f"Pitch sd interval: {pitch_sd[9]} ,{pitch_sd[90]} original Value :{sd_normal_PCS_} sd value : {np.mean(pitch_sd)}" )
print(f"Gearbox mean interval: {gearbox_mean[9]} ,{gearbox_mean[90]} original Value :{mean_logar_gearbox_} mean value : {np.mean(gearbox_mean)}")
print(f"Gearbox sd interval: {gearbox_sd[9]},{gearbox_sd[90]}  original Value :{sd_logar_gearbox_} sd value : {np.mean(gearbox_sd)}")
print(f"Brake mean interval: {brake_mean[9]} ,{brake_mean[90]} original Value :{mean_exponential_brake_} mean value : {np.mean(brake_mean)}")
print(f"Frequency mean interval: {frequency_mean[9]} ,{frequency_mean[90]} original Value :{mean_exponential_frequency_ }mean value : {np.mean(frequency_mean)}")
print(f"Generator m interval: {generator_m[9]} ,{generator_m[90]} original Value :{m_weibull_generator_ }")
print(f"Generator n interval: {generator_n[9]} ,{generator_n[90]} original Value :{n_weibull_generator_ }")
print(f"lubrication m interval: {lubrication_m[9]} ,{lubrication_m[90]} original Value :{m_weibull_lubrication_ }")
print(f"lubrication n interval: {lubrication_n[9]} ,{lubrication_n[90]} original Value :{n_weibull_lubrication_ }")
print(f"electrical m interval: {electrical_m[9]} ,{electrical_m[90]} original Value :{m_weibull_electrical_ }")
print(f"electrical n interval: {electrical_n[9]} ,{electrical_n[90]} original Value :{n_weibull_electrical_ }")
print(f"yaw location interval: {yaw_location[9]} ,{yaw_location[90]} original Value :{mean_extreme_yaw_ }")
print(f"yaw scale interval: {yaw_scale[9]} ,{yaw_scale[90]} original Value :{sd_extreme_yaw_ }")

# print()
# print ("*****Confidence Interval Top decile Bottom decile*****")
# blade_mean.sort()
# blade_mean_decile=list()
# blade_sd_decile=list()
#
# pitch_mean_decile=list()
# pitch_sd_decile=list()
#
# gearbox_mean_decile=list()
# gearbox_sd_decile=list()
#
# brake_mean_decile=list()
#
# frequency_mean_decile=list()
#
#
# for i in range(0,10):
#     blade_mean_decile.append(blade_mean[i])
#     blade_sd_decile.append(blade_sd[i])
#     pitch_mean_decile.append(pitch_mean[i])
#     pitch_sd_decile.append(pitch_sd[i])
#     gearbox_mean_decile.append(gearbox_mean[i])
#     gearbox_sd_decile.append(gearbox_sd[i])
#     brake_mean_decile.append(brake_mean[i])
#     frequency_mean_decile.append(frequency_mean[i])
#
# for i in range(90,100):
#     blade_mean_decile.append(blade_mean[i])
#     blade_sd_decile.append(blade_sd[i])
#     pitch_mean_decile.append(pitch_mean[i])
#     pitch_sd_decile.append(pitch_sd[i])
#     gearbox_mean_decile.append(gearbox_mean[i])
#     gearbox_sd_decile.append(gearbox_sd[i])
#     brake_mean_decile.append(brake_mean[i])
#     frequency_mean_decile.append(frequency_mean[i])
#
# print(f"Blade mean interval: {confidence_interval(blade_mean_decile)}")
# print(f"Blade sd interval: {confidence_interval(blade_sd_decile)}")
# print(f"Pitch sd interval: {confidence_interval(pitch_sd_decile)}")
# print(f"Pitch mean interval: {confidence_interval(pitch_mean_decile)}")
# print(f"Gearbox sd interval: {confidence_interval(gearbox_sd_decile)}")
# print(f"Gearbox mean interval: {confidence_interval(gearbox_mean_decile)}")
# print(f"Brake sd interval: {confidence_interval(brake_mean_decile)}")
# print(f"Frequency sd interval: {confidence_interval(frequency_mean_decile)}")




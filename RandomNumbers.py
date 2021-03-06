
# Xj= (aXj-1 +b)mod m
import numpy as np
import math as math
import statistics

def randomNumbers (seed ,num):
    x0=seed
    a=5
    b=3
    m=10000
    randoNums= list()
    for i in range(0,num):
        xj=(a*x0+b)%m
        randoNums.append(xj/m)
        x0=xj
    return randoNums

def extremeDistribution(randomNumber:list() , u , b):
    extremeList= list()
    for i in randomNumber:
        extremeList.append(u - b * np.log(-np.log(i)))
    return extremeList

def extremeDistributionParams(distributionList):
    mean = sum(distributionList)/len(distributionList)

    newExtremeList = list()
    for i in distributionList:
        newExtremeList.append(pow(i-mean,2))
    std = math.sqrt((1/len(distributionList)) * sum(newExtremeList))

    loc = mean - (0.45006*std)
    scale = (std*np.sqrt(6))/np.pi

    return loc, scale


def extremeMinDistributionParams(distributionList):
    mean = sum(distributionList)/len(distributionList)

    newExtremeList = list()
    for i in distributionList:
        newExtremeList.append(pow(i-mean,2))
    std = math.sqrt((1/len(distributionList)) * sum(newExtremeList))

    loc = mean + (0.45006*std)
    scale = (std*np.sqrt(6))/np.pi

    return loc, scale
#logarithmic :
def logarithmicNormalDistribution(randomNumbers: list(), u, sd):
    distributionList = list()
    for i in range(len(randomNumbers)):
        if i%2==0:
            n1=randomNumbers[i]
            n2=randomNumbers[i+1]
            t1=((-2*math.log(n1,math.e))**0.5)*math.cos(2*math.pi*n2)
            t1=(math.e)**(u+sd*t1)
            t2 = ((-2 * math.log(n1, math.e)) ** 0.5) * math.sin(2 * math.pi * n2)
            t2 = (math.e) ** (u + sd * t2)
            # a =math.sqrt(-2*np.log(n1))
            # t1=math.exp(a*math.sin(2*math.pi*n2))
            # t1_=math.exp(u+sd*t1)
            # t2=math.exp(a*math.cos(2*math.pi*n2))
            # t2_=math.exp(u+sd*t2)
            distributionList.append(t1)
            distributionList.append(t2)
    return distributionList

def logarithmicNormalDistributionParams(distributionList):
    distributionListAfterLn=list()
    for i in distributionList:
        distributionListAfterLn.append(np.log(i))
    mean_=sum(distributionListAfterLn)/len(distributionListAfterLn)

    listForSD=list()
    for i in distributionListAfterLn:
        listForSD.append(math.pow(i-mean_,2))

    sd_= math.sqrt(sum(listForSD)/len(distributionListAfterLn))
    return mean_,sd_

#normal:
def normalDistribution(randomNumbers: list(), u, sd):
    distributionList = list()
    for i in range(len(randomNumbers)):
        if i%2==0:
            n1=randomNumbers[i]
            n2=randomNumbers[i+1]
            t1 = ((-2 * math.log(n1, math.e)) ** 0.5) * math.cos(2 * math.pi * n2)
            t1 =(u + sd * t1)
            t2 = ((-2 * math.log(n1, math.e)) ** 0.5) * math.sin(2 * math.pi * n2)
            t2 =(u + sd * t2)
            distributionList.append(t1)
            distributionList.append(t2)
    return distributionList

def normalDistributionParams(distributionList):
    mean_ = sum(distributionList) / len(distributionList)

    listForSD = list()
    for i in distributionList:
        listForSD.append(math.pow(i - mean_, 2))

    sd_ = math.sqrt(sum(listForSD) / len(distributionList))
    return mean_, sd_

#exponrntial :
def exponentialDistribution(randomNumbers: list(), u, t0):
    distributionList = list()
    for i in randomNumbers:
        t= t0+(-np.log(i)/(1/u))
        distributionList.append(t)
    return distributionList

def exponentialDistributionParam(distributionList):
    return 1/(len(distributionList)/sum(distributionList))

#weibull
def weibullDistribution(randomNumbers: list(),m,n,t0):
    distributionList = list()
    for i in randomNumbers:
        t = n*math.pow((-np.log(i)),1/m)+t0
        distributionList.append(t)
    return distributionList
    # m_=
    # n_=
    # return m_,n_

def weibullDistributionParams(distributionList, m):
    #print(distributionList)
    weibullList = list()
    for i in distributionList:
        weibullList.append(pow(i,m))
    #print(weibullList)
    n_pow_m = (1/len(weibullList)) * sum(weibullList)
    n_new = math.pow(n_pow_m, 1/m)

    weibullList2 = list()
    for i in distributionList:
        weibullList2.append(pow(i,m) * np.log(i))

    weibullList3 = list()
    for i in distributionList:
        weibullList3.append(np.log(i))


    m_temp = (sum(weibullList2)/sum(weibullList)) - (1/len(weibullList)*sum(weibullList3))
    m_new = 1/m_temp

    return n_new, m_new


#print(randomNumbers(0.55,10000))
# print(exponentialDistributionParam(exponentialDistribution(randomNumbers(0.55,500),120000,0)))
np.random.seed(1)
rn = np.random.uniform(0, 1, 500)
# print(logarithmicNormalDistributionParams(logarithmicNormalDistribution(rn,11,1.2)))

# print(normalDistributionParams(normalDistribution(rn, 84534, 506)))

#print(normalDistributionParams(normalDistribution(rn, 84534, 506)))

print(extremeDistributionParams(extremeDistribution(rn, 65000, 370)))

# print(exponentialDistributionParam(exponentialDistribution(rn,45000,0)))


# print(weibullDistributionParams(weibullDistribution(rn, 1.2, 76000, 0), 1.2))
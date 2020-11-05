
from RandomNumbers import *

def ExponentialComparison(u):
    # Random 500 values for each distribution with seed=0.5
    exponentialList1 = exponentialDistribution(randomNumbers(0.5,500),u,0)
    exponentialParam1 = exponentialDistributionParam(exponentialList1)
    print(exponentialParam1)

    #Random 500 more values for each distribution with seed=0.5
    exponentialList2 = exponentialDistribution(randomNumbers(0.5,500),u,0)
    #print(exponentialBrakeList2)
    exponentialParam2 = exponentialDistributionParam(exponentialList2)
    print(exponentialParam2)

    #Random 500 more values for each distribution with other seed=0.8
    exponentialList3 = exponentialDistribution(randomNumbers(0.8,500),u,0)
        #print(exponentialBrakeList3)
    exponentialParam3 = exponentialDistributionParam(exponentialList3)
    print(exponentialParam3)

    #Random 10000 more values for each distribution with seed=1
    exponentialList4 = exponentialDistribution(randomNumbers(1,10000), u, 0)
        # print(exponentialBrakeList3)
    exponentialParam4 = exponentialDistributionParam(exponentialList4)
    print(exponentialParam4)

def NormalComparison(u,sd):

    # Random 500 values for each distribution with seed=0.5
    NormalList1 = normalDistribution(randomNumbers(0.5,500), u, sd)
    NormalParams1 = normalDistributionParams(NormalList1)
    print(NormalParams1)

    #Random 500 more values for each distribution with seed=0.5
    NormalList2 = normalDistribution(randomNumbers(0.5, 500), u, sd)
    NormalParams2 = normalDistributionParams(NormalList2)
    print(NormalParams2)

    #Random 500 more values for each distribution with other seed=0.8
    NormalList3 = normalDistribution(randomNumbers(0.8, 500), u, sd)
    NormalParams3 = normalDistributionParams(NormalList3)
    print(NormalParams3)

    #Random 10000 more values for each distribution with seed=1
    NormalList4 = normalDistribution(randomNumbers(1, 10000), u, sd)
    NormalParams4 = normalDistributionParams(NormalList4)
    print(NormalParams4)

def LogarithmicNormalComparison(u,sd):

    # Random 500 values for each distribution with seed=0.5
    NormalList1 = logarithmicNormalDistribution(randomNumbers(0.5,500), u, sd)
    NormalParams1 = logarithmicNormalDistributionParams(NormalList1)
    print(NormalParams1)

    #Random 500 more values for each distribution with seed=0.5
    NormalList2 = logarithmicNormalDistribution(randomNumbers(0.5, 500), u, sd)
    NormalParams2 = logarithmicNormalDistributionParams(NormalList2)
    print(NormalParams2)

    #Random 500 more values for each distribution with other seed=0.8
    NormalList3 = logarithmicNormalDistribution(randomNumbers(0.8, 500), u, sd)
    NormalParams3 = logarithmicNormalDistributionParams(NormalList3)
    print(NormalParams3)

    #Random 10000 more values for each distribution with seed=1
    NormalList4 = logarithmicNormalDistribution(randomNumbers(1, 10000), u, sd)
    NormalParams4 = logarithmicNormalDistributionParams(NormalList4)
    print(NormalParams4)

#ExponentialComparison(120000)
#ExponentialComparison(45000)
#NormalComparison(42000,663)
#NormalComparison(84534,506)
#LogarithmicNormalComparison(11,1.2)

#ExtremeComparison(65000,370)
#WeibullComparison(66000,1.3)
#WeibullComparison(35000,1.5)
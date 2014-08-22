from numpy import *

Features = [3,#lengthOfURL values 0,1,2
            3,#NumOfNumber values 0,1,2
            3,#NumOf/ values 0,1,2
            2 #lengthOfDomain values 0,1,2
        ]

NumOfFeatures = len(Features)
#print NumOfFeatures

#initial sumOfFeaturs = [[1,1,1],
#                        [1,1,1],
#                        [1,1,1],
#                        [1,1]]
#
#Laplace Smooth: x belog to {1,2,...,L} then p(x=i|y=k) = (sum(x=i,y=k) + 1) / sum{y=k} + L
#
def trainer(trainMatrix, ClassVect):
    m = len(ClassVect) #num of training sample 
    goods = sum(ClassVect) #num of good url sample
    bads = (m-sum(ClassVect)) #num of bad url sample
    pGood = goods /float(m)
    #pBad =  bads /float(m)
    L = 1.0
    for i in range(NumOfFeatures):
        L = L * Features[i]
    goodNum = []; badNum = []; 
    goodDenom = L; badDenom = L
    #init the sumOfFeatures
    for i in range(NumOfFeatures):
        tmpNumList = []
        tmpDenomList = []
        for j in range(Features[i]):
            tmpNumList.append(1.0)
            #tmpDenomList.append(Features[i])
        goodNum.append(tmpNumList)
        badNum.append(tmpNumList)
        #goodDenom.append(tmpDenomList)
        #badDenom.append(tmpDenomList)
        #init end
    
    print goodNum
    print badNum
    for i in range(m): #the ith sample
        if ClassVect[i] == 1 :
            goodDenom += 1
            for j in range(NumOfFeatures): #the jth feature
                value = trainMatrix[i,j]
                goodNum[j][value] += 1
        if ClassVect[i] == 0 :
            badDenom += 1
            for j in range(NumOfFeatures): #the jth feature
                value = trainMatrix[i,j]
                badNum[j][value] += 1
    
    pGoodVect = []
    pBadVect = []
    for i in range(NumOfFeatures):
        pGoodVect.append(log( array(goodNum[i]) / goodDenom ))
        pBadVect.append(log( array(badNum[i]) / badDenom ) )
    return pGoodVect, pBadVect, pGood

    #print goodNum
    #print badNum
    #print goodDenom
    #print badDenom 

    #use laplace smooth and the initial denom is 2
        #for i in range(m):
        #if ClassVect[i] == 0 :
        
def URLclassify(vector, pGoodVect, pBadVect, pGood):
    p1 = 0.0
    p0 = 0.0
    for i in range(NumOfFeatures): #ith feature
        v = vector[i]
        p1 += pGoodVect[i][v] + log(pGood)
        p0 += pBadVect[i][v] + log(1.0-pGood)

    if p1>p0:
        return 1
    else :
        return 0


a = mat([[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,2,2,1],
         [2,1,1,1]     
        ]) 
b= [1,1,1,1,0]
p1,p0,p = trainer(a,b)
print p1
print p0
print p
#print p1[1][0]

vec = [1,2,2,1]
print URLclassify(vec,p1,p0,p)

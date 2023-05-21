import numpy as np
from scipy.stats import triang, pareto, lognorm


def ALECalc(a, b, c, point1, point2, data, mu, sigma, xm, alpha,
          num, point3, point4, point5):

    # (1) calculate probabilities
    # creating the triangular distribution
    distrib1 = triang(c=(c-a)/(b-a), loc=a, scale=b-a)

    # calculating the probability that AV is no greater than point1
    prob1 = distrib1.cdf(point1)

    # calculating the probability that AV is greater than point2
    prob2 = 1 - distrib1.cdf(point2)

    # calculating mean and median of AV
    MEAN_t = distrib1.mean()
    MEDIAN_t = distrib1.median()

    # (2) calculate mean and variance of data
    # converting data to numpy array
    data = np.array(data)

    # calculating mean and variance of data
    MEAN_d = np.mean(data)
    VARIANCE_d = np.var(data)

    # (3) Monte Carlo simulation
    # creating log-normal and Pareto distributions
    distribA1 = lognorm(s=sigma, scale=np.exp(mu))
    distribB1 = pareto(b=alpha, loc=xm)

    # sample from distributions and calculate total impact
    sampleA1distrib = distribA1.rvs(num)
    sampleB1distrib = distribB1.rvs(num)
    total_impact = sampleA1distrib + sampleB1distrib

    # calculating probability that total impact is greater than point3
    prob3 = np.sum(total_impact > point3) / num

    # calculating probability that total impact is between point4 and point5
    prob4 = np.sum((total_impact >= point4) & (total_impact <= point5)) / num

    # (4) calculate ALE
    # calculating SLE using median of triangular distribution as AV and probability
    SLE = MEDIAN_t * prob3

    # calculating ARO using the mean
    ARO = MEAN_d

    # calculating ALE
    ALE = ARO * SLE

    return (prob1, prob2, MEAN_t, MEDIAN_t, MEAN_d, VARIANCE_d, prob3, prob4, ALE)


# input data
a, b, c, point1, point2, mu, sigma, xm, alpha, num, point3, point4, point5 = 10000, 35000, 18000, 12000, 25000, 0, 3, 1, 4, 500000, 30, 50, 100
data = [11, 15, 9, 5, 3, 14, 16, 15, 12, 10, 11, 4, 7, 12, 6]

results = ALECalc(a, b, c, point1, point2, data, mu, sigma, xm, alpha,
                num, point3, point4, point5)

print(results)

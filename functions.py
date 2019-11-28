import math

def normpdf(x, mean, sd):
    '''Return the value of the normal distribution with the specified mean and standard deviation (sd) at position x.'''
    
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    '''Return chance of death.'''
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd))/2
        start += step            
    return integral 
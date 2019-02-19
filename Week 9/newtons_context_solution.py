def f(c, max_voltage):
    y = round(c*exp(0.05*c)*1000 - max_voltage,5)
    return(y)
    
def fdash(c):
    d = round((50*c + 1000)*exp(0.05*c),5)
    return(d)
    
def onestep(x, max_voltage):
    newguess = round(x - f(x, max_voltage)/fdash(x),5)
    return(newguess)
    
def newtons(x, n, p, max_voltage):
    currentStep = 1
    stop = 0
    while stop==0 and currentStep <= n:
        previous = x
        x = onestep(x, max_voltage)
        if 100*abs(previous - x)/previous < p:
            stop = 1
        currentStep = currentStep + 1
    return(x)
    
def will_it_rupture(current, max_voltage):
    guess = newtons(1, 15, 1, max_voltage)
    if guess<=current:
        return(0, guess)
    else:
        return(1, guess)

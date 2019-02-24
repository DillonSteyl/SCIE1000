def calculate_age(carbon):
    halflives = log(carbon/100)/log(0.5)
    years = halflives*5730
    return(years)

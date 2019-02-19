from pylab import *

def convert_to_hours(minutes):
    converted_minutes = minutes%60
    converted_hours = floor(minutes/60)
    return(converted_hours, converted_minutes)

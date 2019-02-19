from pylab import *

P = 100
k = 0.1
n = 30
time = arange(0, n)

exponential = P*exp(k*time)
compounding = P*(1+k)**(time)

if round(compounding[n-1], 5) == round(exponential[n-1], 5):
    print("These two equations are interchangeable when k is constant.")
else:
    print("These two equations are not interchangeable.")

plot(time, exponential, label="Exponential")
plot(time, compounding, label="Compounding")

title("Exponential vs Compounding")
xlabel("Time")
ylabel("Amount")
legend()
show()

import numpy as np

x = np.array([5,15,25,35,45,55])
y = np.array([1,3,5,7,9,11])
m = len(y)
alpha = 0.001
n_iter = 3000

theta0 = 0
theta1 = 1

temp_theta0 = theta0
temp_theta1 = theta1

for i in range(n_iter):
    temp_theta0 = theta0 - alpha*(1/m)*np.sum(theta0+x*theta1-y)
    temp_theta1 = theta1 - alpha*(1/m)*np.sum((theta0+x*theta1-y)*x)
    theta0 = temp_theta0
    theta1 = temp_theta1

print((np.sum(theta0+theta1*x-y)**2)/(2*m))
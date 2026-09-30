import matplotlib.pyplot as plt
from scipy import stats
x =[10,21,45,64,73 , 99]
y =[1, 9, 19, 18, 99, 64]
slope , intercept , r, p, std_err = stats.linregress(x, y)
def func(x):
    return slope * x + intercept
mymodel = list(map(func, x))
plt.scatter(x, y)
plt.plot(mymodel, x)
plt.show()

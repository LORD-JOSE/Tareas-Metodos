import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def poisson(s, lambda_val):
    return (np.exp(-lambda_val)*lambda_val**s/factorial(s))

lambda_val = 50/60 
s = np.arange(1, 10)

p_cond = poisson(s,lambda_val)/(1-np.exp(-lambda_val))
print(p_cond)


plt.bar(s, p_cond)
plt.xlabel('Numero de particulas')
plt.ylabel('Probabilidad de al menos una particula')
plt.title('Distribución de n dado que al menos una partícula ha sido detectada')
plt.show()

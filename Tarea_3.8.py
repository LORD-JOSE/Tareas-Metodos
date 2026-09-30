import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

#En primer lugar defino la distribucion de poisson. La ocupo porque estamos hablando de eventos en un cierto intervalo
def poisson(s, lambda_val):
    return (np.exp(-lambda_val)*lambda_val**s/factorial(s))

#Si bien el tenemos un 50 por minuto, aqui estamos hablando de segundos 
lambda_val = 50/60 
s = np.arange(1, 10)

#defino esta variable porque es la probabilidad de que el sensor se active.
p_cond = poisson(s,lambda_val)/(1-np.exp(-lambda_val))
print(p_cond)


plt.bar(s, p_cond)
plt.xlabel('Numero de particulas')
plt.ylabel('Probabilidad de al menos una particula')
plt.title('Distribución de n dado que al menos una partícula ha sido detectada')
plt.show()

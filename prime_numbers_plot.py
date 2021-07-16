from sympy import sieve
import matplotlib.pyplot as plt


n = [i for i in sieve.primerange(10000)]

ax = plt.subplot(111, projection='polar')
ax.plot(n, n, ',')

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
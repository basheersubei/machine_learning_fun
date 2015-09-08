import scipy, scipy.stats
import numpy as np
import pylab
import mpl_toolkits.mplot3d.axes3d as p3
n = 40

p_min = 0.1
p_max = 0.9
number_p = 10

p_range = scipy.linspace(p_min, p_max, number_p)
k_range = scipy.linspace(0, n, n + 1)

points = []
fig = pylab.figure()
ax = p3.Axes3D(fig)

k_result = []
p_result = []
pmf_result = []

for p in p_range:
    # for n in n_range:
    for k in k_range:
        pmf = scipy.stats.binom.pmf(k, n, p)
        k_result.append(k)
        p_result.append(p)
        pmf_result.append(pmf)
        print("k is %d and p is %f" % (k, p))


ax.scatter(k_result, p_result, pmf_result)
pylab.show()

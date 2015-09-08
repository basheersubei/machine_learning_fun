import scipy, scipy.stats
x = scipy.linspace(0,10,11)
pmf = scipy.stats.binom.pmf(x,10,0.1)
import pylab
pylab.plot(x,pmf)
pylab.show()

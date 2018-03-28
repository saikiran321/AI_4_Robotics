def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]




measurements=[5.,6.,7.,9.,10.,15]
motion=[1.,1.,2.,1.,5.,2]

measurement_sig=4.
motion_sig=2.0

mu=0.
sig=.1

for i in range(len(measurements)):
	[mu,sig]=update(measurements[i],measurement_sig,mu,sig)
	# print mu,sig
	[mu,sig]=predict(motion[i],motion_sig,mu,sig)
	
print [mu,sig]

============
Strauss Plot
============

**Sept 18 2016**, John Hoffman

Strauss plot implementation for python. It's a combination of a heatmap (for 
high density regions) and a scatter plot (for low density regions)

Example usage::

	#!/usr/bin/env python
	from strauss_plot import strauss_plot
	import numpy as np
	import matplotlib.pyplot as plt
	
	f, ax = plt.subplots()

	# generate 5000 points from a normal distribution
	x = np.random.normal(size=5000)
	y = np.random.normal(size=5000)

	# Add strauss plot
	strauss_plot(ax, x, y)

	# display the plot
	plt.show()



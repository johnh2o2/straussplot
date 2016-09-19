"""
strauss_plot.py

(c) 2016 John Hoffman
jah5@princeton.edu

Implements the "Strauss Plot", which is a combined heatmap/scatterplot
that allows for good visualization of data that is dense in certain
regions of phase space and sparse in others.

"""

import matplotlib.pyplot as plt
import numpy as np

def get_grid_and_scatter(x, y, threshold=1, nx=100, ny=100, boundaries=None, **kwargs):
	"""
	Arguments
	---------
	x             :  array-like, size N
	y             :  array-like, size N
	threshold     :  if data points
	""" 

	# grid
	counts = np.zeros((ny, nx))

	# set boundaries
	xmin, xmax, ymin, ymax = None, None, None, None
	if boundaries is None:
		xmin, xmax, ymin, ymax = min(x), max(x), min(y), max(y)
	else:
		xmin, xmax, ymin, ymax = boundaries

	# translate position to grid index
	get_inds = lambda X, Y : (int((X - xmin)/(xmax - xmin) * nx),int((Y - ymin)/(ymax - ymin) * ny))

	# compute number of data within each pixel
	for X, Y in zip(x,y):
		if np.isnan(X) or np.isnan(Y): continue
		ix, iy = get_inds(X,Y)
		if ix >= nx or iy >= ny: continue
		counts[iy][ix] += 1

	# array of data to be plotted as a scatterplot
	scatter_points = []

	# now move data from grid to scatter_points if too sparse
	for X, Y in zip(x,y):
		if np.isnan(X) or np.isnan(Y): continue
		ix, iy = get_inds(X,Y)
		if ix >= nx or iy >= ny: continue

		if counts[iy][ix] > threshold: continue
		
		scatter_points.append((X,Y))
		counts[iy][ix] -= 1

	dx = (xmax - xmin) / nx
	dy = (ymax - ymin) / ny
	xgrid, ygrid = np.meshgrid(np.linspace(xmin, xmax + dx, nx + 1), np.linspace(ymin, ymax + dy, ny + 1))

	return xgrid, ygrid, counts, scatter_points

def strauss_plot(ax, x, y, cmap='viridis', scatter_color='k', scatter_marker='.',
		  alpha = 1.0, **kwargs):
	""" 
	Add Strauss plot to `matplotlib.Axes` instance `ax`
	
	Arguments
	---------

	ax : matplotlib.Axes instance
	   Axis on which to plot the strauss plot

	x : array-like, one-dimensional
	   X values for the data

	y : array-like, one-dimensional
	   Y values for the data (corresponding to the X values)

	cmap : string
	   Name of a maplotlib colormap

	scatter_color : string
	   Color of the scatter markers (defaults to black, 'k')

	scatter_marker : string
	   Marker type for the scatterplot (defaults to .)

	alpha : float, (0, 1)
	   alpha value for the scatter points

	"""
	
	xgrid, ygrid, counts, scatter_points = get_grid_and_scatter(x, y, **kwargs)

	masked_counts = np.ma.masked_where(counts == 0, counts)


	palette = plt.get_cmap(cmap)
	palette.set_bad(alpha=0.0)

	
	sx, sy = zip(*scatter_points)
	ax.scatter(sx, sy, marker=scatter_marker,alpha=alpha, color=scatter_color, s=1)
	ax.set_xlim(xgrid.min(),xgrid.max())
	ax.set_ylim(ygrid.min(), ygrid.max())

	pcol = ax.pcolor(xgrid, ygrid, masked_counts, cmap=palette)
	cbar = plt.colorbar(pcol)



if __name__ == '__main__':
	f, ax = plt.subplots()
	x = np.random.normal(loc=10, size=50000)
	y = np.random.normal(size=50000)

	strauss_plot(ax, x, y)
	ax.axhline(0, color='k', ls=':')
	ax.axvline(10, color='k', ls=':')
	plt.show()


	




import xarray as xr
import matplotlib.pyplot as plt

url = 'http://test.opendap.org/dap/data/nc/sst.mnmean.nc.gz'

ds = xr.open_dataset(url)
print(ds)

#data variable
sst = ds.sst

#timestamp
dsloc = sst.isel(time=1730) 

#regular graph
plt.figure(1)
dsloc.plot()

#discrete colormap with some cool colors
flatui = ['#ff8c0f', '#faf11c', '#71e943', '#43dce9', '#4343e9', '#8c43e9', '#f50fff', '#ff0f6f']

plt.figure(2)
discrete = dsloc.copy()
discrete.plot(levels=8, colors=flatui)

#make it fancy
plt.title('Worldwide sea temperature in March 1998')
plt.tight_layout()

#show the graph(s)
print('check new window with figure(s)')
plt.show()







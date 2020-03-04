import xarray as xr
import matplotlib.pyplot as plt

url = 'http://test.opendap.org/dap/data/nc/sst.mnmean.nc.gz'

ds = xr.open_dataset(url)
print(ds)

#data variable
sst = ds.sst

#print data of North Sea at Dutch coast
dsloc = sst.sel(lon=4, lat=52, method='nearest') 

#regular graph
dsloc.plot()

#line graph with custom settings
dsloc.plot.line(color='purple', marker='o') 

#multiple graphs
fig, axes = plt.subplots(ncols=2) 
dsloc.plot(ax=axes[0]) 
dsloc.plot.hist(ax=axes[1]) 


plt.tight_layout() 

#show the graph(s)
print('check new window with figure(s)')
plt.show()







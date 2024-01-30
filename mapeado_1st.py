import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import pyproj
import verde as vd

data = pd.read_csv('anomalia_airelibre_1arcmin.csv')

data = data.where(data['lon']>-72).dropna()

projection = pyproj.Proj(proj="utm",zone=19, ellps='WGS84', preserve_units=False)
x,y = projection(data.lon, data.lat)

coordinates = (x,y)
region=vd.get_region((data.lon,data.lat))
spacing = 1/60

## Linear interpolation
# grd = vd.Linear().fit(coordinates,data.anom_al_mgal)
# grid = grd.grid(region=region,spacing=spacing, projection=projection, dims=['lat','lon'], data_names="anom_al_mgal")

#nearest neighbors interpolation, k being number of neighbors to consider
grd = vd.KNeighbors(k=10)
grd.fit(coordinates, data.anom_al_mgal)
grid = grd.grid(region=region, spacing=spacing, projection=projection,dims=['lat','lon'], data_names="anom_al_mgal")
crs = ccrs.PlateCarree()

plt.figure(figsize=(7,6))
ax= plt.axes(projection=ccrs.UTM(zone=19))
ax.coastlines()
pc = grid.anom_al_mgal.plot.pcolormesh(ax=ax,transform=crs, zorder=-1, cmap = 'jet', add_colorbar=False)
plt.colorbar(pc).set_label('mgal')

plt.savefig('anom_al_1arcmin_5neighbors')
plt.show()
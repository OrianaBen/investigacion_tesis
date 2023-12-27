import pandas as pd
import boule as bl
from filtrado_datos import save_table_tocsv

df = pd.read_csv('def_data.csv')
gravity = df.to_xarray()
# gravity = gravity.to_array()
# print(gravity)

ellipsoid = bl.WGS84
normal_gravity = ellipsoid.normal_gravity(gravity.lat, gravity.altura_m)

gravity_disturbance = gravity.grav_obs_mgal - normal_gravity
grav_dis_mgal = gravity_disturbance.to_dataframe(name='grav_dis_mgal')

file = df.join(grav_dis_mgal)
save_table_tocsv(file, 'grav_dist_graterol.csv')


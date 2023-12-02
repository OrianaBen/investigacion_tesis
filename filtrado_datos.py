import pandas as pd

def read_data(file_path, cols,rows=0,labels=[]):
    """Lee datos crudos y retorna un df.
    Argumentos:
    file_path -- ubicación del archivo
    cols -- columnas que se leerán
    rows -- fila desde la que se comenzará a leer (default 0)
    labels -- header que tendrá el Dataframe (default empty list)"""

    table = pd.read_table(file_path,sep='\s+',header=None,usecols=cols,skiprows=rows,names=labels)
    return table

def filter_data(table, lon_label, lat_label, max_lon, min_lon, max_lat, min_lat):
    """Filtrado de datos con las coordenadas deseadas. Retorna un df sin valores nulos.
    Argumentos:
    table -- dataframe con el que se trabajará
    lon_label,lat_label -- nombre de la columna de longitud/latitud en el header
    max_lon, min_lon -- cota superior para el filtrado de longitud
    max_lat, min_lat -- cota superior para el filtrado de latitud"""
    
    filtered_table = table.where(
        (table[lon_label]<max_lon) & (table[lon_label]>min_lon) &
        (table[lat_label]<max_lat) & (table[lat_label]>min_lat) 
    )    
    return filtered_table.dropna()

def save_table_tocsv(dataframe, path):
    """Convierte df a archivo csv
    Argumentos:
    dataframe -- archivo a convertir
    path -- ubicación y nombre del archivo resultante"""

    dataframe.to_csv(path)

def minus_360(dataframe,label):
    """Resta el valor 360 a una columna.
    Argumentos:
    dataframe -- archivo de entrada
    label -- identificación de la columna en el header"""

    dataframe[label] = dataframe[label].apply(lambda x: x-360)

file = read_data(
    'datos_crudos/BASEBougTIERRAFebrero2018.DAT',
    [0,1,4,5,6],
    labels=['lon', 'lat','base','altura(m)','grav_obs(mgal)']
)

save_table_tocsv(
        filter_data(file,'lon','lat',-68.2,-73.6,12.8,6.3),
        'def_data.csv'
    )

file = read_data(
    'datos_crudos/EIGEN-6C4_1713c2_P1.gdf',
    [0,1,2,3],
    35,
    labels=['lon','lat','altura(m)','grav_anom(mgal)']
    )

minus_360(file,'lon')

save_table_tocsv(file,'satelitalesp1.csv')

file = read_data(
    'datos_crudos/EIGEN-6C4_ce9e3_P2.gdf',
    [0,1,2,3],
    35,
    labels=['lon','lat','altura(m)','grav_anom(mgal)']
    )

minus_360(file,'lon')

save_table_tocsv(file,'satelitalesp2.csv')
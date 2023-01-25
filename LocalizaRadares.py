import geopandas as gpd
from  shapely.geometry import Point, Polygon
import pandas as pd
import folium

radaresCoord = pd.read_csv('./coordenadas.csv', encoding='ansi')


pontos_geo = []
for xy in zip(radaresCoord['X'], radaresCoord['Y']):
    pontos_geo.append(Point(xy))


localizacoes_geo = gpd.GeoDataFrame(radaresCoord,
                                    crs = {'init': 'epsg:4326'},
                                    geometry = pontos_geo)

fig = folium.Map(width=900, height=600)

pontos = localizacoes_geo[['X', 'Y']].values.tolist()
for point in range(0, len(pontos)):
    folium.Marker(locationlist[point]).add_to(fig)
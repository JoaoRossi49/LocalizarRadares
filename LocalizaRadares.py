import pandas as pd
import folium

Coordenadas = pd.read_csv(r"LocalizarRadares\coordenadas.csv", encoding='ansi')


center = [-22.210868, -49.9373]
map_kenya = folium.Map(location=center, zoom_start=20)


for index, Coordenadas in Coordenadas.iterrows():
    local = [Coordenadas['X'],Coordenadas['Y']]
    folium.Marker(local, popup=f'Tipo do Radar: {Coordenadas["Tipo"]}').add_to(map_kenya)
    

#Salva mapa com pontos em formato html
map_kenya.save('Mapa.html')
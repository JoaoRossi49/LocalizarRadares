import pandas as pd
import folium

#Alimenta variável Coordenadas com conteúdo de .csv
Coordenadas = pd.read_csv(r"LocalizarRadares\coordenadas.csv", encoding='ansi')

#Define um ponto central no mapa, no caso a cidade de Marília
center = [-22.210868, -49.9373]
map_kenya = folium.Map(location=center, zoom_start=20)

#Cria pontos no mapa utilizando coordenadas
for index, Coordenadas in Coordenadas.iterrows():
    local = [Coordenadas['X'],Coordenadas['Y']]
    folium.Marker(local, popup=f'Tipo do Radar: {Coordenadas["Tipo"]}', 
    icon=folium.Icon(icon="info-sign", color="red")).add_to(map_kenya)
    

#Salva mapa com pontos em formato html
map_kenya.save('Mapa.html')
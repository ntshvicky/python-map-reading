import pandas
import folium
import numpy
file = pandas.read_csv("Volcanoes.txt")
lat=list(file.LAT)
lon=list(file.LON)
elev = list(file["ELEV"])
vname=list(file.NAME)

latmean=numpy.median(lat)
lonmean=numpy.median(lon)

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[latmean,lonmean], zoom_start=3, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="Volcanos")
for i,j,k,l in zip(vname,lat,lon,elev):
    iframe = folium.IFrame(html=html % (i, i, l), width=200, height=100)
    #fg.add_child(folium.Marker(location=[j,k], popup=folium.Popup(iframe), tooltip=i, icon=folium.Icon(color="red")))
    fg.add_child(folium.CircleMarker(location=[j,k], radius=6, popup="Hi! I am "+i+" in "+str(j)+" and "+str(k)+"", tooltip="marker", fill_color="green", color="red", fill_opacity="1"))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'red'}))

map.add_child(fgp)
map.add_child(fg)
map.add_child(folium.LayerControl())
#map.save("Volcanoes.html")
map.save("Volcanoes_pophtml.html")

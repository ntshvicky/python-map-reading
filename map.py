import folium
map = folium.Map(location=[23.35,85.24], tiles="Stamen Terrain")
#map.add_child(folium.Marker(location=[23.35,85.24], popup="Hi! I am marker in 23.35 and 85.24", tooltip="marker", icon=folium.Icon(color="red")))
fg = folium.FeatureGroup(name="My Map")
#fg.add_child(folium.CircleMarker(location=[23.35,85.24], popup="Hi! I am marker in 23.35 and 85.24", tooltip="marker"))
fg.add_child(folium.Marker(location=[23.35,85.24], popup="Hi! I am marker in 23.35 and 85.24", tooltip="marker1", icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=[23.09,85.10], popup="Hi! I am marker in 23.09and 85.10", tooltip="marker2", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map2.html")
import folium as fm
import os
import settings
import vaca
    
def get_html(event_path):
    f = open(event_path + "/html.txt", "r")
    html = f.read()
    f.close()
    return html
    
def get_location(event_path):
    f = open(event_path + "/coords.txt", "r")
    coords = [float(f.readline()), float(f.readline())]
    f.close()
    return coords
    
    
base = fm.Map(location = settings.start_coords, zoom_start = settings.zoom, tiles = 'stamenwatercolor')
fm.TileLayer('Stamen Terrain').add_to(base)


centuries = settings.main_folders

for century in centuries:
    
    century_path = settings.main_path + '/' + century
    categories = os.listdir(century_path)
    
    group = fm.map.FeatureGroup(name = century)
    
    if century == "Antes de 1750":
        fm.PolyLine(vaca.path, color='blue', dash_array = '10', tooltip = 'Viaje de Cabeza de Vaca').add_to(group)
        
    for category in categories:
        category_path = century_path + '/' + category
        things = os.listdir(category_path)
        
        for thing in things:
            thing_path = category_path + '/' + thing
            
            html = get_html(thing_path)
            coords = get_location(thing_path)
            
            popup = fm.Popup(html = html, max_width = settings.popup_width)
            icon = fm.Icon(color=settings.colors[category], icon = settings.icons[category], prefix = 'fa')
            
            marker = fm.Marker(location = coords, icon = icon, popup = popup, tooltip = "Haz clic")
            marker.add_to(group)
        
    group.add_to(base)

# Create title
#base.get_root().html.add_child(fm.Element(settings.title_html))

fm.LayerControl().add_to(base)
base.save("index.html")


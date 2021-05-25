import folium as fm

# Paths
main_path = "Map Folder"
main_folders = ["Antes de 1750", "1750 - 1850", "1850 - 1950", "1950 al presente"]

# Map Settings
start_coords = [31.7953, -94.1803]
zoom = 5

# Title
title_html = '''
             <h4 style="text-align: center;"><em>El mapa de la historia chicano</em></h4>
             '''

# Icons
icons = {'Personas':'user',
         'Resistencias':'hand-rock-o',
         'Literatura':'book',
         'Musica':'music',
         'Arte':'paint-brush',
         'Medios':'film',
         'Migraciones':'home'}

colors = {'Personas':'blue',
          'Resistencias':'darkgreen',
          'Literatura':'gray',
          'Musica':'red',
          'Arte':'green',
          'Medios':'darkpurple',
          'Migraciones':'beige'}

# Popup Settings
popup_width = 700

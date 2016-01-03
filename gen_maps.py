import ds_pygmaps as pygmaps
import par

final = par.parse_json()
mymap = pygmaps.maps(22.69781, 120.960515, 8)
for i in range(len(final)):
    if (final[i]['x1'] != '') and (final[i]['y1'] != ''):
        mymap.addpoint(final[i], "#0000FF")
mymap.draw('./index.html')

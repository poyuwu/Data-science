import ds_pygmaps as pygmaps
import par

final = par.parse_json()
mymap = pygmaps.maps(22.69781, 120.960515, 8)
#mymap.setgrids(22.65, 22.75, 0.001, 120.90, 121.05, 0.001)
for i in range(len(final)):
    if (final[i]['x1'] != '') and (final[i]['y1'] != ''):
        title = final[i]['roadtype']
        mymap.addpoint(final[i], "#0000FF")
mymap.draw('./mymap.html')

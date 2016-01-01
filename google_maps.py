import ds_pygmaps as pygmaps
import par

final = par.parse_json()
mymap = pygmaps.maps(22.69781, 120.960515, 8)
#mymap.setgrids(22.65, 22.75, 0.001, 120.90, 121.05, 0.001)
#for i in range(len(final)):
for i in range(440, 450):
    if (final[i]['x1'] != '') and (final[i]['y1'] != ''):
        comments = final[i]['comment'].splitlines()
        comments[0].strip('"')
        mymap.addpoint(float(final[i]['y1']), float(final[i]['x1']), "#0000FF", comments[0])
mymap.draw('./mymap.html')

# -*- coding: utf8 -*-
import ds_pygmaps as pygmaps
import par
import sys
import datetime

if __name__ == '__main__':
    final = par.parse_json()
    mymap = pygmaps.maps(22.69781, 120.960515, 8)
    beginTime_flag, endTime_flag, type_flag, region_flag = False, False, False, False
    output = 'index.html'
    for i in range(len(sys.argv)):        
        if sys.argv[i].startswith('-h'):
            print '\nUsage:\n\tpython gen_maps.py [-b %Y-%m-%d,%H:%M:%S | -e %Y-%m-%d,%H:%M:%S | -t [roadtype] | -r [region] | -o [output_html_filename]]'
            print '\t-b: begin_time, \n\t-e: end_time.'
            print '\t-t: roadtype = ["其他", "事故", "阻塞", "交通障礙", "交通管制", "號誌故障", "道路施工", "災變", "正常"]'
            print '\t-r: region = ["A", "N", "M", "S", "E"]'
            print '\t-o: output file name, e.g. foo.html, default = "index.html"\n'
            sys.exit()
        elif sys.argv[i].startswith('-b'):
            i += 1
            begin_time = datetime.datetime.strptime(sys.argv[i], '%Y-%m-%d,%H:%M:%S')
            beginTime_flag = True
        elif sys.argv[i].startswith('-e'):
            i += 1
            end_time = sys.argv[i]
            end_time = datetime.datetime.strptime(sys.argv[i], '%Y-%m-%d,%H:%M:%S')
            endTime_flag = True
        elif sys.argv[i].startswith('-t'):
            i += 1
            road_type = sys.argv[i]
            type_flag = True
        elif sys.argv[i].startswith('-r'):
            i += 1
            region = sys.argv[i]
            region_flag = True
        elif sys.argv[i].startswith('-o'):
            i += 1
            output = sys.argv[i]

    for i in range(len(final)):
        if (final[i]['x1'] != '') and (final[i]['y1'] != ''):
            try:
                    happen_time = datetime.datetime.strptime(final[i]['happendate']+'T'+final[i]['happentime'][0:8],'%Y-%m-%dT%H:%M:%S')
            except:
                    happen_time = final[i]['happendate'].encode('utf-8') + final[i]['happentime'].encode('utf-8')
            if (type_flag == True) and (final[i]['roadtype'].encode('utf-8') != road_type):
                continue
            if (beginTime_flag == True) and (type(happen_time) == datetime.datetime) and (happen_time <= begin_time):
                continue
            if (endTime_flag == True) and (type(happen_time) == datetime.datetime) and (happen_time >= end_time):
                continue
            if (region_flag == True) and (final[i]['region'].encode('utf-8') != region):
                continue
            mymap.addpoint(final[i], "#0000FF")
    mymap.draw(output)


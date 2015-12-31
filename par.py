import json
import urllib2
import time
#f = open('result.json','w')
data = []
for i in range(12):
    if i ==0:
        continue
    #flag = 1
    f = open('result'+str(i)+'.json')
    text = f.read()
    newDic = json.loads(text)
    result = newDic['result']
    #N = len(data)
    #for j in range(len(data)):
    #    if data[N-1-j] == result[0]:
    #        print "QQ"
    #        data[:N-1-j] += result
    #        flag=0
    #        break
    #if flag == 1:
    data+=result
    f.close()
final = = [dict(t) for t in set([tuple(d.items()) for d in data])]

""" 
response = urllib2.urlopen('http://210.69.35.216/data/api/pbs')
html = response.read()
newDic = json.loads(html)
result = newDic['result']
pre_result = result
for i in range(len(result)):
    print result[i]
"""
#print 'in each UID,exist value'
#for i in result[0]:
#    print i
#while(1):
#    time.sleep(60*60*24)
#    response = urllib2.urlopen('http://210.69.35.216/data/api/pbs')
#    html = response.read()
#    newDic = json.loads(html)
#    result = newDic['result']
#    pre_result = result
        
#if __name__ == '__main__':


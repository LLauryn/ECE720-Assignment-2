import pandas as pd
import csv

csvfile = pd.read_csv('data/OtherData/vben2_unremoved.csv')
newfile = open('data/OtherData/5-VBEN2.csv', 'w', newline='')
writer = csv.writer(newfile)
writer.writerow(['from','to','weight'])

fromid = csvfile['from']
toid = csvfile['to']
weight = csvfile['weight']
pair=[]
pairw=[]

for i in range(len(fromid)):
    temp=[fromid[i],toid[i]]
    # pair.append()
    if temp in pair:
        x=pair.index(temp)
        a=pairw[x]
        pairw[x][2]=pairw[x][2]+weight[i]
    if temp not in pair:
        pair.append(temp)
        pairw.append(temp+[weight[i]])
for i in pairw:
    writer.writerow(i)
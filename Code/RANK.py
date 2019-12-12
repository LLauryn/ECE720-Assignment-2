import pandas as pd
import csv

csvfile = pd.read_csv('data/OtherData/allPosts.csv',encoding='ISO-8859-1')
uid = csvfile['OwnerId']
link = csvfile['OwnerLink']
name = csvfile['OwnerDisplayName']
newfile = open('data/OtherData/topuserinfo.csv', 'w', newline='')
writer = csv.writer(newfile)
writer.writerow(['UserId','displayName','ProfileLink'])
id= [2336654, 4686625, 2901002, 9209546, 4909087, 704848, 624829, 4333359, 10201580, 3483203, 4238408, 7964527, 5741205, 6361531, 190597, 9698684, 7093741, 6287308, 2535611]

for i in range(len(id)):
    for j in range(len(uid)):
        if int(id[i])==int(uid[j]):
            writer.writerow([id[i], name[j], link[j]])
            break
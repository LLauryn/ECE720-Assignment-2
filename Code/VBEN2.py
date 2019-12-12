import csv

csvfile1 = open('data/OtherData/ARNwV.csv','r')
reader1 = csv.reader(csvfile1)
csvfile2 = open('data/OtherData/4-VBEN.csv','r')
reader2 = csv.reader(csvfile2)

newfile = open('data/OtherData/vben2_unremoved.csv', 'w', newline='')
writer = csv.writer(newfile)
writer.writerow(['from','to','weight'])

next(reader1)
for i in reader1:
    if int(i[1])<int(i[3]):
        w = int(i[3])-int(i[1])
        writer.writerow([i[0],i[2], w])

next(reader2)
for i in reader2:
    writer.writerow(i)


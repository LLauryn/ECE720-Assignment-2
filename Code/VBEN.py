import pandas as pd
import csv
#make ARNwV.csv
csvfile1 = pd.read_csv('data/OtherData/users_vote.csv')
csvfile2 = open('data/OtherData/1_ARN.csv','r')
reader = csv.reader(csvfile2)

newfile = open('data/OtherData/ARNwV.csv', 'w', newline='')
writer = csv.writer(newfile)

uid = csvfile1['UserId']
score = csvfile1['Score']
users = []
vote = []
for i in range(len(uid)):
    users.append(uid[i])
    vote.append(score[i])

writer.writerow(['from','Score1','to','Score2'])
next(reader)
for i in reader:
    x = users.index(int(i[0]))
    y = users.index(int(i[1]))
    v1 = vote[x]
    v2 = vote[y]
    writer.writerow([i[0], v1, i[1],v2])

#VBEN
csvfile = pd.read_csv('data/OtherData/ARNwV.csv')
newfile = open('data/OtherData/vben_unremoved.csv', 'w', newline='')
writer = csv.writer(newfile)
writer.writerow(['from','to','weight'])

askerid = csvfile['from']
score1 = csvfile['Score1']
answerid = csvfile['to']
score2 = csvfile['Score2']

i=0
while i<len(askerid):
    temp = askerid[i]
    j=i+1
    nodes=[answerid[i]]
    vote = [score2[i]]
    while j<len(askerid) and temp==askerid[j]:
        nodes.append(answerid[j])
        vote.append(score2[j])
        j=j+1
        i=i+1
    i=i+1
    if len(nodes)==1:
        continue
    for k in range(len(nodes)):
        s = vote[k]
        for l in range(len(nodes)):
            sn = vote[l]
            if s<sn:
                w = sn-s
                writer.writerow([nodes[k], nodes[l], w])




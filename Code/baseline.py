import pandas as pd
import csv

csvfile = pd.read_csv('data/OtherData/users_vote.csv')
id = csvfile['UserId']
score = csvfile['Score']
newfile = open('data/OtherData/top10userscore.csv', 'w', newline='')
writer = csv.writer(newfile)
writer.writerow(['userId','Score'])
node=[]
vote=[]

for i in range(len(id)):
    if id[i] in node:
        x = node.index(id[i])
        vote[x]=vote[x]+score[i]
    if id[i] not in node:
        node.append(id[i])
        vote.append(score[i])

index = sorted(range(len(vote)), key=lambda k: vote[k],reverse = True)

for i in range(10):
    writer.writerow([node[index[i]], vote[index[i]]])


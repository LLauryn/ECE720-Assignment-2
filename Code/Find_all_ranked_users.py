import pandas as pd
import csv
#Find all ranked users
node_score=pd.read_csv('data/OtherData/VBENpagerank.csv')
matrix=pd.read_csv('data/OtherData/4_VBEN_matrix_prun.csv')
head=[]
index=[]
for i in node_score["node"]:
    head.append(matrix["Unnamed: 0"][i-1])

node_score=pd.read_csv('data/OtherData/VBEN2pagerank.csv')
matrix=pd.read_csv('data/OtherData/5_VBEN2_matrix_prun.csv')
for i in node_score["node"]:
    if matrix["Unnamed: 0"][i-1] not in head:
        head.append(matrix["Unnamed: 0"][i-1])

node_score=pd.read_csv('data/OtherData/ARNpagerank.csv')
matrix=pd.read_csv('data/OtherData/1_ARN_matrix_prun.csv')
for i in node_score["node"]:
    if matrix["Unnamed: 0"][i-1] not in head:
        head.append(matrix["Unnamed: 0"][i-1])

node_score=pd.read_csv('data/OtherData/CBENpagerank.csv')
matrix=pd.read_csv('data/OtherData/3_CBEN_matrix_prun.csv')
for i in node_score["node"]:
    if matrix["Unnamed: 0"][i-1] not in head:
        head.append(matrix["Unnamed: 0"][i-1])

node_score=pd.read_csv('data/OtherData/ABANpagerank.csv')
matrix=pd.read_csv('data/OtherData/2_ABAN_matrix_prun.csv')
for i in node_score["node"]:
    if matrix["Unnamed: 0"][i-1] not in head:
        head.append(matrix["Unnamed: 0"][i-1])

#ARN all ranked user&score
node_score=pd.read_csv('data/OtherData/ARNrank.csv')
matrix=pd.read_csv('data/OtherData/1_ARN_matrix_prun.csv')
f4=open('ARN_user_PRscore.csv','w',newline='')
write4=csv.writer(f4)
header=["UserId","score"]
write4.writerow(header)
user_id_list=[]
for i in range(len(matrix["Unnamed: 0"])):
    user_id_list.append([matrix["Unnamed: 0"][i],node_score["rank"][i]])
for j in range(len(user_id_list)):
    if user_id_list[j][0] in head:
        write4.writerow(user_id_list[j])

#ABAN all ranked user&score
node_score=pd.read_csv('data/OtherData/ABANrank.csv')
matrix=pd.read_csv('data/OtherData/2_ABAN_matrix_prun.csv')
f4=open('data/OtherData/ABAN_user_PRscore.csv','w',newline='')
write4=csv.writer(f4)
header=["UserId","score"]
write4.writerow(header)
user_id_list=[]
for i in range(len(matrix["Unnamed: 0"])):
    user_id_list.append([matrix["Unnamed: 0"][i],node_score["rank"][i]])
for j in range(len(user_id_list)):
    if user_id_list[j][0] in head:
        write4.writerow(user_id_list[j])

#CBEN all ranked user&score
node_score=pd.read_csv('data/OtherData/CBENrank.csv')
matrix=pd.read_csv('data/OtherData/3_CBEN_matrix_prun.csv')
f4=open('data/OtherData/CBEN_user_PRscore.csv','w',newline='')
write4=csv.writer(f4)
header=["UserId","score"]
write4.writerow(header)
user_id_list=[]
for i in range(len(matrix["Unnamed: 0"])):
    user_id_list.append([matrix["Unnamed: 0"][i],node_score["rank"][i]])
for j in range(len(user_id_list)):
    if user_id_list[j][0] in head:
        write4.writerow(user_id_list[j])

#VBEN all ranked user&score
node_score=pd.read_csv('data/OtherData/VBENrank.csv')
matrix=pd.read_csv('data/OtherData/4_VBEN_matrix_prun.csv')
f4=open('data/OtherData/VBEN_user_PRscore.csv','w',newline='')
write4=csv.writer(f4)
header=["UserId","score"]
write4.writerow(header)
user_id_list=[]
for i in range(len(matrix["Unnamed: 0"])):
    user_id_list.append([matrix["Unnamed: 0"][i],node_score["rank"][i]])
for j in range(len(user_id_list)):
    if user_id_list[j][0] in head:
        write4.writerow(user_id_list[j])

#VBEN2 all ranked user&score
node_score=pd.read_csv('data/OtherData/VBEN2rank.csv')
matrix=pd.read_csv('data/OtherData/5_VBEN2_matrix_prun.csv')
f4=open('data/OtherData/VBEN2_user_PRscore.csv','w',newline='')
write4=csv.writer(f4)
header=["UserId","score"]
write4.writerow(header)
user_id_list=[]
for i in range(len(matrix["Unnamed: 0"])):
    user_id_list.append([matrix["Unnamed: 0"][i],node_score["rank"][i]])
for j in range(len(user_id_list)):
    if user_id_list[j][0] in head:
        write4.writerow(user_id_list[j])
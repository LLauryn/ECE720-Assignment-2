import json
import csv
import codecs
#get question.json and answer.json
jsonData1 = codecs.open('data/OtherData/question_data_filtered.json', 'r', 'utf-8')
jsonData2 = codecs.open('data/OtherData/answers_data_filtered.json', 'r', 'utf-8')
f1 = open('data/OtherData/question.json','wt')
f2 = open('data/OtherData/answer.json','wt')

for t in jsonData1:
    dic = json.loads(t)
    dic = dic["items"]
    for i in dic:
        f1.write(json.dumps(i))
        f1.write('\n')
for t in jsonData2:
    dic = json.loads(t)
    for i in dic:
        f2.write(json.dumps(i))
        f2.write('\n')

#get allPosts.csv
jsonData1 = codecs.open('data/OtherData/question.json', 'r', 'utf-8')
jsonData2 = codecs.open('data/OtherData/answer.json', 'r', 'utf-8')
csvfile = open('data/OtherData/allPosts.csv', 'w', newline='')
writer = csv.writer(csvfile)#, delimiter='\t'
keys = ['Tags','OwnerReputation','OwnerUserId','OwnerUserType','OwnerAcceptRate','OwnerProfileImage','OwnerDisplayName',
        'OwnerLink','IsAnswered','ViewCount','AcceptedAnswerId','AnswerCount','Score','LastActivityDate','CreationDate',
        'LastEditDate','PostId','ParentId','Link','Title','PostTypeID']
writer.writerow(keys)
keys1 = ['tags', 'reputation', 'user_id', 'user_type', 'accept_rate','profile_image', 'display_name', 'ulink', 'is_answered',
         'view_count','accepted_answer_id', 'answer_count', 'score', 'last_activity_date', 'creation_date', 'last_edit_date',
         'answer_id', 'question_id', 'link', 'title']
for dic in jsonData1:
    values = []
    dic = json.loads(dic)
    k = list(dic.keys())
    v = list(dic.values())
    k.remove(k[1])
    v.remove(v[1])
    k2 = list(dic['owner'].keys())
    if 'link' in k2:
        k2[k2.index('link')]='ulink'
    v2 = list(dic['owner'].values())
    for i in range(len(k2)):
        k.insert(i + 1, k2[i])
        v.insert(i + 1, v2[i])
    for j in range(len(keys1)):
        if keys1[j] in k:
            x = k.index(keys1[j])
            values.append(v[x])
        else:
            values.append('')
    writer.writerow(['python;python-3.x;pandas',values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],
                     values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[17],'',values[18],values[19],1])

for dic in jsonData2:
    values = []
    dic = json.loads(dic)
    k = list(dic.keys())
    v = list(dic.values())
    k.remove(k[1])
    v.remove(v[1])
    k2 = list(dic['owner'].keys())
    if 'link' in k2:
        k2[k2.index('link')]='ulink'
    v2 = list(dic['owner'].values())
    for i in range(len(k2)):
        k.insert(i + 1, k2[i])
        v.insert(i + 1, v2[i])
    for j in range(len(keys1)):
        if keys1[j] in k:
            x = k.index(keys1[j])
            values.append(v[x])
        else:
            values.append('')
    writer.writerow(['',values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],
                     values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],2])


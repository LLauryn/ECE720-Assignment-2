import json
import csv
#ABAN
question=json.load(open("data/OtherData/question_data_filtered.json"))
answer=json.load(open("data/OtherData/answers_data_filtered.json"))
edge=[]

for i in range(len(question["items"])):
    q_id=question["items"][i]["question_id"]
    score=[]
    iter_answer=[]
    best_score=0
    if 'user_id' in question["items"][i]["owner"]:
        asker=question["items"][i]["owner"]["user_id"]
    else:
        asker=question["items"][i]["owner"]["display_name"]
    for j in range(len(answer)):
        if answer[j]["question_id"]==q_id:
            iter_answer.append(answer[j])
            score.append(answer[j]["score"])
    if score!=[]:
        best_score=max(score)
        for m in range(len(iter_answer)):
            if iter_answer[m]["score"]==best_score:
                if 'user_id' in iter_answer[m]["owner"]:
                    answerer=iter_answer[m]["owner"]["user_id"]
                else:
                    answerer=iter_answer[m]["owner"]["display_name"]
                edge.append([asker,answerer])

f = open('data/OtherData/2-ABAN.csv', 'w', newline='')
writer = csv.writer(f)
head = ["from","to"]
writer.writerow(head)
for i in range(len(edge)):
    writer.writerow(edge[i])


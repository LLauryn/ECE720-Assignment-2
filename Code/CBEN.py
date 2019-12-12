import json
import csv
question=json.load(open("question_data_filtered.json"))
answer=json.load(open("answers_data_filtered.json"))
edge=[]
for i in range(len(question["items"])):
    q_id=question["items"][i]["question_id"]
    score=[]
    iter_answer=[]
    best_answer=[]
    poor_answer=[]
    best_score=0
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
                best_answer.append(answerer)
            else:
                if 'user_id' in iter_answer[m]["owner"]:
                    answerer=iter_answer[m]["owner"]["user_id"]
                else:
                    answerer=iter_answer[m]["owner"]["display_name"]
                poor_answer.append(answerer)
    if best_answer!=[] and poor_answer!=[]:
        for b_answer in best_answer:
            for p_answer in poor_answer:
                edge.append([p_answer,b_answer])

f = open('data/OtherData/3-CBEN.csv', 'w', newline='')
writer = csv.writer(f)
head = ["from","to"]
writer.writerow(head)
for i in range(len(edge)):
    writer.writerow(edge[i])

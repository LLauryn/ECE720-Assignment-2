import csv
import json
question=json.load(open("data/OtherData/question_data_filtered.json"))
answer=json.load(open("data/OtherData/answers_data_filtered.json"))
result=[]
for i in range(len(question["items"])):
    q_id=question["items"][i]["question_id"]
    if 'user_id' in question["items"][i]["owner"]:
        asker=question["items"][i]["owner"]["user_id"]
    else:
        asker=question["items"][i]["owner"]["display_name"]
    for j in range(len(answer)):
        if answer[j]["question_id"]==q_id:
            if 'user_id' in answer[j]["owner"]:
                answerer = answer[j]["owner"]["user_id"]
            else:
                answerer = answer[j]["owner"]["display_name"]
            result.append([asker, answerer])
# print(result)
f = open('data/OtherData/1-ARN.csv', 'w', newline='')
writer = csv.writer(f)
head = ["from","to"]
writer.writerow(head)
for i in range(len(result)):
    writer.writerow(result[i])


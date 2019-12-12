import csv
import pandas as pd
# generate ARN matrix
edge = pd.read_csv('data/OtherData/1_ARN.csv')
f5 = open('data/OtherData/1_ARN_matrix.csv', 'w', newline='')
write5 = csv.writer(f5)
user_dict = {}
user_index = 0
head = ['']
edge_list = []
for i in range(len(edge)):
    edge_list.append([edge["from"][i], edge["to"][i]])
for e_list in edge_list:
    for user in e_list:
        if str(user) not in user_dict:
            head.append(user)
            user_dict[str(user)] = user_index
            user_index += 1

write5.writerow(head)
ARN_matrix = [[0 for i in range(len(user_dict))] for i in range(len(user_dict))]
for [x, y] in edge_list:
    x_index = user_dict[str(x)]
    y_index = user_dict[str(y)]
    ARN_matrix[x_index][y_index] += 1
for i in range(len(head) - 1):
    w = [head[i + 1]]
    w.extend(ARN_matrix[i])
    write5.writerow(w)


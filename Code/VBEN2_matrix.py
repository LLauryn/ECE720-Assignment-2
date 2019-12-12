import csv
import pandas as pd
# generate VBEN2 matrix
edge = pd.read_csv('data/OtherData/5_VBEN2.csv')
f5 = open('data/OtherData/5_VBEN2_matrix.csv', 'w', newline='')
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
VBEN2_matrix = [[0 for i in range(len(user_dict))] for i in range(len(user_dict))]
for [x, y] in edge_list:
    x_index = user_dict[str(x)]
    y_index = user_dict[str(y)]
    VBEN2_matrix[x_index][y_index] += 1
for i in range(len(head) - 1):
    w = [head[i + 1]]
    w.extend(VBEN2_matrix[i])
    write5.writerow(w)
import pandas as pd
import csv
edge = pd.read_csv('vbenremove.csv')
edge_list = []
edge_list_weight = []
for i in range(len(edge)):
    edge_list.append([edge["from"][i], edge["to"][i]])
    edge_list_weight.append([edge["from"][i], edge["to"][i], edge["weight"][i]])
head = []
for e_list in edge_list:
    for user in e_list:
        if str(user) not in head:
            head.append(str(user))

node = pd.read_csv('D:/Study/ECE720 S2/Assignment2/VBEN_node.csv')
node_list = []
for i in range(len(node)):
    node_list.append(int(node["node"][i]))
print("node_list", len(node_list))

head_new = []
for i in range(len(head)):
    if i + 1 in node_list:
        head_new.append(head[i])
print("head_new", len(head_new))

edge_new = []
weight = []
for user in edge_list_weight:
    if str(user[0]) in head_new and str(user[1]) in head_new:
        edge_new.append([user[0], user[1]])
        weight.append(user[2])

user_dict = {}
user_index = 0
for user in head_new:
    user_dict[str(user)] = user_index
    user_index += 1

f5 = open('VBEN_matrix_prun.csv', 'w', newline='')
write5 = csv.writer(f5)
head1 = ['']
head1.extend(head_new)
write5.writerow(head1)
VBEN_matrix = [[0 for i in range(len(user_dict))] for i in range(len(user_dict))]
for i in range(len(edge_new)):
    x_index = user_dict[str(edge_new[i][0])]
    y_index = user_dict[str(edge_new[i][1])]
    VBEN_matrix[x_index][y_index] = weight[i]
for i in range(len(head1) - 1):
    w = [head1[i + 1]]
    w.extend(VBEN_matrix[i])
    write5.writerow(w)


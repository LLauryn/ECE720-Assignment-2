

library(igraph)
library(sna)
library(CINNA)
set.seed(10)
id=read.table(file = 'data/OtherData/1_ARN_matrix.tsv',  header = TRUE)
id_matrix=as.matrix(id)

id=read.table(file = 'data/OtherData/2_ABAN_matrix.tsv',  header = TRUE)
id_matrix=as.matrix(id)

id=read.table(file = 'data/OtherData/3_CBEN_matrix.tsv',  header = TRUE)
id_matrix=as.matrix(id)

id=read.table(file = 'data/OtherData/4_VBEN_matrix.tsv',  header = TRUE)
id_matrix=as.matrix(id)

id=read.table(file = 'data/OtherData/5_VBEN2_matrix.tsv',  header = TRUE)
id_matrix=as.matrix(id)


#plot graph
gplot(id_matrix)


#pruning component
g=graph.adjacency(id_matrix)
c=clusters(g)
a=which(c$csize>=5)
nodes=c("node")
for (m in 1:length(a)){
  node=c(which(c$membership==a[m]))
  nodes=c(nodes,node)
}
write.table(nodes,file='data/OtherData/ARN_node.csv', sep=" ",
            row.names = FALSE, col.names = FALSE)
write.table(nodes,file='data/OtherData/ABAN_node.csv', sep=" ",
            row.names = FALSE, col.names = FALSE)
write.table(nodes,file='data/OtherData/CBEN_node.csv', sep=" ",
            row.names = FALSE, col.names = FALSE)
write.table(nodes,file='data/OtherData/VBEN_node.csv', sep=" ",
            row.names = FALSE, col.names = FALSE)
write.table(nodes,file='data/OtherData/VBEN2_node.csv', sep=" ",
            row.names = FALSE, col.names = FALSE)

#visualization
id_matrix=as.matrix(read.table(file='data/OtherData/1_ARN_matrix_prun.csv',sep=',',header=TRUE))
id_matrix = id_matrix[,2:2107]
id_matrix=as.matrix(read.table(file='data/OtherData/2_ABAN_matrix_prun.csv',sep=',',header=TRUE))
id_matrix = id_matrix[,2:1543]
id_matrix=as.matrix(read.table(file='data/OtherData/3_CBEN_matrix_prun.csv',sep=',',header=TRUE))
id_matrix = id_matrix[,2:540]
id_matrix=as.matrix(read.table(file='data/OtherData/4_VBEN_matrix_prun.csv',sep=',',header=TRUE))
id_matrix = id_matrix[,2:1497]
id_matrix=as.matrix(read.table(file='data/OtherData/5_VBEN2_matrix_prun.csv',sep=',',header=TRUE))
id_matrix = id_matrix[,2:2239]


#plot graph
gplot(id_matrix)


#page rank
library(igraph)
g=graph.adjacency(id_matrix)
p=page.rank(g)
n=as.data.frame(p[1])
r=c("rank",n)
write.table(r,file='Desktop/ARNrank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(r,file='Desktop/ABANrank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(r,file='Desktop/CBENrank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(r,file='Desktop/VBENrank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(r,file='Desktop/VBEN2rank.csv', sep=",",row.names = FALSE, col.names = FALSE)
x=sort(x=n,decreasing=TRUE)
index=order(x=n,decreasing=TRUE)[1:10]
node=c("node")
rank=c("rank")
for (m in 1:length(index)){
  node=c(node,index[m])
  rank=c(rank,x[m,1])
}
pagerank=data.frame(node,rank)
write.table(pagerank,file='data/OtherData/ARNpagerank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(pagerank,file='data/OtherData/ABANpagerank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(pagerank,file='data/OtherData/CBENpagerank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(pagerank,file='data/OtherData/VBENpagerank.csv', sep=",",row.names = FALSE, col.names = FALSE)
write.table(pagerank,file='data/OtherData/VBEN2pagerank.csv', sep=",",row.names = FALSE, col.names = FALSE)



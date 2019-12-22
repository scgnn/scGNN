import numpy as np
import networkx as nx
import community
from sklearn.metrics import silhouette_samples, silhouette_score
from visualize_util import * 

pvalueList=[]
with open('/home/wangjue/scRNA/VarID_analysis/pvalue.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        words = line.split(',')
        for word in words:
            pvalueList.append(word)    
    f.close()

edgeList = []
with open('/home/wangjue/scRNA/VarID_analysis/links.txt','r') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        words = line.split(',')
        for i in range(1,11):
            vvalue = float(pvalueList[count])
            if float(pvalueList[count])<0.01:
                vvalue = 0.0
            edgeList.append((int(words[0])-1,int(words[i])-1,vvalue))
            count += 1   
    f.close()

memberList = []
with open('/home/wangjue/scRNA/VarID_analysis/member.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        memberList.append(int(line)-1)    
    f.close()

z = pd.read_csv('/home/wangjue/scRNA/VarID_analysis/pca.csv')
z = z.to_numpy()
z = z.transpose()

modularity = calcuModularity(memberList, edgeList)
silhouette = calcuSilhouette(memberList, z)
print(str(modularity)+"\t"+str(silhouette))
    
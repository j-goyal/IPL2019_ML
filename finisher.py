import numpy as np
import pandas as pd

dataset = pd.read_csv('finishers.csv',encoding='cp1252')
x = dataset.iloc[:, 0:18].values

dataset2 = pd.read_csv('batsman.csv',encoding='cp1252')
batsman = dataset2.iloc[:,:].values
X2 = dataset2.iloc[:, [0]].values


li2 = list()

for i in X2:
    for j in i:
        li2.append(j.strip())

temp = list()

a = list()
for i in x:
    if i[6] in li2:
        a.append(i[6])
        temp.append(list(i))


di = dict()

for i in temp:
    if i[6] not in di:
        di[i[6]] = [1, i[15]]
    else:
        di[i[6]][0] = di[i[6]][0] + 1
        di[i[6]][1] = di[i[6]][1] + i[15]

sr = list()
for k,v in di.items():
    srt = (float(v[1])/float(v[0]))*100
    sr.append([k, round(srt,2),v[0],v[1]])

#print(sr)

li = list()
#li = [['PLAYER','Mat','Inns','NO','Runs','Avg','BF','SR','100','50','4s','6s','BF(16-20)','Runs(16-20)', 'SR(16-20)']

for i in sr:
    for j in batsman:
        if i[0] == j[0]:
            l = list(j)
            l.append(i[2])
            l.append(i[3])
            l.append(i[1])
            li.append(l)



dataset1 = pd.DataFrame(li)  #converting array to dataframe
export_csv = dataset1.to_csv(r'C:\Users\windows 10\Desktop\K_Means\ipl_batsman_finisher.csv', index = None, header=True)

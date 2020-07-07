import numpy as np
import pandas as pd

dataset = pd.read_csv('finishers.csv',encoding='cp1252')
x = dataset.iloc[:, 0:18].values

dataset4 = pd.read_csv('powerplay.csv',encoding='cp1252')
x1 = dataset4.iloc[:, 0:18].values

dataset2 = pd.read_csv('batsman.csv',encoding='cp1252')
batsman = dataset2.iloc[:,:].values
X2 = dataset2.iloc[:, [0]].values

li2 = list()

for i in X2:
    for j in i:
        li2.append(j.strip())

#print(li2)
temp = list()

a = list()
for i in x:
    if i[6] in li2:
        a.append(i[6])
        temp.append(list(i))


##########################3 powerplay ##########################
temp2 = list()

b = list()
for i in x1:
    if i[6] in li2:
        b.append(i[6])
        temp2.append(list(i))

#print(temp)


#dataset1 = pd.DataFrame(temp)  #converting array to dataframe
#export_csv = dataset1.to_csv(r'C:\Users\windows 10\Desktop\K_Means\finishing.csv', index = None, header=True)

di = dict()

for i in temp:
    if i[6] not in di:
        di[i[6]] = [1, i[15]]
    else:
        di[i[6]][0] = di[i[6]][0] + 1
        di[i[6]][1] = di[i[6]][1] + i[15]

#print(di)

di2 = dict()

for i in temp2:
    if i[6] not in di2:
        di2[i[6]] = [1, i[15]]
    else:
        di2[i[6]][0] = di2[i[6]][0] + 1
        di2[i[6]][1] = di2[i[6]][1] + i[15]



sr = list()
for k,v in di.items():
    srt = (float(v[1])/float(v[0]))*100
    sr.append([k, round(srt,2),v[0],v[1]])



sr2 = list()
for k,v in di2.items():
    srt2 = (float(v[1])/float(v[0]))*100
    sr2.append([k, round(srt2,2),v[0],v[1]])

#print(sr)
li = list()
#li = [['PLAYER','Mat','Inns','NO','Runs','Avg','BF','SR','100','50','4s','6s','BF(16-20)','Runs(16-20)', 'SR(16-20)','BF(1-6)','Runs(1-6)', 'SR(1-6)']]


for i in sr:
    for j in batsman:
        if i[0] == j[0]:
            l = list(j)
            l.append(i[2])
            l.append(i[3])
            l.append(i[1])
            li.append(l)

li2 = list()

for i in sr2:
    for j in li:
        if i[0] == j[0]:
            l = list(j)
            l.append(i[2])
            l.append(i[3])
            l.append(i[1])
            li2.append(l)

for i in li2:
    print(i)

header = ['PLAYER','Mat','Inns','NO','Runs','Avg','BF','SR','100','50','4s','6s','BF(16-20)','Runs(16-20)', 'SR(16-20)','BF(1-6)','Runs(1-6)', 'SR(1-6)']
li2.insert(0, header)



#dataset1 = pd.DataFrame(li2)  #converting array to dataframe
#export_csv = dataset1.to_csv(r'C:\Users\windows 10\Desktop\K_Means\ipl_batsman_final_statistics.csv', index = None, header=True)
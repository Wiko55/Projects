#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[79]:


dfs= {}
indexes= {}
k=0
w_diff=[]

def IndexAndDf(df,party_name,i=k):
        df_party = df[df.party==party_name]
        df_party = df_party.reset_index()
        df_party['index']=df_party.index
        women_1 = df_party[df_party.gender=='Woman']
        women_index = women_1.index[0]
        dfs[i] = df_party
        indexes[i] = women_index
        return women_index
        
def AvgDiffNthPlace(n,df_dictionary=dfs):
    diff_list = []
    for index in df_dictionary:
        df = df_dictionary[index]
        if df.shape[0] > n:
            prev = df['votes_percent'][n-1]
            nth = df['votes_percent'][n]
            diff = prev - nth
            diff_list.append(diff)
    return sum(diff_list)/len(diff_list)

def Diff(df,index):
    prev=df['votes_percent'][index-1]
    woman = df['votes_percent'][index]
    diff = prev - woman
    diff_list.append(diff)
    return diff


# In[80]:


for j in range(41):
    path = f'X:\Data Analysis\Wybory 2023\okreg_{j+1}_utf8.csv'
    dane = pd.read_csv(path,sep=";")
    df = pd.DataFrame(dane)
    df = df.drop(labels=['Nr okręgu','Liczba uwzględnionych komisji','Liczba komisji'], axis=1)
    column_names = list(df.columns.values)
    parties = []
    parties2 = []
    df2 = {'candidate':[], 'party':[], 'votes':[],'gender':[]}
    
    for party in parties:
        if parties.count(party)>2 and party not in parties2:
            parties2.append(party)
            
    for value in column_names:
        find=value.find(' KW ')
        if find == -1:
            find=value.find(' KKW ')
        name_surname=value[0:find-2]
        party_=value[find:].strip()
        df2['candidate'].append(name_surname)
        df2['party'].append(party_)
        name=name_surname.split()[1]
        if name[-1]=='a':
            gender='Woman'
        else:
            gender="Man"
        df2['gender'].append(gender)

    for i in range(len(df.axes[1])):
        df2['votes'].append(df.iloc[0,i])
    final_df=pd.DataFrame.from_dict(df2)
    parties=final_df.party.unique()
    parties=np.delete(parties, -1)
        
    for party in parties:
        IndexAndDf(final_df,party,k)
        k+=1


# In[81]:


final_indexes = []
final_dfs = []
diff_list=[]

for i in range(len(indexes)):
    if indexes[i]>0:
        final_indexes.append(i)
for index in final_indexes:
    final_dfs.append(dfs[index])
for index in dfs:
    df=dfs[index]
    df['votes_percent'] = df['votes']/sum(df['votes'])*100
    
for df in final_dfs:
    df['votes_percent']=df['votes']/sum(df['votes'])*100

for i, index in enumerate(final_indexes):
    df = final_dfs[i]
    final_dfs[i] = df[0:indexes[index]+1]
    Diff(final_dfs[i],indexes[index])
    


# In[82]:


i=final_indexes[11]
j=indexes[i]
plot_df = dfs[i]
party=plot_df['party'][0]
plt.plot(plot_df.index,plot_df.votes_percent,marker='o',markevery=[j],mec = 'black', mfc = 'red')
plt.title(f"{plot_df['party'][0]}",fontsize=10)
plt.suptitle("Percentage of votes among candidates", fontsize=16)
plt.xlabel("Position in list")
plt.ylabel("% of votes")
plt.annotate("1st woman", (j,plot_df.votes_percent[j]+1), color='red')
plt.show()


# In[83]:


avg_dif = round(sum(diff_list)/len(diff_list),2)
avg_dif


# In[84]:


for index in final_indexes:
    w_index = indexes[index]
    difference = Diff(dfs[index],w_index)-AvgDiffNthPlace(w_index,dfs)
    print(f'{Diff(dfs[index],w_index)} - {AvgDiffNthPlace(w_index,dfs)}')
    w_diff.append(difference)
    
avg = sum(w_diff)/len(w_diff)
avg = round(avg,2)


# In[85]:


diff_list


# In[86]:


avg


# In[ ]:





# In[ ]:





# In[ ]:





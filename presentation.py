# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:13:29 2022

@author: rana_
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from matplotlib.axis import Axis

st.set_page_config(page_title="French Election", layout="wide" )

data=pd.read_csv(r"C:\Users\rana_\OneDrive\Bureau\Final project\presentation\data.csv")

st.title("French Election 2022")


st.image('https://prmeng.rosselcdn.net/sites/default/files/dpistyles_v2/ena_16_9_extra_big/2022/03/07/node_285069/38906021/public/2022/03/07/B9730176814Z.1_20220307140937_000%2BGVJK1MA2E.1-0.jpg?itok=QaxdQPQK1646722555',
  width=400)


#######################table of candidats######################################
st.text("Candidats name")
candidat_number= pd.DataFrame(data['Candidat'].unique())
candidat_number.columns= ['candidat_name']
st.table(candidat_number)

#########################Voting results########################################

df_temp = data.groupby(['Candidat']).agg({'Voix':'sum','Exprimés': 'sum'})

df_temp['total_vot'] = df_temp.Voix *100/ df_temp.Exprimés
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
pie_fig=plt.figure(figsize=(4, 4))
bx = pie_fig.add_subplot(111)
bx=df_temp['total_vot'].plot(kind='pie', explode=explode, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 6}, radius=1)
plt.title('Voting results per candidate %')
st.pyplot(pie_fig)

###############################top 2 candidates################################


candidtes_top_2 =data.loc[(data['Candidat']=='Emmanuel MACRON') | (data['Candidat']=='Marine LE PEN')] 
candidtes_top_2 =data.loc[(data['Candidat']=='Emmanuel MACRON') | (data['Candidat']=='Marine LE PEN')] 
voting_Macron =candidtes_top_2.loc[(candidtes_top_2['Candidat']=='Emmanuel MACRON')] 
voting_Macron=voting_Macron.reset_index()

voting_Lepen =candidtes_top_2.loc[(candidtes_top_2['Candidat']=='Marine LE PEN')] 
voting_Lepen=voting_Lepen.reset_index()
res=pd.DataFrame()
res["Macron"]=voting_Macron['% Voix/Exp']
res["Le Pen"]=voting_Lepen['% Voix/Exp']
res['Macron'] = res['Macron'].str.replace(',','.').astype(float)
res['Le Pen'] = res['Le Pen'].str.replace(',','.').astype(float)
res["winner"]=res["Macron"] - res["Le Pen"]
res["Person"]=np.where(res.winner < 0,  "Le Pen", "Macron")

x=res.Person.value_counts()
explode = (0.1, 0.1)
pie_fig=plt.figure(figsize=(2, 1))
bx = pie_fig.add_subplot(111)
bx=res.Person.value_counts().plot(kind='pie', explode=explode, autopct='%1.1f%%', textprops={'fontsize': 3})
plt.title('Winners per commune')
st.pyplot(pie_fig)




#######################Map of clusters########################################
st.sidebar.markdown(" Clusters map  ")

from PIL import Image

image = Image.open("Image1.png")

st.image(image)

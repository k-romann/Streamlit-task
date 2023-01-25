import pandas as pd
import numpy as np
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


st.write('# Проведение анализа файла tips.csv')

path = pd.read_csv('tips.csv')
st.write(path.head(10))


st.write('### Ниже представлена гистограмма total bill')
fig = plt.figure(figsize=(10, 5))
sns.histplot(x='total_bill', data=path).set(title='Гистограмма Total bill')
st.pyplot(fig)


st.write('### Scatterplot, показывающая связь между total bill и tip')
fig = plt.figure(figsize=(10, 5))
sns.regplot(x='total_bill', y='tip', data=path).set(title= 'Диаграмма рассеяния')
st.pyplot(fig)


st.write('### График, связывающий total bill, tip, size')
fig = plt.figure(figsize=(10, 5))
sns.scatterplot(x='total_bill', y='tip', data=path, hue='size', size = 'size')
st.pyplot(fig)

st.write('### График, с днем недели по оси y, чаевыми по оси x, и цветом по полу')
fig = plt.figure(figsize=(10, 5))
sns.scatterplot(x="day", y="tip",hue='sex', data=path)
st.pyplot(fig)

st.write('### Box plot с суммой всех счетов за каждый день, разбитый по time (Dinner/Lunch)')
fig = plt.figure(figsize=(10, 5))
sns.boxplot(x='day', y='total_bill', hue='time', data=path)
st.pyplot(fig)

st.write('### 2 Гистограммы чаевых на обед и ланч')
fig = plt.figure(figsize=(10, 5))
sns.histplot(x='tip', data=path, hue='time')
st.pyplot(fig)

st.write('### Связь размера счета и чаевых, разбитый на курящих и некурящих')
fig, axes = plt.subplots(1, 2, sharex=True, figsize=(10,5))
sns.scatterplot(ax = axes[0], x ='total_bill', y='tip', data=path.loc[path['sex']=='Male'], hue='smoker')
axes[0].set_title('Male')
sns.scatterplot(ax = axes[1], x='total_bill', y='tip', data=path.loc[path['sex']=='Female'], hue='smoker')
axes[1].set_title('Female')
st.pyplot(fig)


st.write('### Scatter plot с днем недели по оси y, счетами по оси x, и цветом по полу')
fig = plt.figure(figsize=(10, 5))
sns.scatterplot(x="day", y="total_bill",hue='sex', data=path)
st.pyplot(fig)
#Козлова О.С. 3см 7 вариант
import streamlit as st
import pandas as pd

def var7_list(df, choice):
    df_nullcost = df[(df['Fare'] == 0)]
    result = df_nullcost[(df_nullcost['Survived'] == choice)]
    return result
def var7(df):
    st.subheader('Вариант 7: вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен / нет')
    choice = st.radio('Вас интересует список:', ['Спасен', 'Не спасен'])
    if choice == 'Спасен':
        choice = 1
    else:
        choice = 0
    st.dataframe(var7_list(df, choice))